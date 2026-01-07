# Cam-Sys 

Cam-Sys is a **Python-based camera analysis and security system** built using **OpenCV** and **Tkinter**.  
It provides a desktop interface to monitor camera activity, detect motion, track entry/exit direction, and record video with timestamps.

This project was developed as a hands-on exploration of **computer vision** and **real-time video processing**.

---

## Features 

- Live camera feed using OpenCV
- Motion detection (full-frame & region-based)
- In / Out detection based on movement direction
- Automatic image capture for entry and exit events
- Video recording with timestamp overlay
- SQLite database for logs and records
- Interactive Tkinter-based UI with icons and popups

---

## Working:

- Captures frames from a webcam
- Uses frame differencing to detect motion
- Tracks bounding box movement across frames
- Determines **IN / OUT** direction based on motion flow
- Allows region selection for focused monitoring
- Saves images and videos locally
- Logs timestamps and metadata in a SQLite database

---


## Project Structure 📂

```text
Cam-Sys/
│
├── main.py                     # Main Tkinter UI and controller
├── in_out.py                   # Entry / Exit detection logic
├── motion.py                   # Full-frame motion detection
├── rect_noise.py               # Region-based motion detection
├── record.py                   # Video recording module
├── scroll.py                   # UI helpers and popup controls
├── setup_database.py           # SQLite database setup & indexing
├── setup_database.db           # Local database file
│
├── visitors/
│   ├── in/                     # Captured entry images
│   ├── out/                    # Captured exit images
│   └── recordings/             # Recorded video files
│
├── icons/                      # UI icons
├── haarcascade_frontalface_default.xml
├── mn.png                      # Application icon
└── README.md

## Requirements 

- Python 3.8+
- OpenCV
- Pillow

Install dependencies:

```bash
pip install opencv-python pillow

```
#Run the application
```
python main.py
```
#UI Control will have:
-Spot → Select a region and monitor motion
-Security → Track entry and exit movement
-Record → Start video recording
-Monitor → Continuous motion detection
-Exit → Close the control popup
