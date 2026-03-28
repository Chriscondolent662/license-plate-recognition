import argparse, cv2
from src.plate_detector import PlateDetector
from src.ocr_engine import OCREngine

def main():
    p = argparse.ArgumentParser(description="ANPR System")
    p.add_argument("--mode", choices=["image", "live", "api"], default="image")
    p.add_argument("--input", help="Image path")
    p.add_argument("--port", type=int, default=8000)
    args = p.parse_args()
    if args.mode == "image":
        for plate in PlateDetector().detect(cv2.imread(args.input)):
            r = OCREngine().read_plate(plate["image"])
            print(f"Plate: {r['text']} (conf={r['confidence']:.2f})")
    elif args.mode == "api":
        import uvicorn; uvicorn.run("src.api:app", host="0.0.0.0", port=args.port)

if __name__ == "__main__": main()
