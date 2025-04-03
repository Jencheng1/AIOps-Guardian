import React, { useEffect, useState } from 'react';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import { DataGrid } from '@mui/x-data-grid';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Alert from '@mui/material/Alert';
import CircularProgress from '@mui/material/CircularProgress';

interface Incident {
  id: string;
  title: string;
  severity: string;
  status: string;
  timestamp: string;
}

interface Metric {
  name: string;
  value: number;
  timestamp: string;
}

const Dashboard: React.FC = () => {
  const [incidents, setIncidents] = useState<Incident[]>([]);
  const [metrics, setMetrics] = useState<Metric[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Fetch incidents
        const incidentsResponse = await fetch('/api/incidents');
        const incidentsData = await incidentsResponse.json();
        setIncidents(incidentsData);

        // Fetch metrics
        const metricsResponse = await fetch('/api/metrics');
        const metricsData = await metricsResponse.json();
        setMetrics(metricsData);
      } catch (err) {
        setError('Failed to fetch dashboard data');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const incidentColumns = [
    { field: 'id', headerName: 'ID', width: 90 },
    { field: 'title', headerName: 'Title', width: 200 },
    { field: 'severity', headerName: 'Severity', width: 130 },
    { field: 'status', headerName: 'Status', width: 130 },
    { field: 'timestamp', headerName: 'Timestamp', width: 180 },
  ];

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="400px">
        <CircularProgress />
      </Box>
    );
  }

  if (error) {
    return (
      <Box m={2}>
        <Alert severity="error">{error}</Alert>
      </Box>
    );
  }

  return (
    <Grid container spacing={3}>
      {/* Summary Cards */}
      <Grid item xs={12} md={3}>
        <Card>
          <CardContent>
            <Typography color="textSecondary" gutterBottom>
              Active Incidents
            </Typography>
            <Typography variant="h4">
              {incidents.filter(i => i.status === 'active').length}
            </Typography>
          </CardContent>
        </Card>
      </Grid>
      <Grid item xs={12} md={3}>
        <Card>
          <CardContent>
            <Typography color="textSecondary" gutterBottom>
              Critical Incidents
            </Typography>
            <Typography variant="h4">
              {incidents.filter(i => i.severity === 'critical').length}
            </Typography>
          </CardContent>
        </Card>
      </Grid>
      <Grid item xs={12} md={3}>
        <Card>
          <CardContent>
            <Typography color="textSecondary" gutterBottom>
              Resolved Today
            </Typography>
            <Typography variant="h4">
              {incidents.filter(i => 
                i.status === 'resolved' && 
                new Date(i.timestamp).toDateString() === new Date().toDateString()
              ).length}
            </Typography>
          </CardContent>
        </Card>
      </Grid>
      <Grid item xs={12} md={3}>
        <Card>
          <CardContent>
            <Typography color="textSecondary" gutterBottom>
              Average Resolution Time
            </Typography>
            <Typography variant="h4">
              2.5h
            </Typography>
          </CardContent>
        </Card>
      </Grid>

      {/* Metrics Chart */}
      <Grid item xs={12}>
        <Paper sx={{ p: 2 }}>
          <Typography variant="h6" gutterBottom>
            System Metrics
          </Typography>
          <LineChart
            width={800}
            height={300}
            data={metrics}
            margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="timestamp" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="value" stroke="#8884d8" />
          </LineChart>
        </Paper>
      </Grid>

      {/* Incidents Table */}
      <Grid item xs={12}>
        <Paper sx={{ p: 2 }}>
          <Typography variant="h6" gutterBottom>
            Recent Incidents
          </Typography>
          <Box sx={{ height: 400, width: '100%' }}>
            <DataGrid
              rows={incidents}
              columns={incidentColumns}
              pageSize={5}
              rowsPerPageOptions={[5]}
              disableSelectionOnClick
            />
          </Box>
        </Paper>
      </Grid>
    </Grid>
  );
};

export default Dashboard; 