import cv2
import time

# カメラを開く
cap = cv2.VideoCapture(0)

indexNo = 0
while True:
    # 画像をキャプチャする
    ret, frame = cap.read()
    timeNow = int(time.time())
    # 画像を表示する
    cv2.imwrite(f"cameraPhoto\\frame_{timeNow}.jpg", frame)
    print(f"image{indexNo:05d}.jpg")
    indexNo = indexNo + 1
    time.sleep(0.3)

    pt1_1 = 200
    pt1_2 = 100
    pt2_1 = 450
    pt2_2 = 350

    dst_img = cv2.rectangle( img = frame,
    pt1 = (pt1_1,pt1_2),
    pt2 = (pt2_1,pt2_2),
    color = (0,255,0),
    thickness = 3,
    lineType = 4 )
    cv2.imshow("Image", frame)
    # save_yolo_annotation(pt1_1, pt1_2, pt2_1, pt2_2)
    # f = open(f"cameraPhoto\\frame_{timeNow}.txt", "w")
    # f.write(f"0 {pt1_1} {pt1_2} {pt2_1} {pt2_2}")
    # f.close()
    
    # def save_yolo_annotation(x, y, w, h, image_width, image_height, annotation_path):
    #     x_center = (x + w / 2) / image_width
    #     y_center = (y + h / 2) / image_height
    #     width = w / image_width
    #     height = h / image_height

    #     annotation = f"0 {x_center} {y_center} {width} {height}\n"
    #     with open(annotation_path, 'w') as f:
    #         f.write(annotation)

    # `q`キーを押すとループを終了する
    if cv2.waitKey(1) == ord('q'):
        break
    # elif cv2.waitKey(1) == ord('c'):
# カメラを閉じる
cap.release()
# すべてのウィンドウを閉じる
cv2.destroyAllWindows()