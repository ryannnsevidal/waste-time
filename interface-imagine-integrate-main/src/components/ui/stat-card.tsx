import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { LucideIcon } from "lucide-react";
import { cn } from "@/lib/utils";

interface StatCardProps {
  title: string;
  value: string;
  change?: string;
  icon: LucideIcon;
  variant?: "default" | "success" | "warning" | "destructive";
  className?: string;
}

export function StatCard({
  title,
  value,
  change,
  icon: Icon,
  variant = "default",
  className,
}: StatCardProps) {
  const variantStyles = {
    default: "border-border bg-card",
    success: "border-success/20 bg-success/5",
    warning: "border-warning/20 bg-warning/5", 
    destructive: "border-destructive/20 bg-destructive/5",
  };

  const iconStyles = {
    default: "text-muted-foreground",
    success: "text-success",
    warning: "text-warning",
    destructive: "text-destructive",
  };

  return (
    <Card className={cn(
      "transition-all duration-300 hover:shadow-card hover:scale-105 relative overflow-hidden",
      variantStyles[variant],
      className
    )}>
      {/* Real-time pulse indicator */}
      <div className="absolute top-2 right-2 w-2 h-2 bg-success rounded-full animate-pulse opacity-60"></div>
      
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium text-muted-foreground">
          {title}
        </CardTitle>
        <Icon className={cn("h-4 w-4", iconStyles[variant])} />
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold transition-all duration-500">{value}</div>
        {change && (
          <p className="text-xs text-muted-foreground mt-1">
            {change}
          </p>
        )}
      </CardContent>
    </Card>
  );
}