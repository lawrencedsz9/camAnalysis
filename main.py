import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk, ImageOps, ImageDraw
from threading import Thread
from in_out import in_out  # Assuming these are your OpenCV scripts
from motion import noise
from rect_noise import rect_noise
from record import record

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
    except Exception as e:
        print(f"Error starting recording: {e}")

# Function to start OpenCV capture for rectangle noise detection
def start_rect_noise():
    try:
        Thread(target=rect_noise).start()
    except Exception as e:
        print(f"Error starting rectangle noise detection: {e}")

# Function to create a circular button
def create_rounded_button(parent, text, image, command, fg_color, hover_color):
    def on_enter(e):
        btn['background'] = hover_color

    def on_leave(e):
        btn['background'] = fg_color

    btn = tk.Button(parent, text=text, image=image, compound='left', command=command, 
                    font=font.Font(size=15, weight='bold'), fg='white', bg=fg_color, 
                    relief='flat', bd=0, highlightthickness=0)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

# Function to create a rounded image
def make_rounded_image(image_path, size=(150, 150)):
    img = Image.open(image_path).resize(size, Image.LANCZOS)
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    img.putalpha(mask)
    return ImageTk.PhotoImage(img)

# Function to open a pop-up window with buttons
def open_popup():
    popup = tk.Toplevel(window)
    popup.title("Camera Controls")
    popup.geometry("400x300")
    popup.configure(bg='black')
    
    btn2 = create_rounded_button(popup, 'Spot', btn2_image, start_rect_noise, 'blue', 'darkblue')
    btn2.pack(pady=10)

    btn3 = create_rounded_button(popup, 'Security', btn3_image, start_in_out, 'red', 'darkred')
    btn3.pack(pady=10)

    btn4 = create_rounded_button(popup, 'Record', btn4_image, start_record, 'purple', 'darkpurple')
    btn4.pack(pady=10)

    btn6 = create_rounded_button(popup, 'Monitor', btn6_image, start_noise, 'orange', 'darkorange')
    btn6.pack(pady=10)

    btn5 = create_rounded_button(popup, 'Exit', btn5_image, popup.destroy, 'black', 'gray')
    btn5.pack(pady=10)

# Create the main window
window = tk.Tk()
window.title("CCTV - Spy Theme")
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
icon = make_rounded_image('icons/cam.png')
label_icon = tk.Label(frame1, image=icon, bg='black')
label_icon.grid(row=1, pady=(5, 10), column=2)
label_icon.bind("<Button-1>", lambda e: open_popup())  # Bind click event to open popup

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
