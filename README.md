
# AI Virtual Mouse Project 🖱️

This project implements an AI-powered virtual mouse using Python, OpenCV, Mediapipe, and Autopy. The application tracks your hand gestures via a webcam and allows you to control the mouse cursor and perform click actions without touching a physical mouse.

---

## Changelog 🚀
### v2.0
- **Added Right-Click**: Right-click functionality with the pinky finger was added.
- **Multiple Click Issue Fixed**: The issue of continuous clicking was fixed, ensuring only one click occurs when intended.
- **Added Scroll Functionality**: Scrolling added. Scroll down when the thumb is open and far from the index finger, and scroll up when the thumb is open and close to the index finger.
- **Code Optimization**: Various optimizations were made to improve the efficiency and performance of the program.

---

## Features ✨
- **Hand Tracking**: Uses Mediapipe to detect and track hands in real-time.
- **Mouse Movement**: Move the mouse cursor by moving your index finger.
- **Click Actions**: Simulate mouse clicks using hand gestures.
- **Smooth Movement**: Ensures a fluid cursor movement with smoothing algorithms.
- **Frame Reduction**: Restricts hand movement to a specific region for better accuracy.

---

## Prerequisites 🛠️
- **Python 3.8** (Tested and Working)
- **Python 3.12** (Not working due to compatibility issues with Autopy)

### Required Libraries:
Install the following Python modules before running the project:
- `opencv-python`
- `mediapipe`
- `autopy`
- `numpy`
- `pyautogui`
- `cv2`

You can install them using pip:
```bash
pip install opencv-python mediapipe autopy numpy pyautogui cv2
```

---

## Files in the Project 📂
1. **`AIVirtualMouseProject.py`**: Main script that handles hand detection and mouse control.
2. **`HandTrackingModule.py`**: Custom module for hand tracking and gesture recognition.
3. **`README.md`**: Documentation for the project.

---

## How It Works ⚙️
1. **Hand Detection**:
   - Detects and tracks hand landmarks using Mediapipe.
   - Identifies specific points like fingertips and the base of the hand.
   
2. **Mouse Control**:
   - The tip of the index finger controls the cursor position.
   - Clicking is simulated by pinching the index and middle fingers together.

3. **Smoothing**:
   - Reduces jerky movements for smoother cursor control.

4. **Click Detection**:
   - If the distance between the index and middle fingertips is less than a threshold, a mouse click is triggered.

5. **Scroll Detection**:
   - Thumb open and far from index finger: Scroll down.
   - Thumb open and close to index finger: Scroll up.

---

## Usage 🚀
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/AI-Virtual-Mouse.git
   cd AI-Virtual-Mouse
   ```

2. Run the main script:
   ```bash
   python AIVirtualMouseProject.py
   ```

3. Ensure your webcam is functional. A live feed will appear, and the program will start detecting your hand gestures.

4. Use the following gestures:
   - **Index Finger Up**: Move the cursor.
   - **Index and Middle Fingers Up**: Simulate a mouse click by bringing the fingers close together.
   - **Thumb Open and Far from Index Finger**: Scroll down.
   - **Thumb Open and Close to Index Finger**: Scroll up.

---

## Code Overview 🖥️

### Main Script: `AIVirtualMouseProject.py`
- **Imports and Initialization**:
   - Initializes camera and screen dimensions.
   - Loads the `HandTrackingModule`.

- **Main Loop**:
   - Captures webcam feed.
   - Detects hand landmarks and gestures.
   - Translates hand movements to mouse movements.
   - Handles click actions based on finger gestures.

### Hand Tracking Module: `HandTrackingModule.py`
- Contains reusable functions:
   - `findHands()`: Detect hands in a frame.
   - `findPosition()`: Get the positions of key landmarks.
   - `fingersUp()`: Determine which fingers are up.
   - `findDistance()`: Calculate the distance between two points.

---

## Screenshots 📸
![Project Screenshot](images/image.png)
![Project Screenshot](images/image1.png)

---

## Future Enhancements 🚀
- Add support for right-click and drag gestures.
- Include gesture-based scrolling functionality.
- Enhance performance for low-light conditions.

---

## Acknowledgments 💡
- **Mediapipe**: For providing robust hand tracking models.
- **Autopy**: For mouse control functionalities.
- **OpenCV**: For video capture and processing.

---

## License 📝
This project is open source and available under the MIT License.

---
