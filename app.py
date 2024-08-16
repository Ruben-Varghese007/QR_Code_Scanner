import cv2
import numpy as np
import streamlit as st
from pyzbar.pyzbar import decode

def process_frame(frame):
    # Convert the frame to grayscale for better decoding
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    decoded_objects = decode(gray)

    myDataList = []
    with open('path to myDataFile.text') as f:
        myDataList = f.read().splitlines()

    myData = ""
    myOutput = "No QR Code detected"
    myColor = (0, 0, 0)  # Default color

    # Process each detected barcode (QR code)
    for barcode in decoded_objects:
        myData = barcode.data.decode('utf-8')

        # Check if the data is in the authorized list
        if myData in myDataList:
            myOutput = 'Authorized'
            myColor = (0, 255, 0)
        else:
            myOutput = 'Un-Authorized'
            myColor = (0, 0, 255)

        # Draw the polygon around the QR code
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, myColor, 5)

        # Display the authorization status near the QR code
        pts2 = barcode.rect
        cv2.putText(frame, myOutput, (pts2[0], pts2[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)

    return frame, myOutput

st.title('QR Code Scanner with Streamlit')

# Set up the video capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

# Placeholder for displaying the video frame and status
stframe = st.empty()
status_display = st.empty()

while True:
    ret, frame = cap.read()
    if not ret:
        st.write("Failed to grab frame.")
        break

    try:
        # Process the frame and get the authorization status
        frame, status = process_frame(frame)

        # Convert the frame to RGB format for Streamlit
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame_rgb, channels='RGB')

        # Continuously update the status display
        status_display.text(f"Status: {status}")

        # Wait a short period to give time for the camera to refresh
        cv2.waitKey(1)

    except AssertionError as e:
        st.write(f"AssertionError: {e}")
        st.write("Invalid QR Code")
    except Exception as e:
        st.write(f"Error: {e}")
        st.write("An unexpected error occurred")

cap.release()


