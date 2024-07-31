import os
import sqlite3
from datetime import datetime

# Define folder paths
VIDEO_FOLDER = r'C:\Users\lawrence\Desktop\pythooon\visitors\recordings'
IN_RECORDS_FOLDER = r'C:\Users\lawrence\Desktop\pythooon\visitors\in'
OUT_RECORDS_FOLDER = r'C:\Users\lawrence\Desktop\pythooon\visitors\out'

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect('setup_database.db')

# Function to create tables
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recordings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        timestamp TEXT NOT NULL
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS in_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        timestamp TEXT NOT NULL
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS out_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        timestamp TEXT NOT NULL
    );
    ''')
    
    conn.commit()
    conn.close()

# Function to insert a recording
def insert_recording(name, timestamp):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO recordings (name, timestamp) VALUES (?, ?)', (name, timestamp))
    conn.commit()
    conn.close()

# Function to insert an "in" record
def insert_in_record(name, timestamp):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO in_records (name, timestamp) VALUES (?, ?)', (name, timestamp))
    conn.commit()
    conn.close()

# Function to insert an "out" record
def insert_out_record(name, timestamp):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO out_records (name, timestamp) VALUES (?, ?)', (name, timestamp))
    conn.commit()
    conn.close()

# Function to update a recording's timestamp
def update_recording_timestamp(name, new_timestamp):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE recordings SET timestamp = ? WHERE name = ?', (new_timestamp, name))
    conn.commit()
    conn.close()

# Function to process files in a directory
def process_files(folder_path, table):
    conn = connect_db()
    cursor = conn.cursor()
    
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            timestamp = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d %H:%M:%S')
            print(f"Processing file: {filename}, Timestamp: {timestamp}")  # Debug print statement
            if table == 'recordings':
                insert_recording(filename, timestamp)
            elif table == 'in_records':
                insert_in_record(filename, timestamp)
            elif table == 'out_records':
                insert_out_record(filename, timestamp)
    
    conn.commit()
    conn.close()

# Function to create indexes
def create_indexes():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_recordings_timestamp ON recordings (timestamp);')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_in_records_timestamp ON in_records (timestamp);')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_out_records_timestamp ON out_records (timestamp);')
    
    conn.commit()
    conn.close()

# Main execution
if __name__ == "__main__":
    # Create tables
    create_tables()
    
    # Process video files
    process_files(VIDEO_FOLDER, 'recordings')
    
    # Process images in the "in" records folder
    process_files(IN_RECORDS_FOLDER, 'in_records')
    
    # Process images in the "out" records folder
    process_files(OUT_RECORDS_FOLDER, 'out_records')
    
    # Example of updating a recording's timestamp
    update_recording_timestamp('Recording1.mp4', '2024-07-16 11:00:00')
    
    # Create indexes
    create_indexes()
    
    print("Database updated with files from folders and indexes created.")
