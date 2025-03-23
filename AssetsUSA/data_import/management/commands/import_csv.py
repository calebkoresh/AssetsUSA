import csv
import os
from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Import data from CSV files into the Aurora database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')
        parser.add_argument('table_name', type=str, help='Database table name')
        
    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        table_name = options['table_name']
        
        if not os.path.exists(csv_file_path):
            self.stdout.write(self.style.ERROR(f'File not found: {csv_file_path}'))
            return
            
        try:
            # Open the CSV file
            with open(csv_file_path, 'r', encoding='utf-8') as f:
                # Get column names from the first line
                reader = csv.reader(f)
                headers = next(reader)
                
                # Create table if it doesn't exist
                create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ("
                column_defs = []
                for header in headers:
                    # Assume text type for all columns - you can refine this as needed
                    column_defs.append(f'"{header}" TEXT')
                create_table_sql += ", ".join(column_defs) + ")"
                
                with connection.cursor() as cursor:
                    cursor.execute(create_table_sql)
                
                # Instead of using copy_expert, we'll use executemany with batch processing
                # Reset the file pointer to the beginning and skip the header
                f.seek(0)
                reader = csv.reader(f)
                next(reader)  # Skip the header row
                
                # Prepare the INSERT statement
                placeholders = ",".join(["%s"] * len(headers))
                columns = ",".join([f'"{h}"' for h in headers])
                insert_sql = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
                
                # Process in batches of 1000 rows for efficiency
                batch_size = 1000
                batch = []
                
                with connection.cursor() as cursor:
                    for row in reader:
                        batch.append(row)
                        
                        # Execute when batch size is reached
                        if len(batch) >= batch_size:
                            cursor.executemany(insert_sql, batch)
                            batch = []
                    
                    # Insert any remaining rows
                    if batch:
                        cursor.executemany(insert_sql, batch)
                    
                self.stdout.write(self.style.SUCCESS(f'Successfully imported data from {csv_file_path} to {table_name}'))
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing data: {e}'))