import cv2
import numpy as np
from ultralytics import YOLO

class PlateDetector:
    def __init__(self, model_path="yolov8n.pt", confidence=0.5):
        self.model = YOLO(model_path)
        self.confidence = confidence

    def detect(self, frame):
        results = self.model(frame, conf=self.confidence, verbose=False)
        plates = []
        for result in results:
            if result.boxes is None: continue
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                conf = float(box.conf[0])
                plates.append({"bbox": (x1, y1, x2, y2), "image": frame[y1:y2, x1:x2], "confidence": conf})
        return plates

    def detect_and_draw(self, frame):
        plates = self.detect(frame)
        annotated = frame.copy()
        for p in plates:
            x1, y1, x2, y2 = p["bbox"]
            cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)
        return annotated, plates
