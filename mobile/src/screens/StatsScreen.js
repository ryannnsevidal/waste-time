import React, { useState, useEffect } from 'react';
import { View, StyleSheet, ScrollView, Dimensions } from 'react-native';
import { Card, Title, Paragraph, Text, DataTable } from 'react-native-paper';
import { LinearGradient } from 'expo-linear-gradient';
import { LineChart, BarChart, PieChart } from 'react-native-chart-kit';

const screenWidth = Dimensions.get('window').width;

export default function StatsScreen() {
  const [stats, setStats] = useState({
    totalCalls: 127,
    totalTimeWasted: 15420, // seconds
    averageCallTime: 121,
    topScammerType: 'Tech Support',
    successRate: 87,
    moneyWasted: 2340
  });

  const [chartData, setChartData] = useState({
    daily: [45, 52, 38, 67, 71, 83, 127],
    scammerTypes: [
      { name: 'Tech Support', population: 45, color: '#E74C3C', legendFontColor: '#ECF0F1' },
      { name: 'IRS Scam', population: 32, color: '#F39C12', legendFontColor: '#ECF0F1' },
      { name: 'Romance', population: 28, color: '#9B59B6', legendFontColor: '#ECF0F1' },
      { name: 'Other', population: 22, color: '#3498DB', legendFontColor: '#ECF0F1' }
    ],
    hourly: [12, 8, 5, 3, 2, 4, 8, 15, 23, 31, 28, 25, 22, 19, 24, 27, 29, 26, 21, 18, 16, 14, 13, 11]
  });

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
      r: '4',
      strokeWidth: '2',
      stroke: '#FF6B6B'
    }
  };

  const formatTime = (seconds) => {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    return `${hours}h ${minutes}m`;
  };

  const achievements = [
    { title: 'First Call', description: 'Made your first scammer waste time', unlocked: true },
    { title: 'Time Thief', description: 'Wasted 1 hour total', unlocked: true },
    { title: 'Master Waster', description: 'Wasted 10 hours total', unlocked: true },
    { title: 'Legend', description: 'Wasted 100 hours total', unlocked: false },
    { title: 'Script Master', description: 'Used all scammer types', unlocked: true },
    { title: 'Marathon', description: 'Single call over 30 minutes', unlocked: false }
  ];

  return (
    <LinearGradient
      colors={['#2C3E50', '#34495E', '#2C3E50']}
      style={styles.container}
    >
      <ScrollView style={styles.scrollView}>
        {/* Overview Stats */}
        <Card style={styles.card}>
          <Card.Content>
            <Title style={styles.cardTitle}>📊 Overview</Title>
            <View style={styles.statsGrid}>
              <View style={styles.statItem}>
                <Text style={styles.statNumber}>{stats.totalCalls}</Text>
                <Text style={styles.statLabel}>Total Calls</Text>
              </View>
              <View style={styles.statItem}>
                <Text style={styles.statNumber}>{formatTime(stats.totalTimeWasted)}</Text>
                <Text style={styles.statLabel}>Time Wasted</Text>
              </View>
              <View style={styles.statItem}>
                <Text style={styles.statNumber}>{stats.averageCallTime}s</Text>
                <Text style={styles.statLabel}>Average Call</Text>
              </View>
              <View style={styles.statItem}>
                <Text style={styles.statNumber}>{stats.successRate}%</Text>
                <Text style={styles.statLabel}>Success Rate</Text>
              </View>
            </View>
          </Card.Content>
        </Card>

        {/* Daily Calls Chart */}
        <Card style={styles.card}>
          <Card.Content>
            <Title style={styles.cardTitle}>📈 Daily Calls (Last 7 Days)</Title>
            <LineChart
              data={{
                labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                datasets: [{ data: chartData.daily }]
              }}
              width={screenWidth - 60}
              height={200}
              chartConfig={chartConfig}
              bezier
              style={styles.chart}
            />
          </Card.Content>
        </Card>

        {/* Scammer Types Pie Chart */}
        <Card style={styles.card}>
          <Card.Content>
            <Title style={styles.cardTitle}>🎭 Scammer Types</Title>
            <PieChart
              data={chartData.scammerTypes}
              width={screenWidth - 60}
              height={200}
              chartConfig={chartConfig}
              accessor="population"
              backgroundColor="transparent"
              paddingLeft="15"
              style={styles.chart}
            />
          </Card.Content>
        </Card>

        {/* Hourly Activity */}
        <Card style={styles.card}>
          <Card.Content>
            <Title style={styles.cardTitle}>🕐 Hourly Activity</Title>
            <BarChart
              data={{
                labels: ['0', '4', '8', '12', '16', '20'],
                datasets: [{ data: chartData.hourly.filter((_, i) => i % 4 === 0) }]
              }}
              width={screenWidth - 60}
              height={200}
              chartConfig={chartConfig}
              style={styles.chart}
              showValuesOnTopOfBars
            />
          </Card.Content>
        </Card>

        {/* Top Performers Table */}
        <Card style={styles.card}>
          <Card.Content>
            <Title style={styles.cardTitle}>🏆 Personal Records</Title>
            <DataTable>
              <DataTable.Header>
                <DataTable.Title textStyle={styles.tableHeader}>Record</DataTable.Title>
                <DataTable.Title textStyle={styles.tableHeader}>Value</DataTable.Title>
              </DataTable.Header>
              <DataTable.Row>
                <DataTable.Cell textStyle={styles.tableCell}>Longest Call</DataTable.Cell>
                <DataTable.Cell textStyle={styles.tableCell}>47 minutes</DataTable.Cell>
              </DataTable.Row>
              <DataTable.Row>
                <DataTable.Cell textStyle={styles.tableCell}>Best Day</DataTable.Cell>
                <DataTable.Cell textStyle={styles.tableCell}>12 calls</DataTable.Cell>
              </DataTable.Row>
              <DataTable.Row>
                <DataTable.Cell textStyle={styles.tableCell}>Most Wasted (Day)</DataTable.Cell>
                <DataTable.Cell textStyle={styles.tableCell}>3.2 hours</DataTable.Cell>
              </DataTable.Row>
              <DataTable.Row>
                <DataTable.Cell textStyle={styles.tableCell}>Favorite Script</DataTable.Cell>
                <DataTable.Cell textStyle={styles.tableCell}>Tech Support</DataTable.Cell>
              </DataTable.Row>
            </DataTable>
          </Card.Content>
        </Card>

        {/* Achievements */}
        <Card style={styles.card}>
          <Card.Content>
            <Title style={styles.cardTitle}>🏅 Achievements</Title>
            {achievements.map((achievement, index) => (
              <View key={index} style={[styles.achievement, !achievement.unlocked && styles.lockedAchievement]}>
                <Text style={[styles.achievementTitle, !achievement.unlocked && styles.lockedText]}>
                  {achievement.unlocked ? '✅' : '🔒'} {achievement.title}
                </Text>
                <Text style={[styles.achievementDesc, !achievement.unlocked && styles.lockedText]}>
                  {achievement.description}
                </Text>
              </View>
            ))}
          </Card.Content>
        </Card>

        {/* Money Impact */}
        <Card style={[styles.card, styles.moneyCard]}>
          <Card.Content>
            <Title style={styles.cardTitle}>💰 Economic Impact</Title>
            <Text style={styles.moneyText}>
              Estimated scammer revenue prevented: ${stats.moneyWasted}
            </Text>
            <Text style={styles.moneySubtext}>
              Based on average scammer earnings of $18.40 per successful call
            </Text>
          </Card.Content>
        </Card>

        <View style={styles.bottomSpacing} />
      </ScrollView>
    </LinearGradient>
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
    marginBottom: 12,
  },
  statsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  statItem: {
    width: '48%',
    alignItems: 'center',
    marginBottom: 16,
  },
  statNumber: {
    color: '#E74C3C',
    fontSize: 24,
    fontWeight: 'bold',
  },
  statLabel: {
    color: '#BDC3C7',
    fontSize: 12,
    marginTop: 4,
  },
  chart: {
    marginVertical: 8,
    borderRadius: 16,
  },
  tableHeader: {
    color: '#ECF0F1',
    fontWeight: 'bold',
  },
  tableCell: {
    color: '#BDC3C7',
  },
  achievement: {
    marginBottom: 12,
    padding: 12,
    backgroundColor: '#2C3E50',
    borderRadius: 8,
    borderLeftWidth: 4,
    borderLeftColor: '#27AE60',
  },
  lockedAchievement: {
    borderLeftColor: '#95A5A6',
    opacity: 0.6,
  },
  achievementTitle: {
    color: '#ECF0F1',
    fontSize: 16,
    fontWeight: 'bold',
  },
  achievementDesc: {
    color: '#BDC3C7',
    fontSize: 12,
    marginTop: 4,
  },
  lockedText: {
    color: '#7F8C8D',
  },
  moneyCard: {
    backgroundColor: '#27AE60',
  },
  moneyText: {
    color: '#FFFFFF',
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  moneySubtext: {
    color: '#D5DBDB',
    fontSize: 12,
    textAlign: 'center',
    marginTop: 8,
  },
  bottomSpacing: {
    height: 20,
  },
});
