import cv2
from pyzbar.pyzbar import decode

def scan_barcode():
    # Initialize the camera
    camera = cv2.VideoCapture(0)

    while True:
        # Capture a frame from the camera
        ret, frame = camera.read()

        # Decode barcodes in the frame
        barcodes = decode(frame)

        # Draw rectangles around detected barcodes
        for barcode in barcodes:
            # Extract barcode data and type
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type

            # Draw a rectangle around the barcode
            points = barcode.polygon
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                cv2.polylines(frame, [hull], True, (255, 0, 0), 3)

            # Put the barcode data and type on the image
            text = f"{barcode_type}: {barcode_data}"
            cv2.putText(frame, text, (barcode.rect.left, barcode.rect.top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Show the frame with barcode information
        cv2.imshow('Barcode Scanner', frame)

        # Exit the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_barcode()
