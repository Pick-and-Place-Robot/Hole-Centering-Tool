"""
Author: Pulindu Vidmal
Edited by: Jayamadu Gammune

This script implements a Hole Centering Tool using computer vision techniques.
It detects circular shapes (holes) from a webcam feed or a selected video file 
and provides visual feedback to align these holes with a crosshair displayed on 
the screen.

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:
...
"""

import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

# Draw a crosshair at the center of the image
def draw_crosshair(image):
    height, width, _ = image.shape
    center = (width // 2, height // 2)
    cv2.line(image, (center[0] - 10, center[1]), (center[0] + 10, center[1]), (0, 0, 255), 2)
    cv2.line(image, (center[0], center[1] - 10), (center[0], center[1] + 10), (0, 0, 255), 2)
    return center

# Initialize the GUI for video source selection
def select_video_source():
    global cap
    source_type = source_var.get()
    
    if source_type == "Webcam":
        cap = cv2.VideoCapture(0)  # Default webcam
    else:
        file_path = filedialog.askopenfilename(title="Select Video File",
                                               filetypes=(("Video Files", "*.mp4;*.avi;*.mov"), ("All Files", "*.*")))
        if file_path:
            cap = cv2.VideoCapture(file_path)
        else:
            messagebox.showerror("File Error", "No file selected. Please select a video file or use the webcam.")
            return
    
    # Start video processing
    process_video()

# Process video for hole detection and alignment feedback
def process_video():
    global cap
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Blur the grayscale image
        gray_blurred = cv2.blur(gray, (3, 3))

        # Apply Hough transform to detect circles
        detected_circles = cv2.HoughCircles(gray_blurred,
                                            cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                                            param2=30, minRadius=1, maxRadius=40)

        # Draw detected circles and alignment information
        if detected_circles is not None:
            detected_circles = np.uint16(np.around(detected_circles))

            for pt in detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]

                # Draw the circle
                cv2.circle(frame, (a, b), r, (0, 255, 0), 2)
                cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)

                # Calculate and display distances
                display_center = draw_crosshair(frame)
                distance_x = a - display_center[0]
                distance_y = b - display_center[1]
                cv2.line(frame, (a, b), display_center, (255, 0, 0), 2)
                cv2.putText(frame, f'Distance X: {distance_x:.2f}, Distance Y: {distance_y:.2f}',
                            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Show the frame
        cv2.imshow('Hole Centering Tool', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

# Setup Tkinter GUI
root = tk.Tk()
root.title("Hole Centering Tool - Select Video Source")
root.geometry("300x200")

source_var = tk.StringVar(value="Webcam")

# Create radio buttons for video source selection
webcam_radio = tk.Radiobutton(root, text="Webcam", variable=source_var, value="Webcam")
file_radio = tk.Radiobutton(root, text="Video File", variable=source_var, value="Video File")
start_button = tk.Button(root, text="Start", command=select_video_source)

webcam_radio.pack(pady=10)
file_radio.pack(pady=10)
start_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
