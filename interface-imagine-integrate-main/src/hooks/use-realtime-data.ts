import { useCallback, useEffect, useState } from 'react';

interface ApiData {
  totalTimeWasted: string;
  totalCalls: number;
  activeNow: number;
  successRate: string;
  totalSaved: string;
  thisWeek: string;
  recentCalls: Array<{
    id: string;
    phoneNumber: string;
    duration: number;
    scamType: string;
    strategy: string;
    timestamp: Date;
    success: boolean;
    wastedTime: number;
  }>;
  currentCall?: {
    id: string;
    phoneNumber: string;
    duration: number;
    status: "active" | "ended";
    scamType: string;
    strategy: string;
    wastedTime: number;
  } | null;
}

// Real API service connecting to Flask backend
class ApiService {
  private static instance: ApiService;
  private baseUrl = window.location.origin; // Use same host as frontend
  
  static getInstance(): ApiService {
    if (!ApiService.instance) {
      ApiService.instance = new ApiService();
    }
    return ApiService.instance;
  }

  // Get real-time stats from Flask backend
  async getStats(): Promise<ApiData> {
    try {
      const response = await fetch(`${this.baseUrl}/api/stats`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      
      // Transform the data to match our interface
      return {
        totalTimeWasted: data.totalTimeWasted || "0h 0m",
        totalCalls: data.totalCalls || 0,
        activeNow: data.activeNow || 0,
        successRate: data.successRate || "0%",
        totalSaved: data.totalSaved || "$0",
        thisWeek: data.thisWeek || "0%",
        recentCalls: (data.recentCalls || []).map((call: any) => ({
          ...call,
          timestamp: new Date(call.timestamp)
        })),
        currentCall: data.currentCall || null
      };
    } catch (error) {
      console.error('Failed to fetch stats:', error);
      throw error;
    }
  }

  async endCall(callId: string): Promise<void> {
    try {
      const response = await fetch(`${this.baseUrl}/api/calls/${callId}/end`, { 
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        }
      });
      
      if (!response.ok) {
        throw new Error(`Failed to end call: ${response.status}`);
      }
    } catch (error) {
      console.error('Failed to end call:', error);
      throw error;
    }
  }
}

export function useRealTimeData() {
  const [data, setData] = useState<ApiData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchData = useCallback(async () => {
    try {
      const newData = await ApiService.getInstance().getStats();
      setData(newData);
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch data');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    // Initial fetch
    fetchData();

    // Set up real-time updates every 2 seconds for active monitoring
    const interval = setInterval(fetchData, 2000);

    return () => clearInterval(interval);
  }, [fetchData]);

  const endCall = useCallback(async (callId: string) => {
    try {
      await ApiService.getInstance().endCall(callId);
      // Immediately refresh data
      await fetchData();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to end call');
    }
  }, [fetchData]);

  return {
    data,
    loading,
    error,
    refetch: fetchData,
    endCall
  };
}

export { ApiService };