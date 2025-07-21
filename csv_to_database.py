import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import glob
from datetime import datetime

class CSVtoDatabaseMigrator:
    def __init__(self, database_url=None):
        """Initialize the migrator with database connection"""
        self.database_url = database_url or os.environ.get('DATABASE_URL')
        if not self.database_url:
            raise ValueError("DATABASE_URL environment variable is required")
        
        self.engine = create_engine(self.database_url)
        self.csv_directory = "analytics_data"
    
    def create_analytics_table(self):
        """Create the analytics table if it doesn't exist"""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS scammer_analytics (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP,
            scammer_input TEXT,
            strategy VARCHAR(100),
            response_preview TEXT,
            urgency_score FLOAT,
            authority_score FLOAT,
            payment_score FLOAT,
            info_score FLOAT,
            frustration_score FLOAT,
            threat_score FLOAT,
            caps_ratio FLOAT,
            exclamation_count INTEGER,
            estimated_time_waste INTEGER,
            total_time_wasted INTEGER,
            scammer_frustration VARCHAR(50),
            is_high_urgency BOOLEAN,
            is_authority_claim BOOLEAN,
            is_payment_scam BOOLEAN,
            is_info_phishing BOOLEAN,
            is_threatening BOOLEAN,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            source_file VARCHAR(255)
        );
        """
        
        with self.engine.connect() as connection:
            connection.execute(create_table_sql)
            connection.commit()
        print("✅ Analytics table created successfully")
    
    def migrate_csv_files(self):
        """Migrate all CSV files to the database"""
        csv_files = glob.glob(f'{self.csv_directory}/*.csv')
        
        if not csv_files:
            print("❌ No CSV files found in analytics_data directory")
            return
        
        total_rows = 0
        for csv_file in csv_files:
            try:
                print(f"📊 Processing {csv_file}...")
                
                # Read CSV file
                df = pd.read_csv(csv_file)
                
                # Add source file column
                df['source_file'] = os.path.basename(csv_file)
                
                # Convert timestamp column if it exists
                if 'timestamp' in df.columns:
                    df['timestamp'] = pd.to_datetime(df['timestamp'])
                
                # Insert into database
                rows_inserted = df.to_sql(
                    'scammer_analytics', 
                    self.engine, 
                    if_exists='append', 
                    index=False,
                    method='multi'
                )
                
                total_rows += len(df)
                print(f"✅ {len(df)} rows inserted from {csv_file}")
                
            except Exception as e:
                print(f"❌ Error processing {csv_file}: {str(e)}")
        
        print(f"🎉 Migration completed! Total rows migrated: {total_rows}")
    
    def get_analytics_summary(self):
        """Get summary of analytics data"""
        query = """
        SELECT 
            COUNT(*) as total_interactions,
            AVG(urgency_score) as avg_urgency,
            AVG(frustration_score) as avg_frustration,
            SUM(estimated_time_waste) as total_time_wasted,
            COUNT(DISTINCT DATE(timestamp)) as active_days
        FROM scammer_analytics
        WHERE timestamp IS NOT NULL;
        """
        
        with self.engine.connect() as connection:
            result = connection.execute(query).fetchone()
            return {
                'total_interactions': result[0],
                'avg_urgency': round(result[1] or 0, 2),
                'avg_frustration': round(result[2] or 0, 2),
                'total_time_wasted': result[3] or 0,
                'active_days': result[4] or 0
            }

def main():
    """Main migration function"""
    print("🚀 Starting CSV to Database Migration...")
    
    # Check if DATABASE_URL is set
    if not os.environ.get('DATABASE_URL'):
        print("❌ DATABASE_URL environment variable not set")
        print("Set it like: export DATABASE_URL='postgresql://user:password@host:port/dbname'")
        return
    
    try:
        # Initialize migrator
        migrator = CSVtoDatabaseMigrator()
        
        # Create table
        migrator.create_analytics_table()
        
        # Migrate CSV data
        migrator.migrate_csv_files()
        
        # Show summary
        summary = migrator.get_analytics_summary()
        print("\n📈 Analytics Summary:")
        print(f"Total Interactions: {summary['total_interactions']}")
        print(f"Average Urgency Score: {summary['avg_urgency']}")
        print(f"Average Frustration Score: {summary['avg_frustration']}")
        print(f"Total Time Wasted: {summary['total_time_wasted']} minutes")
        print(f"Active Days: {summary['active_days']}")
        
    except Exception as e:
        print(f"❌ Migration failed: {str(e)}")

if __name__ == "__main__":
    main()
