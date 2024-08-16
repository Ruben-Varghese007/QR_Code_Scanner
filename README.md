# QR Code Scanner

This project is a real-time QR Code Scanner built using OpenCV, PyZbar, and Streamlit. 
The application reads QR codes through your webcam and checks if the decoded data matches any authorized entries in a predefined list. 
The application will continuously display the status of the scanned QR code as either "Authorized" or "Un-Authorized" based on the data.

## Run the OpenCV application:
>python QRCodeProject.py
### OR
> standard F5 or Run program

## Run the Streamlit application:
> streamlit run app.py

## Features
- Real-time QR Code Scanning: The application captures video feed from your webcam and scans QR codes in real-time.
- Data Authorization Check: The application compares the scanned QR code data with a list of authorized entries.
- Continuous Status Display: The status of the scanned QR code (Authorized/Un-Authorized) is displayed continuously as long as the QR code is in view.

## Requirements
- Python 3.6+
- Streamlit
- OpenCV
- Pyzbar
- NumPy
- Installation

## Install the required packages:

> pip install streamlit opencv-python-headless numpy pyzbar

### Prepare your authorized data file:

Create a text file named myDataFile.text in the project directory(already available). Add or Edit each authorized QR code data entry on a new line.
