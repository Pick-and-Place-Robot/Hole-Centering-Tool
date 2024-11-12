"""
Author: Pulindu Vidmal

Edited by : Jayamadu Gammune

This script implements a Hole Centering Tool using computer vision techniques.
It detects circular shapes (holes) from a webcam feed and provides visual feedback
to align these holes with a crosshair displayed on the screen.

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
"""

import cv2
import numpy as np

# Draw a crosshair at the center of the image
def draw_crosshair(image):
    height, width, _ = image.shape
    center = (width // 2, height // 2)
    cv2.line(image, (center[0] - 10, center[1]), (center[0] + 10, center[1]), (0, 0, 255), 2)
    cv2.line(image, (center[0], center[1] - 10), (center[0], center[1] + 10), (0, 0, 255), 2)
    return center

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blur the grayscale image
    gray_blurred = cv2.blur(gray, (3, 3))

    # Apply Hough transform on the blurred image
    detected_circles = cv2.HoughCircles(gray_blurred,
                                        cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                                        param2=30, minRadius=1, maxRadius=40)

    # Draw circles and calculate center coordinates
    if detected_circles is not None:
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]

            # Draw the circumference of the circle
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2)

            # Draw a small circle (of radius 1) to show the center
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)

            # Calculate the center of the display
            display_center = draw_crosshair(frame)

            # Calculate the distance between circle center and display center
            circle_center = (a, b)
            distance_x = circle_center[0] - display_center[0]
            distance_y = circle_center[1] - display_center[1]

            # Draw a line from circle center to display center
            cv2.line(frame, circle_center, display_center, (255, 0, 0), 2)

            # Print the distance from circle center to display center on the display
            cv2.putText(frame, f'Distance X: {distance_x:.2f}, Distance Y: {distance_y:.2f}',
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Check for key press and break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
