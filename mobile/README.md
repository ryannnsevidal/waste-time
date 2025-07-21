# Mobile App Setup Guide

## Quick Start

### Prerequisites
```bash
npm install -g expo-cli
npm install -g eas-cli
```

### Installation
```bash
cd mobile-app
npm install
```

### Development
```bash
# Start development server
npm start

# Run on Android
npm run android

# Run on iOS
npm run ios

# Run on web
npm run web
```

## Features

### Core Functionality
- **Real-time Dashboard** - Live statistics and call monitoring
- **Active Call Interface** - Script management and call controls
- **Comprehensive Stats** - Charts, analytics, and achievements
- **Settings Management** - Customizable app configuration

### Mobile-Specific Features
- **Cross-platform** - Works on iOS, Android, and web
- **Responsive Design** - Optimized for all screen sizes
- **Dark Theme** - Professional dark mode interface
- **Offline Support** - Core features work without internet
- **Push Notifications** - Real-time alerts and updates

## Screens

### 1. Dashboard Screen
- Live connection status
- Real-time statistics cards
- Call trends chart
- Quick action buttons
- Floating action button for new calls

### 2. Call Screen
- Active call status with pulse animation
- Scammer type selection (Tech Support, IRS, Romance)
- Dynamic script suggestions
- Waste level progress bar
- Call controls (start/end)

### 3. Stats Screen
- Overview statistics grid
- Daily calls line chart
- Scammer types pie chart
- Hourly activity bar chart
- Personal records table
- Achievement system
- Economic impact display

### 4. Settings Screen
- App preferences (notifications, sounds)
- Call configuration (duration, auto-start)
- Connection settings (API URL, key)
- Advanced options
- Data export functionality
- About information

## Configuration

### API Connection
Update the API URL in Settings screen or modify default in `SettingsScreen.js`:
```javascript
apiUrl: 'http://your-backend-url:5000'
apiKey: 'your-api-key'
```

### Customization
- **Colors**: Modify theme in `App.js`
- **Charts**: Configure chart settings in screen files
- **Scripts**: Update call scripts in `CallScreen.js`

## Building for Production

### Android
```bash
eas build --platform android
```

### iOS
```bash
eas build --platform ios
```

### Web
```bash
expo build:web
```

## Deployment

### Expo Publishing
```bash
expo publish
```

### App Stores
1. Build production versions with EAS Build
2. Submit to Google Play Store / Apple App Store
3. Configure app store listings and metadata

## Security Features

- **API Key Authentication** - Secure backend communication
- **Input Validation** - All user inputs sanitized
- **Secure Storage** - Sensitive settings encrypted
- **HTTPS Only** - Encrypted data transmission

## Analytics Integration

Ready for analytics services:
- **Expo Analytics** - Built-in user analytics
- **Custom Events** - Track call success rates
- **Performance Monitoring** - App performance metrics

## Troubleshooting

### Common Issues
1. **Metro bundler errors**: Clear cache with `expo r -c`
2. **Android build fails**: Check Java/Android SDK versions
3. **iOS simulator issues**: Reset simulator or restart
4. **Network errors**: Verify API URL and connectivity

### Debug Mode
```bash
expo start --dev-client
```

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes to mobile app
4. Test on multiple devices
5. Submit pull request

## License

MIT License - see LICENSE file for details

---

**Note**: This mobile app connects to the secure Flask backend created earlier. Make sure the backend is running and accessible from your mobile device network.
