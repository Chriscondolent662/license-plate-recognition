class PlateTracker:
    def __init__(self, max_age=30):
        self.max_age = max_age
        self.tracks = {}
        self._next_id = 0
        self._age = {}

    def update(self, plates):
        for plate in plates:
            text = plate.get("text", "")
            conf = plate.get("confidence", 0)
            if not text: continue
            if text in self.tracks:
                t = self.tracks[text]
                if conf > t["best_confidence"]: t["best_confidence"] = conf
                t["count"] += 1
            else:
                self.tracks[text] = {"id": self._next_id, "best_text": text, "best_confidence": conf, "count": 1}
                self._next_id += 1
            self._age[text] = 0
        for text in list(self._age.keys()):
            self._age[text] += 1
            if self._age[text] > self.max_age:
                del self._age[text]
                self.tracks.pop(text, None)
        return list(self.tracks.values())
