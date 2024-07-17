import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk, ImageOps
from threading import Thread
import sqlite3
from scroll import create_rounded_button, open_popup
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record

# Function to connect to the database
def connect_db():
    return sqlite3.connect('setup_database.db')

# Function to create the recordings table if it doesn't exist
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recordings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Call create_table function to ensure the table is created
create_table()

# Function to insert a new recording into the database
def insert_recording(name, timestamp):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO recordings (name, timestamp) VALUES (?, ?)', (name, timestamp))
    conn.commit()
    conn.close()

# Function to fetch all recordings from the database
def fetch_recordings():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM recordings')
    recordings = cursor.fetchall()
    conn.close()
    return recordings

# Function to delete a recording from the database
def delete_recording(recording_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM recordings WHERE id = ?', (recording_id,))
    conn.commit()
    conn.close()

# Function to start OpenCV capture for in_out functionality
def start_in_out():
    try:
        Thread(target=in_out).start()
    except Exception as e:
        print(f"Error starting in_out: {e}")

# Function to start OpenCV capture for noise detection
def start_noise():
    try:
        Thread(target=noise).start()
    except Exception as e:
        print(f"Error starting noise detection: {e}")

# Function to start OpenCV capture for recording video
def start_record():
    try:
        Thread(target=record).start()
        insert_recording('Recording Name', '2024-07-16 12:00:00')  # Example of inserting a recording
    except Exception as e:
        print(f"Error starting recording: {e}")

# Function to start OpenCV capture for rectangle noise detection
def start_rect_noise():
    try:
        Thread(target=rect_noise).start()
    except Exception as e:
        print(f"Error starting rectangle noise detection: {e}")

# Create the main window
window = tk.Tk()
window.title("Cam-Sys")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('1080x760')
window.configure(bg='black')  # Set the background color to black

# Create a frame to hold the widgets
frame1 = tk.Frame(window, bg='black')

# Title label
label_title = tk.Label(frame1, text="Camera Analysis", fg='lime', bg='black')
label_font = font.Font(size=35, weight='bold', family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10, 10), column=2)

# Load and resize icons
icon = Image.open('icons/cam.png').resize((150, 150), Image.LANCZOS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon, bg='black')
label_icon.grid(row=1, pady=(5, 10), column=2)

# Add hover effect for cam.png
def on_enter(e):
    label_icon['bg'] = 'gray'

def on_leave(e):
    label_icon['bg'] = 'black'

label_icon.bind("<Enter>", on_enter)
label_icon.bind("<Leave>", on_leave)
label_icon.bind("<Button-1>", lambda e: open_popup(window, btn2_image, btn3_image, btn4_image, btn5_image, btn6_image,
                                                   start_rect_noise, start_in_out, start_record, start_noise))

# Load button icons and resize
def load_button_image(image_path):
    img = Image.open(image_path).resize((50, 50), Image.LANCZOS)
    img = ImageOps.expand(img, border=(25, 25), fill='black')  # Add padding for circular look
    img = ImageTk.PhotoImage(img)
    return img

btn2_image = load_button_image('icons/rectangle-of-cutted-line-geometrical-shape.png')
btn3_image = load_button_image('icons/web-camera.png')
btn4_image = load_button_image('icons/recording.png')
btn5_image = load_button_image('icons/exit.png')
btn6_image = load_button_image('icons/incognito.png')

# Pack the frame
frame1.pack(expand=True)

# Start the tkinter main loop
window.mainloop()
