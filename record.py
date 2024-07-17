# record.py

import cv2
from datetime import datetime
import os

def record():
    cap = cv2.VideoCapture(0)  # Initialize video capture from the first camera

    # Define codec and output video file
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_path = 'C:/Users/lawrence/Desktop/pythooon/visitors/recordings/'
    output_file = f'{output_path}{datetime.now().strftime("%H-%M-%S")}.avi'
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cv2.putText(frame, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50, 50), cv2.FONT_HERSHEY_COMPLEX,
                    0.6, (255, 255, 255), 2)

        out.write(frame)  # Write the frame to the output file

        cv2.imshow("Recording", frame)  # Display the frame

        # Check for 'f' key press to stop recording
        if cv2.waitKey(1) & 0xFF == ord('f'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
