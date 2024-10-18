import cv2
import cvzone
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay = cv2.imread('native.png', cv2.IMREAD_UNCHANGED)
while True:
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for (x, y, w, h) in faces:
        overlay_resize = cv2.resize(overlay, (int(w*1.5), int(h*1.5)))
        x_offset = max(0, x - 45)
        y_offset = max(0, y - 75)
        if x_offset + overlay_resize.shape[1] > frame.shape[1]:
            overlay_resize = overlay_resize[:, :frame.shape[1] - x_offset]
        if y_offset + overlay_resize.shape[0] > frame.shape[0]:
            overlay_resize = overlay_resize[:frame.shape[0] - y_offset, :]
        frame = cvzone.overlayPNG(frame, overlay_resize, [x_offset, y_offset])
    cv2.imshow('Akkyaaa Wala Snap', frame)
    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()