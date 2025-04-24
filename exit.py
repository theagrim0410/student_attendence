import cv2
import axcess
import saving
import main

def setup_camera(width, height):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Failed to access camera.")
    cap.set(3, width)
    cap.set(4, height)
    return cap

def draw_roi(frame, box_x1, box_y1, box_x2, box_y2):
  
    cv2.rectangle(frame, (box_x1, box_y1), (box_x2, box_y2), (255, 0, 0), 2)

def process_qr_code(frame, detector, box_x1, box_y1, box_x2, box_y2):
    roi = frame[box_y1:box_y2, box_x1:box_x2]
    data, bbox, _ = detector.detectAndDecode(roi)
    return data

def handle_qr_data(data):
    ans = axcess.show(data)
    if ans == -1:
        # print(f"QR code data '{data}' not found in database.")
        main.speak(f"QR code data {data} not found in database")
        saving.store_wrong(data, "Exit", "Student not found in database")
    else:
        saving.store_attendence_out(ans[3], ans[0], ans[1], ans[2])
        # print(f"Attendance recorded for exit: {ans}")
        main.speak(f"Attendance recorded for exit {ans[1]}")
        return True  
    return False

def main2():
    
    frame_width = 640
    frame_height = 480
    box_w, box_h = 250, 250
    box_x1 = (frame_width - box_w) // 2
    box_y1 = (frame_height - box_h) // 2
    box_x2 = box_x1 + box_w
    box_y2 = box_y1 + box_h

    try:
        cap = setup_camera(frame_width, frame_height)
        detector = cv2.QRCodeDetector()

        while True:
            ret, frame = cap.read()
            if not ret:
                # print("Failed to capture frame.")
                main.speak("Failed to captute frame.")
                break

            draw_roi(frame, box_x1, box_y1, box_x2, box_y2)
            data = process_qr_code(frame, detector, box_x1, box_y1, box_x2, box_y2)
            cv2.putText(frame, 'Scan Your ID Card', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
            1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, 'Press q if wana exit', (80, 80), cv2.FONT_HERSHEY_SIMPLEX, 
            1, (0, 255, 0), 2, cv2.LINE_AA)

            if data:  
                if handle_qr_data(data):
                    break 
            cv2.imshow("QR Code Scanner", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        # print(f"An error occurred: {e}")
        main.speak(f"An error occured {e}")

    finally:
  
        cap.release()
        cv2.destroyAllWindows()

    if not data:
        # print("No QR Code detected during the session.")
        main.speak("No QR Code detected during the session.")

if __name__ == "__main__":
    main2()
