"""
Advanced Analytics Module for Scammer Waste Bot
Real-time dashboard with comprehensive metrics
"""
import json
import csv
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any
import statistics

class AnalyticsDashboard:
    """Advanced analytics for scammer waste bot performance"""
    
    def __init__(self):
        self.data_dir = os.path.join('data', 'analytics')
        self.ensure_data_directory()
        
    def ensure_data_directory(self):
        """Ensure analytics data directory exists"""
        os.makedirs(self.data_dir, exist_ok=True)
        
    def get_real_time_stats(self) -> Dict[str, Any]:
        """Get real-time performance statistics"""
        conversations = self._load_conversation_data()
        
        if not conversations:
            return self._empty_stats()
        
        # Calculate key metrics
        total_conversations = len(conversations)
        total_time_wasted = sum(conv.get('duration_minutes', 0) for conv in conversations)
        avg_conversation_length = total_time_wasted / total_conversations if total_conversations > 0 else 0
        
        # Scammer technique analysis
        techniques = [conv.get('technique_type', 'unknown') for conv in conversations]
        technique_counts = {technique: techniques.count(technique) for technique in set(techniques)}
        
        # Success rate calculation
        successful_conversations = len([conv for conv in conversations if conv.get('success_rating', 0) > 7])
        success_rate = (successful_conversations / total_conversations * 100) if total_conversations > 0 else 0
        
        # Time-based analysis
        today_conversations = self._get_conversations_by_date(conversations, datetime.now().date())
        this_week = self._get_conversations_by_week(conversations)
        
        return {
            'overview': {
                'total_conversations': total_conversations,
                'total_time_wasted_hours': round(total_time_wasted / 60, 2),
                'average_conversation_minutes': round(avg_conversation_length, 2),
                'success_rate_percentage': round(success_rate, 1),
                'estimated_cost_to_scammers': round(total_time_wasted * 0.25, 2)  # $0.25 per minute
            },
            'today': {
                'conversations': len(today_conversations),
                'time_wasted_minutes': sum(conv.get('duration_minutes', 0) for conv in today_conversations),
                'top_technique': self._get_top_technique(today_conversations)
            },
            'this_week': {
                'conversations': len(this_week),
                'average_daily': round(len(this_week) / 7, 1),
                'total_time_hours': round(sum(conv.get('duration_minutes', 0) for conv in this_week) / 60, 2)
            },
            'techniques': technique_counts,
            'performance_trends': self._calculate_trends(conversations),
            'geographic_data': self._analyze_geographic_patterns(conversations),
            'effectiveness_by_time': self._analyze_time_patterns(conversations)
        }
    
    def _empty_stats(self) -> Dict[str, Any]:
        """Return empty stats structure"""
        return {
            'overview': {
                'total_conversations': 0,
                'total_time_wasted_hours': 0,
                'average_conversation_minutes': 0,
                'success_rate_percentage': 0,
                'estimated_cost_to_scammers': 0
            },
            'today': {'conversations': 0, 'time_wasted_minutes': 0, 'top_technique': 'none'},
            'this_week': {'conversations': 0, 'average_daily': 0, 'total_time_hours': 0},
            'techniques': {},
            'performance_trends': [],
            'geographic_data': {},
            'effectiveness_by_time': {}
        }
    
    def _load_conversation_data(self) -> List[Dict]:
        """Load conversation data from CSV files"""
        conversations = []
        csv_file = os.path.join(self.data_dir, 'conversations.csv')
        
        if not os.path.exists(csv_file):
            return conversations
            
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Convert numeric fields
                    if 'duration_minutes' in row:
                        row['duration_minutes'] = float(row.get('duration_minutes', 0))
                    if 'success_rating' in row:
                        row['success_rating'] = int(row.get('success_rating', 0))
                    if 'conversation_turn' in row:
                        row['conversation_turn'] = int(row.get('conversation_turn', 0))
                    
                    conversations.append(row)
        except Exception as e:
            print(f"Error loading conversation data: {e}")
            
        return conversations
    
    def _get_conversations_by_date(self, conversations: List[Dict], target_date) -> List[Dict]:
        """Filter conversations by specific date"""
        filtered = []
        for conv in conversations:
            try:
                conv_date = datetime.fromisoformat(conv.get('timestamp', '')).date()
                if conv_date == target_date:
                    filtered.append(conv)
            except (ValueError, TypeError):
                continue
        return filtered
    
    def _get_conversations_by_week(self, conversations: List[Dict]) -> List[Dict]:
        """Get conversations from the last 7 days"""
        week_ago = datetime.now() - timedelta(days=7)
        filtered = []
        
        for conv in conversations:
            try:
                conv_datetime = datetime.fromisoformat(conv.get('timestamp', ''))
                if conv_datetime >= week_ago:
                    filtered.append(conv)
            except (ValueError, TypeError):
                continue
                
        return filtered
    
    def _get_top_technique(self, conversations: List[Dict]) -> str:
        """Get the most common technique type"""
        if not conversations:
            return 'none'
            
        techniques = [conv.get('technique_type', 'unknown') for conv in conversations]
        return max(set(techniques), key=techniques.count) if techniques else 'unknown'
    
    def _calculate_trends(self, conversations: List[Dict]) -> List[Dict]:
        """Calculate performance trends over time"""
        trends = []
        
        # Group by day for the last 30 days
        for i in range(30):
            date = datetime.now().date() - timedelta(days=i)
            day_conversations = self._get_conversations_by_date(conversations, date)
            
            trends.append({
                'date': date.isoformat(),
                'conversations': len(day_conversations),
                'time_wasted_minutes': sum(conv.get('duration_minutes', 0) for conv in day_conversations),
                'success_rate': self._calculate_day_success_rate(day_conversations)
            })
        
        return sorted(trends, key=lambda x: x['date'])
    
    def _calculate_day_success_rate(self, day_conversations: List[Dict]) -> float:
        """Calculate success rate for a specific day"""
        if not day_conversations:
            return 0.0
            
        successful = len([conv for conv in day_conversations if conv.get('success_rating', 0) > 7])
        return round((successful / len(day_conversations)) * 100, 1)
    
    def _analyze_geographic_patterns(self, conversations: List[Dict]) -> Dict[str, int]:
        """Analyze geographic patterns in scammer calls"""
        # Simulated geographic data - in real implementation, 
        # this would use caller ID or IP geolocation
        countries = ['India', 'Nigeria', 'Philippines', 'Jamaica', 'Romania', 'Pakistan']
        geographic_data = {}
        
        for country in countries:
            # Simulate distribution based on common scammer origins
            if country == 'India':
                geographic_data[country] = len(conversations) // 3
            elif country == 'Nigeria':
                geographic_data[country] = len(conversations) // 4
            else:
                geographic_data[country] = len(conversations) // 10
                
        return geographic_data
    
    def _analyze_time_patterns(self, conversations: List[Dict]) -> Dict[str, float]:
        """Analyze effectiveness by time of day"""
        time_patterns = {
            'morning': 0,    # 6-12
            'afternoon': 0,  # 12-18
            'evening': 0,    # 18-22
            'night': 0       # 22-6
        }
        
        time_counts = {
            'morning': 0,
            'afternoon': 0,
            'evening': 0,
            'night': 0
        }
        
        for conv in conversations:
            try:
                conv_time = datetime.fromisoformat(conv.get('timestamp', ''))
                hour = conv_time.hour
                duration = conv.get('duration_minutes', 0)
                
                if 6 <= hour < 12:
                    time_patterns['morning'] += duration
                    time_counts['morning'] += 1
                elif 12 <= hour < 18:
                    time_patterns['afternoon'] += duration
                    time_counts['afternoon'] += 1
                elif 18 <= hour < 22:
                    time_patterns['evening'] += duration
                    time_counts['evening'] += 1
                else:
                    time_patterns['night'] += duration
                    time_counts['night'] += 1
                    
            except (ValueError, TypeError):
                continue
        
        # Calculate average duration for each time period
        for period in time_patterns:
            if time_counts[period] > 0:
                time_patterns[period] = round(time_patterns[period] / time_counts[period], 2)
        
        return time_patterns
    
    def log_conversation(self, conversation_data: Dict):
        """Log a completed conversation for analytics"""
        csv_file = os.path.join(self.data_dir, 'conversations.csv')
        
        # Ensure all required fields are present
        required_fields = [
            'timestamp', 'duration_minutes', 'technique_type', 'success_rating',
            'conversation_turn', 'scammer_frustration_level'
        ]
        
        for field in required_fields:
            if field not in conversation_data:
                conversation_data[field] = 0 if 'level' in field or 'rating' in field else 'unknown'
        
        # Check if file exists to determine if we need headers
        file_exists = os.path.exists(csv_file)
        
        try:
            with open(csv_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=conversation_data.keys())
                
                if not file_exists:
                    writer.writeheader()
                
                writer.writerow(conversation_data)
                
        except Exception as e:
            print(f"Error logging conversation: {e}")
    
    def generate_daily_report(self) -> Dict[str, Any]:
        """Generate comprehensive daily performance report"""
        stats = self.get_real_time_stats()
        today_stats = stats['today']
        
        report = {
            'report_date': datetime.now().date().isoformat(),
            'summary': {
                'conversations_handled': today_stats['conversations'],
                'total_time_wasted_minutes': today_stats['time_wasted_minutes'],
                'estimated_cost_impact': round(today_stats['time_wasted_minutes'] * 0.25, 2),
                'primary_technique_encountered': today_stats['top_technique']
            },
            'performance_metrics': {
                'average_conversation_length': round(
                    today_stats['time_wasted_minutes'] / max(today_stats['conversations'], 1), 2
                ),
                'efficiency_score': min(100, today_stats['conversations'] * 10),  # Max 100%
                'technique_diversity': len(stats['techniques'])
            },
            'recommendations': self._generate_recommendations(stats),
            'next_day_forecast': self._generate_forecast(stats)
        }
        
        return report
    
    def _generate_recommendations(self, stats: Dict) -> List[str]:
        """Generate actionable recommendations based on performance"""
        recommendations = []
        
        overview = stats['overview']
        
        if overview['success_rate_percentage'] < 70:
            recommendations.append("Consider updating response strategies for better engagement")
        
        if overview['average_conversation_minutes'] < 5:
            recommendations.append("Focus on extending conversation duration with time-wasting techniques")
        
        if len(stats['techniques']) < 3:
            recommendations.append("Prepare for diverse scammer techniques - expand response repertoire")
        
        if stats['today']['conversations'] == 0:
            recommendations.append("No conversations today - verify system is operational and accessible")
        
        return recommendations if recommendations else ["Performance is optimal - maintain current strategies"]
    
    def _generate_forecast(self, stats: Dict) -> Dict[str, Any]:
        """Generate forecast for next day based on trends"""
        trends = stats['performance_trends']
        
        if len(trends) < 7:
            return {'predicted_conversations': 0, 'confidence': 'low', 'expected_techniques': []}
        
        # Simple trend analysis
        recent_conversations = [day['conversations'] for day in trends[-7:]]
        avg_conversations = statistics.mean(recent_conversations) if recent_conversations else 0
        
        return {
            'predicted_conversations': round(avg_conversations),
            'confidence': 'medium' if len(trends) > 14 else 'low',
            'expected_techniques': list(stats['techniques'].keys())[:3]
        }


# Example usage and testing
if __name__ == "__main__":
    analytics = AnalyticsDashboard()
    
    # Generate sample data for demo
    sample_conversations = [
        {
            'timestamp': (datetime.now() - timedelta(hours=i)).isoformat(),
            'duration_minutes': 5 + (i % 10),
            'technique_type': ['tech_support', 'financial_fraud', 'authority_impersonation'][i % 3],
            'success_rating': 8 if i % 3 == 0 else 6,
            'conversation_turn': 10 + (i % 5),
            'scammer_frustration_level': i % 5
        }
        for i in range(20)
    ]
    
    # Log sample conversations
    for conv in sample_conversations:
        analytics.log_conversation(conv)
    
    # Get real-time stats
    stats = analytics.get_real_time_stats()
    
    print("📊 Analytics Dashboard Demo")
    print("=" * 50)
    print(f"Total Conversations: {stats['overview']['total_conversations']}")
    print(f"Time Wasted: {stats['overview']['total_time_wasted_hours']} hours")
    print(f"Success Rate: {stats['overview']['success_rate_percentage']}%")
    print(f"Cost to Scammers: ${stats['overview']['estimated_cost_to_scammers']}")
    
    print(f"\nTop Techniques:")
    for technique, count in stats['techniques'].items():
        print(f"  • {technique}: {count}")
    
    # Generate daily report
    report = analytics.generate_daily_report()
    print(f"\n📋 Daily Report Summary:")
    print(f"Date: {report['report_date']}")
    print(f"Conversations: {report['summary']['conversations_handled']}")
    print(f"Time Wasted: {report['summary']['total_time_wasted_minutes']} minutes")
    print(f"Recommendations: {len(report['recommendations'])}")
