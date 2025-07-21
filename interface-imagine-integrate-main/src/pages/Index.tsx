import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { StatCard } from "@/components/ui/stat-card";
import { LiveCallMonitor } from "@/components/dashboard/live-call-monitor";
import { CallHistory } from "@/components/dashboard/call-history";
import { AnalyticsCharts } from "@/components/dashboard/analytics-charts";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { useRealTimeData } from "@/hooks/use-realtime-data";
import { 
  Phone, 
  Clock, 
  Shield, 
  TrendingUp, 
  Users, 
  DollarSign,
  AlertTriangle,
  Settings,
  Activity,
  BrainCircuit,
  Smartphone,
  Download
} from "lucide-react";

const Index = () => {
  const { data, loading, error, endCall } = useRealTimeData();

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-dashboard flex items-center justify-center">
        <div className="text-center">
          <BrainCircuit className="h-12 w-12 mx-auto mb-4 animate-spin text-primary" />
          <p className="text-muted-foreground">Connecting to backend...</p>
          <p className="text-xs text-muted-foreground mt-2">Loading real-time data...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gradient-dashboard flex items-center justify-center">
        <div className="text-center">
          <AlertTriangle className="h-12 w-12 mx-auto mb-4 text-destructive" />
          <p className="text-destructive">Connection Error: {error}</p>
          <p className="text-xs text-muted-foreground mt-2">Check if the Flask backend is running</p>
        </div>
      </div>
    );
  }

  const stats = data || {
    totalTimeWasted: "0h 0m",
    totalCalls: 0,
    activeNow: 0,
    successRate: "0%",
    totalSaved: "$0",
    thisWeek: "0%"
  };

  return (
    <div className="min-h-screen bg-gradient-dashboard">
      {/* Header */}
      <header className="border-b bg-card/50 backdrop-blur-sm sticky top-0 z-10">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="p-2 rounded-lg bg-gradient-primary">
                <BrainCircuit className="h-6 w-6 text-primary-foreground" />
              </div>
              <div>
                <h1 className="text-2xl font-bold">Scammer Waste Bot</h1>
                <p className="text-sm text-muted-foreground">AI-Powered Scammer Time Waster</p>
              </div>
            </div>
            
            <div className="flex items-center gap-4">
              <Badge variant="outline" className="text-success border-success">
                <div className="w-2 h-2 bg-success rounded-full mr-2 animate-pulse"></div>
                Live Data
              </Badge>
              <Badge variant="outline" className="text-success border-success">
                <Activity className="h-3 w-3 mr-1" />
                Bot Active
              </Badge>
              <Button variant="outline" size="sm">
                <Smartphone className="h-4 w-4 mr-2" />
                <Download className="h-4 w-4 mr-2" />
                Get Mobile App
              </Button>
              <Button variant="outline" size="sm">
                <Settings className="h-4 w-4 mr-2" />
                Settings
              </Button>
            </div>
          </div>
        </div>
      </header>

      <main className="container mx-auto px-6 py-8 space-y-8">
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-6">
          <StatCard
            title="Total Time Wasted"
            value={stats.totalTimeWasted}
            change={`${stats.thisWeek} this week`}
            icon={Clock}
            variant="success"
            className="lg:col-span-2"
          />
          
          <StatCard
            title="Total Calls Intercepted"
            value={stats.totalCalls.toString()}
            change={`Last updated: ${new Date().toLocaleTimeString()}`}
            icon={Phone}
            variant="default"
          />
          
          <StatCard
            title="Active Calls"
            value={stats.activeNow.toString()}
            icon={Activity}
            variant={stats.activeNow > 0 ? "warning" : "default"}
          />
          
          <StatCard
            title="Success Rate"
            value={stats.successRate}
            change="Real-time calculation"
            icon={Shield}
            variant="success"
          />
          
          <StatCard
            title="Money Saved"
            value={stats.totalSaved}
            change="Estimated victim savings"
            icon={DollarSign}
            variant="success"
          />
        </div>

        <div className="grid gap-6 lg:grid-cols-3">
          <div className="lg:col-span-1">
            <LiveCallMonitor 
              activeCall={data?.currentCall} 
              onEndCall={endCall}
            />
          </div>
          
          <div className="lg:col-span-2">
            <CallHistory calls={data?.recentCalls} />
          </div>
        </div>

        {/* Analytics Dashboard */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <TrendingUp className="h-5 w-5" />
              Analytics Dashboard
            </CardTitle>
          </CardHeader>
          <CardContent>
            <AnalyticsCharts />
          </CardContent>
        </Card>

        {/* Recent Alerts */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <AlertTriangle className="h-5 w-5" />
              Recent Alerts & System Status
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              <div className="flex items-center gap-3 p-3 border rounded-lg bg-success/5 border-success/20">
                <Shield className="h-4 w-4 text-success" />
                <div className="flex-1">
                  <p className="text-sm font-medium">Successful call intercept</p>
                  <p className="text-xs text-muted-foreground">IRS scammer kept busy for 20 minutes - 2 hours ago</p>
                </div>
                <Badge variant="outline" className="text-success border-success">Success</Badge>
              </div>
              
              <div className="flex items-center gap-3 p-3 border rounded-lg bg-warning/5 border-warning/20">
                <AlertTriangle className="h-4 w-4 text-warning" />
                <div className="flex-1">
                  <p className="text-sm font-medium">New scam pattern detected</p>
                  <p className="text-xs text-muted-foreground">AI identified new cryptocurrency scam variant - 4 hours ago</p>
                </div>
                <Badge variant="outline" className="text-warning border-warning">New Pattern</Badge>
              </div>
              
              <div className="flex items-center gap-3 p-3 border rounded-lg">
                <Activity className="h-4 w-4 text-primary" />
                <div className="flex-1">
                  <p className="text-sm font-medium">System health check passed</p>
                  <p className="text-xs text-muted-foreground">All AI models and integrations operational - 6 hours ago</p>
                </div>
                <Badge variant="outline">Healthy</Badge>
              </div>
            </div>
          </CardContent>
        </Card>
      </main>
    </div>
  );
};

export default Index;
