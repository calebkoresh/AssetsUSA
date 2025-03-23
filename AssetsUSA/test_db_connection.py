import psycopg2
import boto3
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Function to get database credentials from AWS Secrets Manager
def get_secret():
    secret_name = "rds!cluster-648e97c0-cb80-44e8-be3b-12eb04421088"
    region_name = "us-east-2"
    
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        secret = get_secret_value_response['SecretString']
        return json.loads(secret)
    except Exception as e:
        print(f"Error retrieving secret: {e}")
        return None

# Get database credentials
db_credentials = get_secret()

if db_credentials:
    username = db_credentials['username']
    password = db_credentials['password']
else:
    print("Failed to retrieve credentials from AWS Secrets Manager.")
    # You could add fallback username/password here if needed
    exit(1)

# Get other database connection parameters from environment variables
db_host = os.environ.get('DB_HOST', 'assetsusa-1-instance-1.cre0ug0s4xql.us-east-2.rds.amazonaws.com')
db_port = os.environ.get('DB_PORT', '5432')
db_name = os.environ.get('DB_NAME', 'assetsusa-1')

print(f"Attempting to connect to {db_host}:{db_port}, database: {db_name}, user: {username}")

try:
    # Connect to the database
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=username,
        password=password
    )
    
    # Create a cursor
    cur = conn.cursor()
    
    # Execute a simple query
    cur.execute("SELECT version();")
    
    # Fetch the result
    version = cur.fetchone()
    print(f"Successfully connected to the database. PostgreSQL version: {version[0]}")
    
    # Close the cursor and connection
    cur.close()
    conn.close()
    
except Exception as e:
    print(f"Error connecting to the database: {e}") 