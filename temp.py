import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

# Load the pre-trained face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize variables
frame_count = 0
avg_area = 0
direction = "Unknown"

# Function to detect and draw rectangles around faces
def detect_faces(frame):
    global frame_count, avg_area, direction

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw rectangle around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Calculate rectangle area
        area = w * h

        # Update average area
        avg_area = (avg_area * frame_count + area) / (frame_count + 1)

        # If rectangle area is more than 100*100 pixels
        if area > 100 * 100:
            frame_count += 1
            # If 40 frames passed, update direction and reset frame count and average area
            if frame_count == 40:
                if avg_area > 100 * 100:
                    direction = "Left" if x < frame.shape[1] // 2 else "Right"
                else:
                    direction = "Not finding humans"
                frame_count = 0
                avg_area = 0
                st.write(f"Robot is ready to move {direction}")

    # Display the frame
    return frame

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        return detect_faces(frame)

def main():
    st.title("Face Detection with Streamlit and OpenCV")

    webrtc_ctx = webrtc_streamer(key="face-detection", 
                                 video_transformer_factory=VideoTransformer)

if __name__ == "__main__":
    main()
