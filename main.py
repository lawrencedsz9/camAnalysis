import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk, ImageOps
from threading import Thread
import sqlite3
import time
from datetime import datetime
from scroll import create_rounded_button, open_popup
from in_out import in_out
from motion import noise  # Update this import to match the correct file
from rect_noise import rect_noise
from record import record

def connect_db():
    return sqlite3.connect('setup_database.db')

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

create_table()

def insert_recording(name, timestamp):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO recordings (name, timestamp) VALUES (?, ?)', (name, timestamp))
    conn.commit()
    conn.close()

def fetch_recordings():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM recordings')
    recordings = cursor.fetchall()
    conn.close()
    return recordings

def delete_recording(recording_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM recordings WHERE id = ?', (recording_id,))
    conn.commit()
    conn.close()

def start_in_out(alert_label):
    try:
        Thread(target=in_out, args=(alert_label,)).start()
    except Exception as e:
        print(f"Error starting in_out: {e}")

def start_noise(alert_label):
    try:
        Thread(target=noise, args=(alert_label,)).start()
    except Exception as e:
        print(f"Error starting noise detection: {e}")

def start_record(alert_label):
    try:
        Thread(target=record, args=(alert_label,)).start()
        insert_recording('Recording Name', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # Example of inserting a recording
    except Exception as e:
        print(f"Error starting recording: {e}")

def start_rect_noise():
    try:
        Thread(target=rect_noise).start()
    except Exception as e:
        print(f"Error starting rectangle noise detection: {e}")

# Function to update the time label every second
def update_time():
    current_time = time.strftime('%I:%M:%S %p')
    label_time.config(text=current_time)
    window.after(1000, update_time)

window = tk.Tk()
window.title("Cam-Sys")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('640x480')  # Set the initial window size
window.configure(bg='black')  

# Create a frame to hold the widgets
frame1 = tk.Frame(window, bg='black')

label_title = tk.Label(frame1, text="Camera Analysis", fg='lime', bg='black')
label_font = font.Font(size=35, weight='bold', family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10, 10), column=1, columnspan=3)

label_time = tk.Label(frame1, text="", fg='white', bg='black')
time_font = font.Font(size=30, family='Helvetica')
label_time['font'] = time_font
label_time.grid(row=1, pady=(5, 10), column=1, columnspan=3)

label_state = tk.Label(frame1, text="State: Recording", fg='white', bg='black')
state_font = font.Font(size=20, family='Helvetica')
label_state['font'] = state_font
label_state.grid(row=2, pady=(5, 10), column=1, columnspan=3)

# Load and resize icons
icon = Image.open('icons/cam.png').resize((150, 150), Image.LANCZOS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon, bg='black')
label_icon.grid(row=3, pady=(5, 10), column=1, columnspan=3)

alert_label = tk.Label(frame1, text="", fg='red', bg='black', font=("Helvetica", 16))
alert_label.grid(row=4, pady=(5, 10), column=1, columnspan=3)

def on_enter(e):
    label_icon['bg'] = 'gray'

def on_leave(e):
    label_icon['bg'] = 'black'

label_icon.bind("<Enter>", on_enter)
label_icon.bind("<Leave>", on_leave)
label_icon.bind("<Button-1>", lambda e: open_popup(window, btn2_image, btn3_image, btn4_image, btn5_image, btn6_image,
                                                   start_rect_noise, lambda: start_in_out(alert_label), lambda: start_record(alert_label), lambda: start_noise(alert_label)))

def load_button_image(image_path):
    img = Image.open(image_path).resize((50, 50), Image.LANCZOS)
    img = ImageOps.expand(img, border=(25, 25), fill='black')  
    img = ImageTk.PhotoImage(img)
    return img

btn2_image = load_button_image('icons/rectangle-of-cutted-line-geometrical-shape.png')
btn3_image = load_button_image('icons/web-camera.png')
btn4_image = load_button_image('icons/recording.png')
btn5_image = load_button_image('icons/exit.png')
btn6_image = load_button_image('icons/incognito.png')

# Pack the frame
frame1.pack(expand=True)

update_time()

# Start the tkinter main loop
window.mainloop()
