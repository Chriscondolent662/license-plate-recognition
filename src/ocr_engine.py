import re, cv2
import numpy as np
import easyocr

PLATE_PATTERNS = {
    "TR": r"^[0-9]{2}\s?[A-Z]{1,3}\s?[0-9]{2,4}$",
    "EU": r"^[A-Z]{1,3}[-\s]?[A-Z]{1,2}[-\s]?[0-9]{1,4}$",
}

class OCREngine:
    def __init__(self, languages=None):
        self.reader = easyocr.Reader(languages or ["en"])

    def preprocess_plate(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (300, 100))
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return thresh

    def read_plate(self, plate_img):
        processed = self.preprocess_plate(plate_img)
        results = self.reader.readtext(processed)
        if not results:
            return {"text": "", "confidence": 0.0, "valid": False}
        text = " ".join([r[1] for r in results]).upper().strip()
        confidence = float(np.mean([r[2] for r in results]))
        text_clean = re.sub(r"[^A-Z0-9\s]", "", text)
        return {"text": text_clean, "confidence": confidence, "valid": self.validate(text_clean)}

    def validate(self, text):
        for pattern in PLATE_PATTERNS.values():
            if re.match(pattern, text.replace(" ", "")):
                return True
        return False
