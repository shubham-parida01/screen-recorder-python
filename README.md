# screen-recorder-python
## README.md

**Project Name:** Screen Recorder

**Description:**

This Python script captures a screen recording of your desktop and saves it as `ScreenRecording.avi`. It uses OpenCV (cv2) for video writing and image manipulation, and pyautogui for capturing screenshots.

**Features:**

- Records your entire screen.
- Saves the recording in AVI format.
- Provides a live preview of the recording window.
- Allows you to stop recording by pressing the 'q' key.

**Installation:**

1. Make sure you have Python installed on your system. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Open a terminal window and run the following command to install the required libraries:

   ```bash
   pip install opencv-python pyautogui
   ```

**Usage:**

1. Save the script as `screen_recorder.py`.
2. Run the script from your terminal using the command:

   ```bash
   python screen_recorder.py
   ```

3. A window titled "Live Recording" will appear, displaying a preview of your screen.
4. To start recording, the script is already running.
5. To stop recording, press the 'q' key on your keyboard.

**Output:**

The recorded screen will be saved as `ScreenRecording.avi` in the same directory as the script.

**Technical Details:**

- The script uses `pyautogui.screenshot()` to capture the entire screen in BGR format.
- It converts the BGR image to RGB format using `cv2.cvtColor()` for compatibility with OpenCV's video writing functionality.
- The video is written to an AVI file using `cv2.VideoWriter()`.
- The live preview window is resized for better viewing experience using `cv2.resizeWindow()`.

**License:**

This code is provided under the MIT License. You are free to use, modify, and distribute it as long as you retain the copyright notice.

**Additional Notes:**

- Depending on your system resources and screen resolution, the recording quality and frame rate might vary.
- You can modify the resolution and codec settings in the script to adjust the video quality and file size.
- Consider adding error handling for potential issues during recording.

**Social Info**
This code has also been shared on the following socials:
- [Twitter][https://x.com/shub_game0/status/1773661858236334382?s=20]
