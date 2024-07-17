import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk, ImageOps
from threading import Thread

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

# Function to open a pop-up window with buttons on the left
def open_popup(window, btn2_image, btn3_image, btn4_image, btn5_image, btn6_image,
               start_rect_noise, start_in_out, start_record, start_noise):
    popup = tk.Toplevel(window)
    popup.title("Camera Controls")
    popup.geometry("400x300")
    popup.configure(bg='black')

    canvas = tk.Canvas(popup, bg='black')
    scrollbar = tk.Scrollbar(popup, orient='vertical', command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg='black')

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    btn2 = create_rounded_button(scrollable_frame, 'Spot', btn2_image, start_rect_noise, 'blue', 'darkblue')
    btn2.pack(pady=10)

    btn3 = create_rounded_button(scrollable_frame, 'Security', btn3_image, start_in_out, 'red', 'darkred')
    btn3.pack(pady=10)

    btn4 = create_rounded_button(scrollable_frame, 'Record', btn4_image, start_record, 'purple', 'darkpurple')
    btn4.pack(pady=10)

    btn6 = create_rounded_button(scrollable_frame, 'Monitor', btn6_image, start_noise, 'orange', 'darkorange')
    btn6.pack(pady=10)

    btn5 = create_rounded_button(scrollable_frame, 'Exit', btn5_image, popup.destroy, 'black', 'gray')
    btn5.pack(pady=10)

    canvas.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')
