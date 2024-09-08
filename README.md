# OpenCV-with-Flask

# Live Stream App

![sscv](https://github.com/user-attachments/assets/753a49d1-6978-4ba5-a590-afd8d1bd34bf)


<img width="1440" alt="Screenshot 2024-09-08 at 7 08 52 PM" src="https://github.com/user-attachments/assets/461bc869-180b-4427-a919-52acc700ab68">


## 🚀 Overview

The Live Stream App is a Flask-based web application that provides real-time video streaming from a webcam, allows capturing images, recording videos, and managing these media files through a gallery interface. The app uses OpenCV for handling video and image processing.

## 📸 Features

- **Real-Time Webcam Streaming**: Live feed from the webcam displayed on the webpage.
- **Image Capture**: Capture and save images as PNG files.
- **Video Recording**: Record videos and save them as MP4 files.
- **Gallery Management**: View, preview, and delete captured images and videos.
- **Responsive Layout**: A modern, responsive interface using Bootstrap.

## ⚙️ Installation

### Prerequisites

- Python 3.x
- Flask
- OpenCV
- Bootstrap (included via CDN)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/live-stream-app.git
   cd live-stream-app
   ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```
    pip install -r requirements.txt
    ```
4. **Run the Flask App**
    ```
    flask run
    ```
 - The app will be available at http://127.0.0.1:5000.


## 🎥 Usage

1. **Start the Camera**: Click the “Start Camera” button to begin streaming from the webcam.
2. **Stop the Camera**: Click the “Stop Camera” button to stop the webcam feed.
3. **Capture Image**: Click the “Capture Image” button to take a snapshot and save it as a PNG file.
4. **Start Recording**: Click the “Start Recording” button to begin recording a video.
5. **Stop Recording**: Click the “Stop Recording” button to stop the video recording and save it as an MP4 file.

## 📷 Gallery

- **View Images**: Captured images will appear in the gallery on the right side of the page.
- **View Videos**: Recorded videos are also displayed in the gallery and can be played directly.
- **Delete Media**: Use the “Delete” button next to images and videos to remove them from the gallery.

## 🖼️ Screenshots

### **Live Feed and Controls.**

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/d1f8fa10-3401-453d-a96d-52d5b948f741" alt="Image 1" style="width: 48%;"/>
  <img src="https://github.com/user-attachments/assets/054629db-d073-4e7f-9ae4-53fabceb0ee2" alt="Image 2" style="width: 48%;"/>
</div>



### **Gallery View.**

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/ef9c258e-ec3e-4344-90d8-b4391872963f" alt="Image 1" style="width: 48%;"/>
  <img src="https://github.com/user-attachments/assets/ba520049-097f-4c56-9755-22189386c647" alt="Image 2" style="width: 48%;"/>
</div>

## 🔧 Troubleshooting

- **Camera Feed Not Displaying**: Ensure your webcam is properly connected and accessible by other applications.
- **Videos Not Playing**: Make sure the video files are encoded correctly and try opening them with standard video players like VLC.
- **Leaked Resources Warning**: Check that the camera and video writer are being properly released in the code.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📫 Contact

For any questions or feedback, please contact [Siddharamayya M](https://github.com/mtptisid/).

Feel free to contribute to this project or suggest improvements by opening an issue or a pull request.
