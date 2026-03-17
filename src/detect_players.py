from ultralytics import YOLO
import cv2
import os
from google.colab.patches import cv2_imshow
from google.colab import files
from src.utils import extract_torso, detect_blue_ratio
from src.config import SCORE_THRESHOLD

uploaded = files.upload()
image_path = list(uploaded.keys())[0]
img = cv2.imread(image_path)

model = YOLO("models/yolov8n.pt")
results = model(img)

blue_count = 0
white_count = 0

for box in results[0].boxes:
    cls = int(box.cls)
    label = model.names[cls]
    score = float(box.conf)
    if score < SCORE_THRESHOLD:
        continue
        
    if label == "person":
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        player = img[y1:y2, x1:x2]
        if player.size == 0:
            continue
        torso = extract_torso(player)
        ratio = detect_blue_ratio(torso)
        
        if ratio > 0.1:
            team = "Blue"
            color = (255,0,0)
            blue_count += 1
        else:
            team = "White"
            color = (255,255,255)
            white_count += 1
        text = f"{team} | {score:.2f}"
        cv2.rectangle(img,(x1,y1),(x2,y2),color,2)
        (w_text,h_text),_ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX,0.6,2)
        cv2.rectangle(img,(x1,y1-h_text-10),(x1+w_text,y1),color,-1)
        cv2.putText(img,text,(x1,y1-5),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2)


