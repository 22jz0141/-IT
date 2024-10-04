import cv2
src_img = cv2.imread("image\lena.jpg")
dst_img = cv2.rectangle( 
  img = src_img,
  pt1 = (100,100),
  pt2 = (150,170),
  color = (0,0,255),
  thickness = 3,
  lineType = 4 
)
cv2.imshow("lena_rect.jpg", dst_img)
cv2.waitKey(0)
cv2.destroyAllWindows()