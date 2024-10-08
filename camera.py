import cv2
import time

# カメラを開く
cap = cv2.VideoCapture(0)

indexNo = 0
while True:
    # 画像をキャプチャする
    ret, frame = cap.read()
    
    # 画像を表示する
    cv2.imwrite(f"cameraPhoto\image{indexNo:05d}.jpg", frame)
    print(f"image{indexNo:05d}.jpg")
    indexNo = indexNo + 1
    time.sleep(0.5)

    dst_img = cv2.rectangle( img = frame,
    pt1 = (200,100),
    pt2 = (450,350),
    color = (0,255,0),
    thickness = 3,
    lineType = 4 )
    cv2.imshow("Image", frame)



    # `q`キーを押すとループを終了する
    if cv2.waitKey(1) == ord('q'):
        break
    # elif cv2.waitKey(1) == ord('c'):
# カメラを閉じる
cap.release()
# すべてのウィンドウを閉じる
cv2.destroyAllWindows()