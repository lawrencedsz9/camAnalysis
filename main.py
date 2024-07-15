import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
import cv2
from threading import Thread  # Import Thread from threading module
from datetime import datetime

# Import your OpenCV scripts
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record

# Function to start OpenCV capture for in_out functionality
def start_in_out():
    in_out()

# Function to start OpenCV capture for noise detection
def start_noise():
    noise()

# Function to start OpenCV capture for recording video
def start_record():
    record()

# Function to start OpenCV capture for rectangle noise detection
def start_rect_noise():
    rect_noise()

# Create the main window
window = tk.Tk()
window.title("cctv")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('1080x760')

# Create a frame to hold the widgets
frame1 = tk.Frame(window)

# Title label
label_title = tk.Label(frame1, text="Camera Analysis")
label_font = font.Font(size=35, weight='bold', family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10, 10), column=2)

# Load and resize icons
icon = Image.open('icons/cam.jpg')
icon = icon.resize((150, 150), Image.LANCZOS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5, 10), column=2)

# Load button icons and resize
btn2_image = Image.open('icons/rectangle-of-cutted-line-geometrical-shape.png').resize((50, 50), Image.LANCZOS)
btn2_image = ImageTk.PhotoImage(btn2_image)
btn3_image = Image.open('icons/web-camera.png').resize((50, 50), Image.LANCZOS)
btn3_image = ImageTk.PhotoImage(btn3_image)
btn4_image = Image.open('icons/recording.png').resize((50, 50), Image.LANCZOS)
btn4_image = ImageTk.PhotoImage(btn4_image)
btn5_image = Image.open('icons/exit.png').resize((50, 50), Image.LANCZOS)
btn5_image = ImageTk.PhotoImage(btn5_image)
btn6_image = Image.open('icons/incognito.png').resize((50, 50), Image.LANCZOS)
btn6_image = ImageTk.PhotoImage(btn6_image)

# Button styles
btn_font = font.Font(size=25)

# Buttons
btn2 = tk.Button(frame1, text='Noise', height=90, width=180, fg='blue', image=btn2_image, compound='left', command=start_rect_noise)
btn2['font'] = btn_font
btn2.grid(row=2, column=1, padx=10)

btn3 = tk.Button(frame1, text='Security', height=90, width=180, fg='red', image=btn3_image, compound='left', command=start_in_out)
btn3['font'] = btn_font
btn3.grid(row=2, column=2, padx=10)

btn4 = tk.Button(frame1, text='Record', height=90, width=180, fg='purple', image=btn4_image, compound='left', command=start_record)
btn4['font'] = btn_font
btn4.grid(row=2, column=3, padx=10)

btn5 = tk.Button(frame1, text='Exit', height=90, width=180, fg='black', image=btn5_image, compound='left', command=window.quit)
btn5['font'] = btn_font
btn5.grid(row=3, column=1, padx=10)

btn6 = tk.Button(frame1, text='Incognito', height=90, width=180, fg='orange', image=btn6_image, compound='left', command=start_noise)
btn6['font'] = btn_font
btn6.grid(row=3, column=2, padx=10)

frame1.pack()

# Start the tkinter main loop
window.mainloop()
