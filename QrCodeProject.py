import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread('qrcode.png')
#code = decode(img)
#print(code)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('path to myDataFile.text') as f:
    myDataList = f.read().splitlines()
print("Authorized : ",myDataList)

prev = ""
myData = ""

while True:
    success, img = cap.read()
    try:
        for barcode in decode(img):
            #print(barcode.data)
            myData = barcode.data.decode('utf-8')
            if prev == myData:
                pass
            else:
                print()
                print("Data:",myData)
                prev = myData

                if myData in myDataList:
                    print("Authorized")
                    myOutput = 'Authorized'
                    myColor = (0,255,0)
                else:
                    print("Un-Authorized")
                    myOutput = 'Un-Authorized'
                    myColor = (0,0,255)

            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,myColor,5)
            pts2 = barcode.rect
            cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,myColor,2)

        cv2.imshow('Result',img)
        cv2.waitKey(1)

    except AssertionError as e:
        print(f"AssertionError: {e}")
        print("Invalid QR Code")
    except Exception as e:
        print(f"Error: {e}")
        print("An unexpected error occurred")

    