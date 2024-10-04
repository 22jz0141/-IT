import cv2
from enum import Enum

# フレームカラーを指定するEnumクラス
class MyFramePutText(Enum):
    MOVIE = 1
    NO_MOVIE = 0

def main():
  frame_movie = MyFramePutText.NO_MOVIE  # 初期設定はカラー
  capture = cv2.VideoCapture(0)

  while True:
    ret, frame = capture.read()

    if frame_movie == MyFramePutText.MOVIE:
        # フレームをグレースケールに変換
        cv2.putText(frame, "test!", (90, 180), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255,255,255))

    cv2.imshow('in camera', frame)

    # キー入力処理
    key = cv2.waitKey(1) & 0xFF

    # 'q'キーで終了
    if key == ord('q'):
        break
    
    # 'g'キーでグレースケールモードに切り替え
    if key == ord('t'):
      frame_movie = MyFramePutText.MOVIE

  # リソースを解放して終了
  capture.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
