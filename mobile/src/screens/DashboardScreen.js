import React, { useState, useEffect } from 'react';
import { View, StyleSheet, ScrollView, RefreshControl, Alert, Dimensions } from 'react-native';
import { Card, Title, Paragraph, Button, FAB, Portal, Provider, Text } from 'react-native-paper';
import { LinearGradient } from 'expo-linear-gradient';
import { LineChart } from 'react-native-chart-kit';
import axios from 'axios';

const screenWidth = Dimensions.get('window').width;

export default function DashboardScreen({ navigation }) {
  const [stats, setStats] = useState({
    totalCalls: 0,
    timeWasted: 0,
    activeCalls: 0,
    moneyWasted: 0
  });
  const [chartData, setChartData] = useState([]);
  const [refreshing, setRefreshing] = useState(false);
  const [isConnected, setIsConnected] = useState(false);

  useEffect(() => {
    fetchStats();
    const interval = setInterval(fetchStats, 5000);
    return () => clearInterval(interval);
  }, []);

  const fetchStats = async () => {
    try {
      // Replace with your actual backend URL
      const response = await axios.get('http://localhost:5000/api/stats', {
        headers: {
          'X-API-Key': 'demo-api-key-123'
        }
      });
      
      setStats(response.data);
      setIsConnected(true);
      
      // Update chart data
      const newChartData = [...chartData.slice(-6), response.data.totalCalls];
      setChartData(newChartData);
    } catch (error) {
      console.log('Connection error:', error.message);
      setIsConnected(false);
    }
  };

  const onRefresh = React.useCallback(() => {
    setRefreshing(true);
    fetchStats().finally(() => setRefreshing(false));
  }, []);

  const startNewCall = () => {
    Alert.alert(
      "Start New Call",
      "Do you want to start wasting a scammer's time?",
      [
        { text: "Cancel", style: "cancel" },
        { text: "Yes, Let's Go!", onPress: () => navigation.navigate('Call') }
      ]
    );
  };

  const formatTime = (seconds) => {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    return `${hours}h ${minutes}m ${secs}s`;
  };

  const chartConfig = {
    backgroundColor: '#2C3E50',
    backgroundGradientFrom: '#34495E',
    backgroundGradientTo: '#2C3E50',
    decimalPlaces: 0,
    color: (opacity = 1) => `rgba(255, 107, 107, ${opacity})`,
    labelColor: (opacity = 1) => `rgba(236, 240, 241, ${opacity})`,
    style: {
      borderRadius: 16
    },
    propsForDots: {
      r: '6',
      strokeWidth: '2',
      stroke: '#FF6B6B'
    }
  };

  return (
    <Provider>
      <LinearGradient
        colors={['#2C3E50', '#34495E', '#2C3E50']}
        style={styles.container}
      >
        <ScrollView
          style={styles.scrollView}
          refreshControl={
            <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
          }
        >
          {/* Connection Status */}
          <Card style={[styles.card, { backgroundColor: isConnected ? '#27AE60' : '#E74C3C' }]}>
            <Card.Content>
              <Title style={styles.cardTitle}>
                {isConnected ? '🟢 Connected' : '🔴 Disconnected'}
              </Title>
              <Paragraph style={styles.cardText}>
                {isConnected ? 'Bot is online and ready' : 'Check your connection'}
              </Paragraph>
            </Card.Content>
          </Card>

          {/* Stats Cards */}
          <View style={styles.statsRow}>
            <Card style={[styles.statCard, styles.callsCard]}>
              <Card.Content>
                <Title style={styles.statNumber}>{stats.totalCalls}</Title>
                <Paragraph style={styles.statLabel}>Total Calls</Paragraph>
              </Card.Content>
            </Card>

            <Card style={[styles.statCard, styles.timeCard]}>
              <Card.Content>
                <Title style={styles.statNumber}>{formatTime(stats.timeWasted)}</Title>
                <Paragraph style={styles.statLabel}>Time Wasted</Paragraph>
              </Card.Content>
            </Card>
          </View>

          <View style={styles.statsRow}>
            <Card style={[styles.statCard, styles.activeCard]}>
              <Card.Content>
                <Title style={styles.statNumber}>{stats.activeCalls}</Title>
                <Paragraph style={styles.statLabel}>Active Calls</Paragraph>
              </Card.Content>
            </Card>

            <Card style={[styles.statCard, styles.moneyCard]}>
              <Card.Content>
                <Title style={styles.statNumber}>${stats.moneyWasted}</Title>
                <Paragraph style={styles.statLabel}>Money Wasted</Paragraph>
              </Card.Content>
            </Card>
          </View>

          {/* Chart */}
          {chartData.length > 1 && (
            <Card style={styles.chartCard}>
              <Card.Content>
                <Title style={styles.cardTitle}>📈 Call Trends</Title>
                <LineChart
                  data={{
                    labels: Array(chartData.length).fill(''),
                    datasets: [{ data: chartData }]
                  }}
                  width={screenWidth - 60}
                  height={200}
                  chartConfig={chartConfig}
                  bezier
                  style={styles.chart}
                />
              </Card.Content>
            </Card>
          )}

          {/* Quick Actions */}
          <Card style={styles.card}>
            <Card.Content>
              <Title style={styles.cardTitle}>🎯 Quick Actions</Title>
              <View style={styles.buttonRow}>
                <Button
                  mode="contained"
                  onPress={() => navigation.navigate('Stats')}
                  style={[styles.actionButton, { backgroundColor: '#3498DB' }]}
                  labelStyle={styles.buttonLabel}
                >
                  📊 View Stats
                </Button>
                <Button
                  mode="contained"
                  onPress={() => navigation.navigate('Settings')}
                  style={[styles.actionButton, { backgroundColor: '#9B59B6' }]}
                  labelStyle={styles.buttonLabel}
                >
                  ⚙️ Settings
                </Button>
              </View>
            </Card.Content>
          </Card>

          <View style={styles.bottomSpacing} />
        </ScrollView>

        {/* Floating Action Button */}
        <FAB
          style={styles.fab}
          icon="phone-plus"
          color="#FFFFFF"
          onPress={startNewCall}
          label="Start Call"
        />
      </LinearGradient>
    </Provider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollView: {
    flex: 1,
    padding: 16,
  },
  card: {
    marginBottom: 16,
    backgroundColor: '#34495E',
    elevation: 4,
  },
  cardTitle: {
    color: '#ECF0F1',
    fontSize: 18,
    fontWeight: 'bold',
  },
  cardText: {
    color: '#BDC3C7',
  },
  statsRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 16,
  },
  statCard: {
    flex: 1,
    marginHorizontal: 4,
    elevation: 4,
  },
  callsCard: {
    backgroundColor: '#E74C3C',
  },
  timeCard: {
    backgroundColor: '#F39C12',
  },
  activeCard: {
    backgroundColor: '#27AE60',
  },
  moneyCard: {
    backgroundColor: '#8E44AD',
  },
  statNumber: {
    color: '#FFFFFF',
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  statLabel: {
    color: '#FFFFFF',
    textAlign: 'center',
    fontSize: 12,
  },
  chartCard: {
    backgroundColor: '#34495E',
    marginBottom: 16,
    elevation: 4,
  },
  chart: {
    marginVertical: 8,
    borderRadius: 16,
  },
  buttonRow: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginTop: 16,
  },
  actionButton: {
    flex: 1,
    marginHorizontal: 8,
  },
  buttonLabel: {
    color: '#FFFFFF',
    fontSize: 12,
  },
  fab: {
    position: 'absolute',
    margin: 16,
    right: 0,
    bottom: 0,
    backgroundColor: '#E74C3C',
  },
  bottomSpacing: {
    height: 80,
  },
});
