import cv2, numpy as np
from fastapi import FastAPI, File, UploadFile, HTTPException
from .plate_detector import PlateDetector
from .ocr_engine import OCREngine
from .database import PlateDatabase

app = FastAPI(title="ANPR API", version="1.0.0")
detector = PlateDetector()
ocr = OCREngine()
db = PlateDatabase()

@app.post("/recognize")
async def recognize(file: UploadFile = File(...)):
    img = cv2.imdecode(np.frombuffer(await file.read(), np.uint8), cv2.IMREAD_COLOR)
    if img is None: raise HTTPException(400, "Invalid image")
    results = []
    for p in detector.detect(img):
        text = ocr.read_plate(p["image"])
        if text["text"]: db.add_read(text["text"], text["confidence"])
        results.append(text)
    return {"plates": results}

@app.get("/stats")
async def stats(): return db.get_stats()
