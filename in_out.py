import cv2
import os
from datetime import datetime

def in_out():
    cap = cv2.VideoCapture(0)

    right, left = "", ""
    x_threshold_right = 500
    x_threshold_left = 200
    mid_x = 300

    # Create directories if they don't exist
    if not os.path.exists('visitors/in'):
        os.makedirs('visitors/in')
    if not os.path.exists('visitors/out'):
        os.makedirs('visitors/out')

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        
        # Delay for the second frame to ensure motion detection
        cv2.waitKey(30)
        
        _, next_frame = cap.read()
        next_frame = cv2.flip(next_frame, 1)

        # Calculate absolute difference between frames
        diff = cv2.absdiff(next_frame, frame)
        diff = cv2.blur(diff, (5, 5))
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        _, threshd = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(threshd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            max_cnt = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(max_cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "MOTION", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
        else:
            x = mid_x  # Reset x to mid value if no contours are found

        if right == "" and left == "":
            if x > x_threshold_right:
                right = True
            elif x < x_threshold_left:
                left = True

        elif right:
            if x < x_threshold_left:
                print("to left")
                right, left = "", ""
                cv2.imwrite(f"visitors/in/{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.jpg", frame)

        elif left:
            if x > x_threshold_right:
                print("to right")
                right, left = "", ""
                cv2.imwrite(f"visitors/out/{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.jpg", frame)

        cv2.imshow("Frame", frame)

        # Exit loop on ESC key
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
