import cv2
import numpy as np

# Video parameters
width, height = 1280, 720  # High resolution
fps = 30
duration = 10  # Duration in seconds
num_frames = fps * duration

# Circle parameters
radius = 30
speed = 15  # Speed of movement

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('random_moving_hole.mp4', fourcc, fps, (width, height))

# Initial position of the circle
x, y = np.random.randint(radius, width-radius), np.random.randint(radius, height-radius)
dx, dy = speed, speed

# Generate frames
for _ in range(num_frames):
    # Dark background
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Draw the moving circle
    cv2.circle(frame, (x, y), radius, (255, 255, 255), -1)

    # Update position
    x += dx
    y += dy

    # Bounce off the edges
    if x <= radius or x >= width - radius:
        dx = -dx
    if y <= radius or y >= height - radius:
        dy = -dy

    # Write frame to video
    out.write(frame)

# Release resources
out.release()
print("Sample video 'random_moving_hole.mp4' created.")
