import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Phone, PhoneOff, Clock, Volume2 } from "lucide-react";
import { useState, useEffect } from "react";

interface CallData {
  id: string;
  phoneNumber: string;
  duration: number;
  status: "active" | "ended";
  scamType: string;
  strategy: string;
  wastedTime: number;
}

interface LiveCallMonitorProps {
  activeCall?: CallData | null;
  onEndCall?: (callId: string) => void;
}

export function LiveCallMonitor({ activeCall: propActiveCall, onEndCall }: LiveCallMonitorProps) {
  const [activeCall, setActiveCall] = useState<CallData | null>(propActiveCall || null);
  const [timer, setTimer] = useState(propActiveCall?.duration || 0);

  // Update when prop changes
  useEffect(() => {
    setActiveCall(propActiveCall || null);
    setTimer(propActiveCall?.duration || 0);
  }, [propActiveCall]);

  useEffect(() => {
    if (activeCall?.status === "active") {
      const interval = setInterval(() => {
        setTimer(prev => prev + 1);
        if (activeCall) {
          setActiveCall(prev => prev ? { ...prev, duration: timer + 1, wastedTime: timer + 1 } : null);
        }
      }, 1000);
      return () => clearInterval(interval);
    }
  }, [activeCall?.status, timer]);

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  const endCall = () => {
    if (activeCall && onEndCall) {
      onEndCall(activeCall.id);
    }
  };

  return (
    <Card className="border-primary/20 bg-gradient-primary">
      <CardHeader>
        <CardTitle className="flex items-center gap-2 text-primary-foreground">
          {activeCall?.status === "active" ? (
            <>
              <Phone className="h-5 w-5 animate-pulse-glow" />
              Live Call in Progress
            </>
          ) : (
            <>
              <PhoneOff className="h-5 w-5" />
              No Active Calls
            </>
          )}
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        {activeCall && activeCall.status === "active" ? (
          <>
            <div className="flex justify-between items-center">
              <span className="text-primary-foreground/80">Scammer Number:</span>
              <span className="font-mono text-primary-foreground">{activeCall.phoneNumber}</span>
            </div>

            <div className="flex justify-between items-center">
              <span className="text-primary-foreground/80">Call Duration:</span>
              <div className="flex items-center gap-2 text-primary-foreground">
                <Clock className="h-4 w-4" />
                <span className="font-mono font-bold text-xl">{formatTime(timer)}</span>
              </div>
            </div>

            <div className="flex justify-between items-center">
              <span className="text-primary-foreground/80">Scam Type:</span>
              <Badge variant="secondary">{activeCall.scamType}</Badge>
            </div>

            <div className="flex justify-between items-center">
              <span className="text-primary-foreground/80">Bot Strategy:</span>
              <Badge variant="outline" className="text-primary-foreground border-primary-foreground/30">
                {activeCall.strategy}
              </Badge>
            </div>

            <div className="pt-4 flex gap-2">
              <Button 
                variant="destructive" 
                onClick={endCall}
                className="flex-1"
              >
                <PhoneOff className="h-4 w-4 mr-2" />
                End Call
              </Button>
              <Button variant="outline" className="text-primary-foreground border-primary-foreground/30">
                <Volume2 className="h-4 w-4" />
              </Button>
            </div>

            <div className="text-center pt-2 border-t border-primary-foreground/20">
              <span className="text-primary-foreground/80 text-sm">Time Wasted: </span>
              <span className="text-primary-foreground font-bold text-lg">{formatTime(activeCall.wastedTime)}</span>
            </div>
          </>
        ) : (
          <div className="text-center py-8 text-primary-foreground/60">
            <PhoneOff className="h-12 w-12 mx-auto mb-4 opacity-50" />
            <p>Bot is ready and waiting for scammer calls...</p>
          </div>
        )}
      </CardContent>
    </Card>
  );
}