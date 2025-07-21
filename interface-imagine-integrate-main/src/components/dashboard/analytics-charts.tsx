import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { 
  LineChart, 
  Line, 
  AreaChart, 
  Area, 
  BarChart, 
  Bar, 
  PieChart, 
  Pie, 
  Cell,
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  ResponsiveContainer,
  Legend
} from "recharts";
import { TrendingUp, Clock, Phone, Shield } from "lucide-react";

// Mock data for charts
const timeWastedData = [
  { day: "Mon", timeWasted: 3420, calls: 8 },
  { day: "Tue", timeWasted: 4567, calls: 12 },
  { day: "Wed", timeWasted: 2890, calls: 6 },
  { day: "Thu", timeWasted: 5234, calls: 15 },
  { day: "Fri", timeWasted: 6789, calls: 18 },
  { day: "Sat", timeWasted: 4321, calls: 11 },
  { day: "Sun", timeWasted: 3876, calls: 9 }
];

const hourlyData = [
  { hour: "00", calls: 1 },
  { hour: "01", calls: 0 },
  { hour: "02", calls: 0 },
  { hour: "03", calls: 1 },
  { hour: "04", calls: 0 },
  { hour: "05", calls: 0 },
  { hour: "06", calls: 2 },
  { hour: "07", calls: 3 },
  { hour: "08", calls: 5 },
  { hour: "09", calls: 8 },
  { hour: "10", calls: 12 },
  { hour: "11", calls: 15 },
  { hour: "12", calls: 18 },
  { hour: "13", calls: 16 },
  { hour: "14", calls: 14 },
  { hour: "15", calls: 11 },
  { hour: "16", calls: 8 },
  { hour: "17", calls: 6 },
  { hour: "18", calls: 4 },
  { hour: "19", calls: 3 },
  { hour: "20", calls: 2 },
  { hour: "21", calls: 1 },
  { hour: "22", calls: 1 },
  { hour: "23", calls: 0 }
];

const scamTypeData = [
  { name: "Tech Support", value: 35, color: "hsl(var(--primary))" },
  { name: "IRS Scam", value: 25, color: "hsl(var(--destructive))" },
  { name: "Bank Fraud", value: 20, color: "hsl(var(--warning))" },
  { name: "Social Security", value: 12, color: "hsl(var(--accent))" },
  { name: "Medicare", value: 8, color: "hsl(var(--success))" }
];

export function AnalyticsCharts() {
  const formatTime = (seconds: number) => {
    const hours = Math.floor(seconds / 3600);
    const mins = Math.floor((seconds % 3600) / 60);
    return `${hours}h ${mins}m`;
  };

  return (
    <div className="space-y-6">
      <Tabs defaultValue="overview" className="w-full">
        <TabsList className="grid w-full grid-cols-4">
          <TabsTrigger value="overview">Overview</TabsTrigger>
          <TabsTrigger value="patterns">Patterns</TabsTrigger>
          <TabsTrigger value="scams">Scam Types</TabsTrigger>
          <TabsTrigger value="performance">Performance</TabsTrigger>
        </TabsList>

        <TabsContent value="overview" className="space-y-6">
          <div className="grid gap-6 md:grid-cols-2">
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <TrendingUp className="h-5 w-5" />
                  Weekly Time Wasted
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ResponsiveContainer width="100%" height={300}>
                  <AreaChart data={timeWastedData}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="day" />
                    <YAxis tickFormatter={formatTime} />
                    <Tooltip 
                      labelFormatter={(label) => `Day: ${label}`}
                      formatter={(value: number) => [formatTime(value), "Time Wasted"]}
                    />
                    <Area 
                      type="monotone" 
                      dataKey="timeWasted" 
                      stroke="hsl(var(--primary))" 
                      fill="hsl(var(--primary) / 0.2)" 
                    />
                  </AreaChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Phone className="h-5 w-5" />
                  Daily Call Volume
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={timeWastedData}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="day" />
                    <YAxis />
                    <Tooltip />
                    <Bar 
                      dataKey="calls" 
                      fill="hsl(var(--accent))" 
                      radius={[4, 4, 0, 0]}
                    />
                  </BarChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>
          </div>
        </TabsContent>

        <TabsContent value="patterns" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Clock className="h-5 w-5" />
                Hourly Call Patterns (24h)
              </CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={400}>
                <LineChart data={hourlyData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="hour" />
                  <YAxis />
                  <Tooltip 
                    labelFormatter={(label) => `${label}:00`}
                    formatter={(value: number) => [value, "Calls"]}
                  />
                  <Line 
                    type="monotone" 
                    dataKey="calls" 
                    stroke="hsl(var(--primary))" 
                    strokeWidth={3}
                    dot={{ fill: "hsl(var(--primary))", strokeWidth: 2, r: 4 }}
                  />
                </LineChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="scams" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Shield className="h-5 w-5" />
                Scam Type Distribution
              </CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={400}>
                <PieChart>
                  <Pie
                    data={scamTypeData}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                    outerRadius={120}
                    fill="#8884d8"
                    dataKey="value"
                  >
                    {scamTypeData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip />
                  <Legend />
                </PieChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="performance" className="space-y-6">
          <div className="grid gap-6 md:grid-cols-2">
            <Card>
              <CardHeader>
                <CardTitle>Success Rate Trends</CardTitle>
              </CardHeader>
              <CardContent>
                <ResponsiveContainer width="100%" height={250}>
                  <LineChart data={timeWastedData}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="day" />
                    <YAxis domain={[0, 100]} />
                    <Tooltip 
                      formatter={(value: number) => [`${value}%`, "Success Rate"]}
                    />
                    <Line 
                      type="monotone" 
                      dataKey="calls" 
                      stroke="hsl(var(--success))" 
                      strokeWidth={3}
                      dot={{ fill: "hsl(var(--success))" }}
                    />
                  </LineChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>Average Call Duration</CardTitle>
              </CardHeader>
              <CardContent>
                <ResponsiveContainer width="100%" height={250}>
                  <BarChart data={timeWastedData}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="day" />
                    <YAxis tickFormatter={(value) => `${Math.floor(value / 60)}m`} />
                    <Tooltip 
                      formatter={(value: number) => [formatTime(value / timeWastedData.find(d => d.timeWasted === value)?.calls || 1), "Avg Duration"]}
                    />
                    <Bar 
                      dataKey="timeWasted" 
                      fill="hsl(var(--warning))" 
                      radius={[4, 4, 0, 0]}
                    />
                  </BarChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>
          </div>
        </TabsContent>
      </Tabs>
    </div>
  );
}