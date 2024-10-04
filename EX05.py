import cv2
# 縦300, 横100, 3チャンネル画像バッファを作る
img = cv2.imread("image\lena.jpg")
# x: 20, y: 50の位置に"ABCxyz"という文字列を描画
cv2.putText(img, "Hello", (90, 180), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255,255,255))
# 座標が分かるよう線を引く
# cv2.line(img, (20,50), (300,50), (0,0,255))
cv2.imwrite("proposeImg\lena_str.jpg", img)
cv2.imshow("lena_str.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()