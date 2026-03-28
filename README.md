# Automatic License Plate Recognition (ANPR)

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green.svg)](https://ultralytics.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Real-time automatic license plate recognition using YOLOv8 for plate detection and EasyOCR for text extraction. Supports EU and Turkish plate formats with database logging.

## Features

- **YOLOv8 Detection**: Fine-tuned model for license plate localization
- **Dual OCR**: EasyOCR primary + Tesseract fallback
- **Plate Tracking**: Cross-frame tracking with best-read selection
- **Format Validation**: Regex-based plate format verification (EU/TR)
- **Database**: SQLite logging with search and history
- **REST API**: FastAPI endpoints for recognition and queries

## Installation

```bash
git clone https://github.com/theYsnS/license-plate-recognition.git
cd license-plate-recognition
pip install -r requirements.txt
```

## Usage

```bash
python main.py --mode live --source 0
python main.py --mode image --input photo.jpg
python main.py --mode api --port 8000
```

## License

MIT License - see [LICENSE](LICENSE) for details.