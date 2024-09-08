from flask import Flask, render_template, Response, request, redirect, url_for
import cv2
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
camera = None
video_writer = None
recording = False

UPLOAD_FOLDER_IMAGES = 'static/images'
UPLOAD_FOLDER_VIDEOS = 'static/videos'
app.config['UPLOAD_FOLDER_IMAGES'] = UPLOAD_FOLDER_IMAGES
app.config['UPLOAD_FOLDER_VIDEOS'] = UPLOAD_FOLDER_VIDEOS

def get_camera():
    global camera
    if camera is None or not camera.isOpened():
        camera = cv2.VideoCapture(0)
    return camera

def release_camera():
    global camera
    if camera is not None and camera.isOpened():
        camera.release()
        camera = None

def generate_frames():
    camera = get_camera()
    while camera.isOpened():
        success, frame = camera.read()
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    release_camera()

@app.route('/')
def index():
    images = [f for f in os.listdir(app.config['UPLOAD_FOLDER_IMAGES']) if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER_IMAGES'], f))]
    videos = [f for f in os.listdir(app.config['UPLOAD_FOLDER_VIDEOS']) if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER_VIDEOS'], f))]
    return render_template('index.html', images=images, videos=videos)

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_camera', methods=['POST'])
def start_camera():
    global camera
    camera = get_camera()
    return redirect(url_for('index'))

@app.route('/stop_camera', methods=['POST'])
def stop_camera():
    release_camera()
    return redirect(url_for('index'))

@app.route('/capture', methods=['POST'])
def capture():
    camera = get_camera()
    success, frame = camera.read()
    if success:
        filename = secure_filename('image.png')
        filepath = os.path.join(app.config['UPLOAD_FOLDER_IMAGES'], filename)
        cv2.imwrite(filepath, frame)
    release_camera()
    return redirect(url_for('index'))

@app.route('/start_recording', methods=['POST'])
def start_recording():
    global recording, video_writer
    if not recording:
        camera = get_camera()
        filename = secure_filename('video.mp4')
        filepath = os.path.join(app.config['UPLOAD_FOLDER_VIDEOS'], filename)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for MP4 format
        video_writer = cv2.VideoWriter(filepath, fourcc, 20.0, (int(camera.get(3)), int(camera.get(4))))
        recording = True
    return redirect(url_for('index'))

@app.route('/stop_recording', methods=['POST'])
def stop_recording():
    global recording, video_writer
    if recording:
        video_writer.release()
        recording = False
    return redirect(url_for('index'))

@app.route('/delete_image/<filename>', methods=['POST'])
def delete_image(filename):
    os.remove(os.path.join(app.config['UPLOAD_FOLDER_IMAGES'], filename))
    return redirect(url_for('index'))

@app.route('/delete_video/<filename>', methods=['POST'])
def delete_video(filename):
    os.remove(os.path.join(app.config['UPLOAD_FOLDER_VIDEOS'], filename))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)