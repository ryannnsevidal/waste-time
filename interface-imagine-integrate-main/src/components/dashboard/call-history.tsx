import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Phone, Clock, Shield, TrendingUp } from "lucide-react";

interface CallRecord {
  id: string;
  phoneNumber: string;
  duration: number;
  scamType: string;
  strategy: string;
  timestamp: Date;
  success: boolean;
  wastedTime: number;
}

interface CallHistoryProps {
  calls?: CallRecord[];
}

const mockCallHistory: CallRecord[] = [
  {
    id: "1",
    phoneNumber: "+1-555-FAKE-123",
    duration: 1247,
    scamType: "IRS Scam",
    strategy: "Confused Grandpa",
    timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000), // 2 hours ago
    success: true,
    wastedTime: 1247
  },
  {
    id: "2", 
    phoneNumber: "+1-555-FRAUD-456",
    duration: 892,
    scamType: "Tech Support",
    strategy: "Confused Grandpa",
    timestamp: new Date(Date.now() - 5 * 60 * 60 * 1000), // 5 hours ago
    success: true,
    wastedTime: 892
  },
  {
    id: "3",
    phoneNumber: "+1-555-SCAM-789",
    duration: 234,
    scamType: "Bank Fraud",
    strategy: "Confused Grandpa",
    timestamp: new Date(Date.now() - 8 * 60 * 60 * 1000), // 8 hours ago
    success: false,
    wastedTime: 234
  },
  {
    id: "4",
    phoneNumber: "+1-555-CHEAT-101",
    duration: 1834,
    scamType: "Social Security",
    strategy: "Confused Grandpa",
    timestamp: new Date(Date.now() - 12 * 60 * 60 * 1000), // 12 hours ago
    success: true,
    wastedTime: 1834
  },
  {
    id: "5",
    phoneNumber: "+1-555-TRICK-202",
    duration: 567,
    scamType: "Medicare Scam",
    strategy: "Confused Grandpa", 
    timestamp: new Date(Date.now() - 18 * 60 * 60 * 1000), // 18 hours ago
    success: true,
    wastedTime: 567
  }
];

export function CallHistory({ calls }: CallHistoryProps) {
  const formatTime = (seconds: number) => {
    const hours = Math.floor(seconds / 3600);
    const mins = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    
    if (hours > 0) {
      return `${hours}h ${mins}m ${secs}s`;
    }
    return `${mins}m ${secs}s`;
  };

  const formatTimestamp = (timestamp: Date) => {
    const now = new Date();
    const diffMs = now.getTime() - timestamp.getTime();
    const diffHours = Math.floor(diffMs / (1000 * 60 * 60));
    
    if (diffHours < 1) {
      const diffMins = Math.floor(diffMs / (1000 * 60));
      return `${diffMins}m ago`;
    }
    return `${diffHours}h ago`;
  };

  const getScamTypeBadgeVariant = (scamType: string) => {
    const variants: Record<string, "default" | "secondary" | "destructive" | "outline"> = {
      "IRS Scam": "destructive",
      "Tech Support": "default", 
      "Bank Fraud": "destructive",
      "Social Security": "secondary",
      "Medicare Scam": "outline"
    };
    return variants[scamType] || "default";
  };

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <Phone className="h-5 w-5" />
          Recent Call History
        </CardTitle>
      </CardHeader>
      <CardContent>
        <ScrollArea className="h-[400px] pr-4">
          <div className="space-y-4">
            {(calls || mockCallHistory).map((call) => (
              <div
                key={call.id}
                className="flex items-center justify-between p-4 border rounded-lg hover:bg-muted/50 transition-colors"
              >
                <div className="flex-1 space-y-2">
                  <div className="flex items-center gap-3">
                    <span className="font-mono text-sm">{call.phoneNumber}</span>
                    <Badge variant={getScamTypeBadgeVariant(call.scamType)}>
                      {call.scamType}
                    </Badge>
                    {call.success ? (
                      <Badge variant="outline" className="text-success border-success">
                        <Shield className="h-3 w-3 mr-1" />
                        Success
                      </Badge>
                    ) : (
                      <Badge variant="outline" className="text-muted-foreground">
                        Ended Early
                      </Badge>
                    )}
                  </div>

                  <div className="flex items-center gap-4 text-sm text-muted-foreground">
                    <div className="flex items-center gap-1">
                      <Clock className="h-3 w-3" />
                      <span>{formatTime(call.duration)}</span>
                    </div>
                    <div className="flex items-center gap-1">
                      <TrendingUp className="h-3 w-3" />
                      <span>Wasted: {formatTime(call.wastedTime)}</span>
                    </div>
                    <span>{formatTimestamp(call.timestamp)}</span>
                  </div>
                </div>

                <Button variant="ghost" size="sm">
                  View Details
                </Button>
              </div>
            ))}
          </div>
        </ScrollArea>
      </CardContent>
    </Card>
  );
}