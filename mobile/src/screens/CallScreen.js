import React, { useState, useEffect } from 'react';
import { View, StyleSheet, ScrollView, Alert } from 'react-native';
import { Card, Title, Paragraph, Button, Chip, ProgressBar, Text } from 'react-native-paper';
import { LinearGradient } from 'expo-linear-gradient';

export default function CallScreen({ navigation }) {
  const [callActive, setCallActive] = useState(false);
  const [callDuration, setCallDuration] = useState(0);
  const [currentScript, setCurrentScript] = useState('');
  const [scammerType, setScammerType] = useState('Tech Support');
  const [wasteScore, setWasteScore] = useState(0);

  const scripts = {
    'Tech Support': [
      "Oh my, yes I'm having terrible computer problems!",
      "Wait, let me get my reading glasses...",
      "I'm 87 years old, can you speak slower please?",
      "My grandson usually helps me with this stuff...",
      "Hold on, my cat is walking on the keyboard again!"
    ],
    'IRS Scam': [
      "Oh no! Am I in trouble with the government?",
      "I've always paid my taxes on time!",
      "Should I call my lawyer? I'm so confused!",
      "Let me get my checkbook... where did I put it?",
      "Can you hold while I find my Social Security card?"
    ],
    'Romance Scam': [
      "You sound so handsome over the phone!",
      "I've been so lonely since Harold passed...",
      "Tell me more about yourself, dear!",
      "I need to ask my daughter about sending money...",
      "You remind me of my late husband!"
    ]
  };

  useEffect(() => {
    let interval;
    if (callActive) {
      interval = setInterval(() => {
        setCallDuration(prev => prev + 1);
        setWasteScore(prev => prev + Math.random() * 10);
        
        // Auto-update script every 30 seconds
        if (callDuration % 30 === 0) {
          const scriptArray = scripts[scammerType];
          const randomScript = scriptArray[Math.floor(Math.random() * scriptArray.length)];
          setCurrentScript(randomScript);
        }
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [callActive, callDuration, scammerType]);

  const startCall = () => {
    setCallActive(true);
    setCallDuration(0);
    setWasteScore(0);
    const scriptArray = scripts[scammerType];
    setCurrentScript(scriptArray[0]);
  };

  const endCall = () => {
    Alert.alert(
      "End Call",
      `Great job! You wasted ${formatTime(callDuration)} of a scammer's time!`,
      [
        { text: "Save & Exit", onPress: () => {
          setCallActive(false);
          navigation.goBack();
        }}
      ]
    );
  };

  const switchScript = () => {
    const types = Object.keys(scripts);
    const currentIndex = types.indexOf(scammerType);
    const nextIndex = (currentIndex + 1) % types.length;
    setScammerType(types[nextIndex]);
    
    const scriptArray = scripts[types[nextIndex]];
    setCurrentScript(scriptArray[0]);
  };

  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  const getWasteLevel = () => {
    if (wasteScore < 50) return { level: 'Warming Up', color: '#F39C12', progress: 0.2 };
    if (wasteScore < 150) return { level: 'Getting Hot', color: '#E67E22', progress: 0.5 };
    if (wasteScore < 300) return { level: 'On Fire!', color: '#E74C3C', progress: 0.8 };
    return { level: 'MAXIMUM WASTE!', color: '#C0392B', progress: 1.0 };
  };

  const wasteInfo = getWasteLevel();

  return (
    <LinearGradient
      colors={['#2C3E50', '#34495E', '#2C3E50']}
      style={styles.container}
    >
      <ScrollView style={styles.scrollView}>
        {/* Call Status */}
        <Card style={[styles.card, { backgroundColor: callActive ? '#27AE60' : '#95A5A6' }]}>
          <Card.Content>
            <Title style={styles.cardTitle}>
              {callActive ? '📞 Call Active' : '📵 Ready to Call'}
            </Title>
            <Paragraph style={styles.cardText}>
              Duration: {formatTime(callDuration)}
            </Paragraph>
            {callActive && (
              <View style={styles.pulseContainer}>
                <View style={[styles.pulse, styles.pulse1]} />
                <View style={[styles.pulse, styles.pulse2]} />
                <View style={[styles.pulse, styles.pulse3]} />
              </View>
            )}
          </Card.Content>
        </Card>

        {/* Scammer Type */}
        <Card style={styles.card}>
          <Card.Content>
            <Title style={styles.cardTitle}>🎭 Scammer Type</Title>
            <View style={styles.chipContainer}>
              <Chip
                selected={scammerType === 'Tech Support'}
                onPress={switchScript}
                textStyle={styles.chipText}
                style={[styles.chip, scammerType === 'Tech Support' && styles.selectedChip]}
              >
                💻 Tech Support
              </Chip>
              <Chip
                selected={scammerType === 'IRS Scam'}
                onPress={switchScript}
                textStyle={styles.chipText}
                style={[styles.chip, scammerType === 'IRS Scam' && styles.selectedChip]}
              >
                🏛️ IRS Scam
              </Chip>
              <Chip
                selected={scammerType === 'Romance Scam'}
                onPress={switchScript}
                textStyle={styles.chipText}
                style={[styles.chip, scammerType === 'Romance Scam' && styles.selectedChip]}
              >
                💕 Romance
              </Chip>
            </View>
          </Card.Content>
        </Card>

        {/* Current Script */}
        <Card style={styles.card}>
          <Card.Content>
            <Title style={styles.cardTitle}>🎬 Current Script</Title>
            <Text style={styles.scriptText}>"{currentScript}"</Text>
            <Button
              mode="outlined"
              onPress={() => {
                const scriptArray = scripts[scammerType];
                const randomScript = scriptArray[Math.floor(Math.random() * scriptArray.length)];
                setCurrentScript(randomScript);
              }}
              style={styles.button}
              labelStyle={styles.buttonLabel}
            >
              🔄 Next Line
            </Button>
          </Card.Content>
        </Card>

        {/* Waste Score */}
        <Card style={styles.card}>
          <Card.Content>
            <Title style={styles.cardTitle}>🔥 Waste Level</Title>
            <Text style={[styles.wasteLevel, { color: wasteInfo.color }]}>
              {wasteInfo.level}
            </Text>
            <ProgressBar
              progress={wasteInfo.progress}
              color={wasteInfo.color}
              style={styles.progressBar}
            />
            <Text style={styles.scoreText}>
              Score: {Math.floor(wasteScore)} points
            </Text>
          </Card.Content>
        </Card>

        {/* Call Controls */}
        <Card style={styles.card}>
          <Card.Content>
            <Title style={styles.cardTitle}>🎮 Controls</Title>
            <View style={styles.controlsContainer}>
              {!callActive ? (
                <Button
                  mode="contained"
                  onPress={startCall}
                  style={[styles.controlButton, { backgroundColor: '#27AE60' }]}
                  labelStyle={styles.controlButtonLabel}
                  icon="phone"
                >
                  Start Wasting Time
                </Button>
              ) : (
                <Button
                  mode="contained"
                  onPress={endCall}
                  style={[styles.controlButton, { backgroundColor: '#E74C3C' }]}
                  labelStyle={styles.controlButtonLabel}
                  icon="phone-hangup"
                >
                  End Call
                </Button>
              )}
            </View>
          </Card.Content>
        </Card>
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
  },
  cardText: {
    color: '#BDC3C7',
    fontSize: 16,
  },
  pulseContainer: {
    position: 'absolute',
    right: 20,
    top: 20,
    width: 20,
    height: 20,
  },
  pulse: {
    position: 'absolute',
    width: 20,
    height: 20,
    borderRadius: 10,
    backgroundColor: '#FFFFFF',
    opacity: 0.6,
  },
  pulse1: {
    transform: [{ scale: 1.0 }],
  },
  pulse2: {
    transform: [{ scale: 1.5 }],
  },
  pulse3: {
    transform: [{ scale: 2.0 }],
  },
  chipContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    marginTop: 8,
  },
  chip: {
    margin: 4,
    backgroundColor: '#95A5A6',
  },
  selectedChip: {
    backgroundColor: '#3498DB',
  },
  chipText: {
    color: '#FFFFFF',
  },
  scriptText: {
    color: '#ECF0F1',
    fontSize: 16,
    fontStyle: 'italic',
    marginVertical: 12,
    padding: 12,
    backgroundColor: '#2C3E50',
    borderRadius: 8,
  },
  button: {
    marginTop: 8,
    borderColor: '#3498DB',
  },
  buttonLabel: {
    color: '#3498DB',
  },
  wasteLevel: {
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'center',
    marginVertical: 8,
  },
  progressBar: {
    height: 8,
    borderRadius: 4,
    marginVertical: 8,
  },
  scoreText: {
    color: '#BDC3C7',
    textAlign: 'center',
    fontSize: 14,
  },
  controlsContainer: {
    marginTop: 16,
  },
  controlButton: {
    paddingVertical: 8,
  },
  controlButtonLabel: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: 'bold',
  },
});
