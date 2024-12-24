import xml.etree.ElementTree as ET

# Pascal VOC のクラス名を YOLO のクラス番号に変換する辞書
class_dict = {'kuma': 0, 'inu': 1}  # 'kuma' = クラス0, 'inu' = クラス1

# Pascal VOC XML ファイルを YOLO 形式に変換する関数
def voc_to_yolo(voc_xml, image_width, image_height):
    # XML をパース
    tree = ET.parse(voc_xml)
    root = tree.getroot()
    
    yolo_annotations = []

    # 各オブジェクト（物体）を処理
    for obj in root.findall('object'):
        # クラス名を取得
        class_name = obj.find('name').text
        class_id = class_dict.get(class_name, None)
        if class_id is None:
            continue  # クラスが辞書にない場合はスキップ
        
        # バウンディングボックス情報を取得
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        
        # バウンディングボックスの中心座標と幅・高さを計算
        x_center = (xmin + xmax) / 2.0 / image_width
        y_center = (ymin + ymax) / 2.0 / image_height
        width = (xmax - xmin) / float(image_width)
        height = (ymax - ymin) / float(image_height)
        
        # YOLO 形式で保存
        yolo_annotations.append(f"{class_id} {x_center} {y_center} {width} {height}")
    
    return yolo_annotations

# Pascal VOC 形式のファイルと画像サイズの指定
voc_xml_path = 'waku.xml'  # 変換対象の Pascal VOC XML ファイル
image_width = 593  # 画像の幅（px）
image_height = 502  # 画像の高さ（px）

# 変換して YOLO 形式のテキストファイルに保存
yolo_annotations = voc_to_yolo(voc_xml_path, image_width, image_height)

# YOLO 形式のアノテーションファイルを作成
yolo_txt_path = voc_xml_path.replace('.xml', '.txt')
with open(yolo_txt_path, 'w') as f:
    for annotation in yolo_annotations:
        f.write(annotation + '\n')

print(f"Converted {voc_xml_path} to {yolo_txt_path}")
