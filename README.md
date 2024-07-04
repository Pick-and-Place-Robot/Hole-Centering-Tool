# Hole Centering Tool 🎯

Hole Centering Tool is a real-time vision-based application designed to assist in precisely aligning circular holes with a crosshair on a screen. This tool utilizes computer vision techniques to detect circular shapes (holes) using a webcam and provides visual feedback to adjust the device so that the hole is centered on the crosshair.

## Features 🔧

- **Real-time Hole Detection:** Detect circular shapes (holes) using a webcam in real-time.
- **Visual Feedback:** Display a crosshair on the screen and provide visual cues to align the detected hole with the crosshair.
- **Displacement Calculation:** Calculate the displacement of the hole from the center and provide directional feedback for adjustment.
- **Angle Calculation:** Compute the angle of rotation required to center the hole on the crosshair.
- **Analog Output:** Map the angle of rotation to an analog value for further processing.

## How It Works 🛠️

The tool captures video from a connected webcam, converts each frame to grayscale, and applies a blur filter to reduce noise. It then applies the Hough Circle Transform to detect circular shapes in the image. Once a circle (hole) is detected, it calculates the distance from the circle's center to the center of the display. Based on this displacement, it provides feedback on how to adjust the device to center the hole on the crosshair.

## Setup and Usage 🚀

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/Hole-Centering-Tool.git
   cd Hole-Centering-Tool
   ```
2. **Install Dependencies:** Ensure you have Python installed along with the necessary libraries:
   ```bash
    pip install -r requirements.txt
   ```
3. **Run the Application:** Execute the hole_aligner.py script to start the application:
      ```bash
        python hole_aligner.py
      ```
4. **Adjustment Process:**

- Place the device such that the circular hole is visible to the webcam.
- Follow the visual feedback provided by the tool to adjust the device position.
- Aim to center the detected hole with the crosshair displayed on the screen.
  
5.**Exit the Application:**
   ```bash
      Press q on your keyboard to close the application and release the webcam.
   ```


## Dependencies 📦
- OpenCV
- NumPy

## Contributing 🤝
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License 📄
This project is open-source and available under the MIT License. See the LICENSE file for more details.
