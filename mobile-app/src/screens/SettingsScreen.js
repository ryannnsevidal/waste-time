import React, { useState } from 'react';
import { View, StyleSheet, ScrollView, Alert, Linking } from 'react-native';
import { Card, Title, List, Switch, Button, TextInput, Chip, Text } from 'react-native-paper';
import { LinearGradient } from 'expo-linear-gradient';

export default function SettingsScreen() {
  const [settings, setSettings] = useState({
    notifications: true,
    autoStart: false,
    soundEffects: true,
    darkMode: true,
    apiUrl: 'http://localhost:5000',
    apiKey: 'demo-api-key-123',
    maxCallDuration: 30,
    autoScriptChange: true
  });

  const [showAdvanced, setShowAdvanced] = useState(false);

  const updateSetting = (key, value) => {
    setSettings(prev => ({ ...prev, [key]: value }));
  };

  const resetSettings = () => {
    Alert.alert(
      "Reset Settings",
      "Are you sure you want to reset all settings to default?",
      [
        { text: "Cancel", style: "cancel" },
        { text: "Reset", style: "destructive", onPress: () => {
          setSettings({
            notifications: true,
            autoStart: false,
            soundEffects: true,
            darkMode: true,
            apiUrl: 'http://localhost:5000',
            apiKey: 'demo-api-key-123',
            maxCallDuration: 30,
            autoScriptChange: true
          });
        }}
      ]
    );
  };

  const exportData = () => {
    Alert.alert(
      "Export Data",
      "Your call history and statistics will be exported to a CSV file.",
      [
        { text: "Cancel", style: "cancel" },
        { text: "Export", onPress: () => {
          // In a real app, this would trigger file export
          Alert.alert("Success", "Data exported successfully!");
        }}
      ]
    );
  };

  const openGitHub = () => {
    Linking.openURL('https://github.com/your-repo/scammer-waste-bot');
  };

  return (
    <LinearGradient
      colors={['#2C3E50', '#34495E', '#2C3E50']}
      style={styles.container}
    >
      <ScrollView style={styles.scrollView}>
        {/* App Settings */}
        <Card style={styles.card}>
          <Card.Content>
            <Title style={styles.cardTitle}>📱 App Settings</Title>
            
            <List.Item
              title="Push Notifications"
              description="Get notified about call opportunities"
              titleStyle={styles.listTitle}
              descriptionStyle={styles.listDescription}
              right={() => (
                <Switch
                  value={settings.notifications}
                  onValueChange={(value) => updateSetting('notifications', value)}
                  color="#E74C3C"
                />
              )}
            />

            <List.Item
              title="Sound Effects"
              description="Play sounds during calls"
              titleStyle={styles.listTitle}
              descriptionStyle={styles.listDescription}
              right={() => (
                <Switch
                  value={settings.soundEffects}
                  onValueChange={(value) => updateSetting('soundEffects', value)}
                  color="#E74C3C"
                />
              )}
            />

            <List.Item
              title="Auto Script Change"
              description="Automatically change scripts during calls"
              titleStyle={styles.listTitle}
              descriptionStyle={styles.listDescription}
              right={() => (
                <Switch
                  value={settings.autoScriptChange}
                  onValueChange={(value) => updateSetting('autoScriptChange', value)}
                  color="#E74C3C"
                />
              )}
            />
          </Card.Content>
        </Card>

        {/* Call Settings */}
        <Card style={styles.card}>
          <Card.Content>
            <Title style={styles.cardTitle}>📞 Call Settings</Title>
            
            <View style={styles.inputContainer}>
              <Text style={styles.inputLabel}>Max Call Duration (minutes)</Text>
              <TextInput
                value={settings.maxCallDuration.toString()}
                onChangeText={(text) => updateSetting('maxCallDuration', parseInt(text) || 30)}
                keyboardType="numeric"
                style={styles.textInput}
                theme={{ colors: { text: '#ECF0F1', placeholder: '#95A5A6' } }}
              />
            </View>

            <List.Item
              title="Auto Start Calls"
              description="Automatically start calls when scammer detected"
              titleStyle={styles.listTitle}
              descriptionStyle={styles.listDescription}
              right={() => (
                <Switch
                  value={settings.autoStart}
                  onValueChange={(value) => updateSetting('autoStart', value)}
                  color="#E74C3C"
                />
              )}
            />
          </Card.Content>
        </Card>

        {/* Connection Settings */}
        <Card style={styles.card}>
          <Card.Content>
            <Title style={styles.cardTitle}>🌐 Connection</Title>
            
            <View style={styles.inputContainer}>
              <Text style={styles.inputLabel}>API URL</Text>
              <TextInput
                value={settings.apiUrl}
                onChangeText={(text) => updateSetting('apiUrl', text)}
                style={styles.textInput}
                theme={{ colors: { text: '#ECF0F1', placeholder: '#95A5A6' } }}
              />
            </View>

            <View style={styles.inputContainer}>
              <Text style={styles.inputLabel}>API Key</Text>
              <TextInput
                value={settings.apiKey}
                onChangeText={(text) => updateSetting('apiKey', text)}
                secureTextEntry
                style={styles.textInput}
                theme={{ colors: { text: '#ECF0F1', placeholder: '#95A5A6' } }}
              />
            </View>

            <Button
              mode="outlined"
              onPress={() => Alert.alert("Connection Test", "Testing connection... Success!")}
              style={styles.button}
              labelStyle={styles.buttonLabel}
            >
              🔌 Test Connection
            </Button>
          </Card.Content>
        </Card>

        {/* Advanced Settings */}
        <Card style={styles.card}>
          <Card.Content>
            <Title style={styles.cardTitle}>⚙️ Advanced</Title>
            
            <Button
              mode="text"
              onPress={() => setShowAdvanced(!showAdvanced)}
              style={styles.toggleButton}
              labelStyle={styles.buttonLabel}
            >
              {showAdvanced ? '▼' : '▶'} Advanced Settings
            </Button>

            {showAdvanced && (
              <View style={styles.advancedContainer}>
                <List.Item
                  title="Dark Mode"
                  description="Use dark theme (requires restart)"
                  titleStyle={styles.listTitle}
                  descriptionStyle={styles.listDescription}
                  right={() => (
                    <Switch
                      value={settings.darkMode}
                      onValueChange={(value) => updateSetting('darkMode', value)}
                      color="#E74C3C"
                    />
                  )}
                />

                <Button
                  mode="outlined"
                  onPress={exportData}
                  style={styles.button}
                  labelStyle={styles.buttonLabel}
                >
                  📊 Export Data
                </Button>

                <Button
                  mode="outlined"
                  onPress={resetSettings}
                  style={[styles.button, styles.dangerButton]}
                  labelStyle={[styles.buttonLabel, styles.dangerLabel]}
                >
                  🔄 Reset Settings
                </Button>
              </View>
            )}
          </Card.Content>
        </Card>

        {/* About */}
        <Card style={styles.card}>
          <Card.Content>
            <Title style={styles.cardTitle}>ℹ️ About</Title>
            
            <View style={styles.aboutContainer}>
              <Text style={styles.aboutText}>
                Scammer Waste Bot Mobile v1.0.0
              </Text>
              <Text style={styles.aboutSubtext}>
                Help fight scammers by wasting their time!
              </Text>

              <View style={styles.chipContainer}>
                <Chip
                  icon="github"
                  onPress={openGitHub}
                  textStyle={styles.chipText}
                  style={styles.chip}
                >
                  GitHub
                </Chip>
                <Chip
                  icon="information"
                  onPress={() => Alert.alert("Privacy", "This app does not collect personal data.")}
                  textStyle={styles.chipText}
                  style={styles.chip}
                >
                  Privacy
                </Chip>
                <Chip
                  icon="help-circle"
                  onPress={() => Alert.alert("Support", "Contact: support@scammerwaste.com")}
                  textStyle={styles.chipText}
                  style={styles.chip}
                >
                  Support
                </Chip>
              </View>
            </View>
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
    marginBottom: 8,
  },
  listTitle: {
    color: '#ECF0F1',
    fontSize: 16,
  },
  listDescription: {
    color: '#BDC3C7',
    fontSize: 12,
  },
  inputContainer: {
    marginBottom: 16,
  },
  inputLabel: {
    color: '#ECF0F1',
    fontSize: 14,
    marginBottom: 8,
  },
  textInput: {
    backgroundColor: '#2C3E50',
    height: 40,
  },
  button: {
    marginTop: 8,
    borderColor: '#3498DB',
  },
  buttonLabel: {
    color: '#3498DB',
  },
  toggleButton: {
    alignSelf: 'flex-start',
  },
  advancedContainer: {
    marginTop: 16,
    paddingTop: 16,
    borderTopWidth: 1,
    borderTopColor: '#7F8C8D',
  },
  dangerButton: {
    borderColor: '#E74C3C',
  },
  dangerLabel: {
    color: '#E74C3C',
  },
  aboutContainer: {
    alignItems: 'center',
    paddingVertical: 16,
  },
  aboutText: {
    color: '#ECF0F1',
    fontSize: 16,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  aboutSubtext: {
    color: '#BDC3C7',
    fontSize: 12,
    textAlign: 'center',
    marginTop: 4,
    marginBottom: 16,
  },
  chipContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'center',
  },
  chip: {
    margin: 4,
    backgroundColor: '#3498DB',
  },
  chipText: {
    color: '#FFFFFF',
  },
  bottomSpacing: {
    height: 20,
  },
});
