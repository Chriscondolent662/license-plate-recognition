import sqlite3
from datetime import datetime

class PlateDatabase:
    def __init__(self, db_path="plates.db"):
        self.db_path = db_path
        with self._connect() as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS plate_reads (id INTEGER PRIMARY KEY AUTOINCREMENT, plate_text TEXT, confidence REAL, camera_id TEXT, timestamp TEXT)")

    def _connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def add_read(self, plate_text, confidence, camera_id="default"):
        with self._connect() as conn:
            conn.execute("INSERT INTO plate_reads (plate_text, confidence, camera_id, timestamp) VALUES (?,?,?,?)",
                         (plate_text, confidence, camera_id, datetime.now().isoformat()))

    def search(self, plate_text):
        with self._connect() as conn:
            return [dict(r) for r in conn.execute("SELECT * FROM plate_reads WHERE plate_text LIKE ?", (f"%{plate_text}%",)).fetchall()]

    def get_stats(self):
        with self._connect() as conn:
            total = conn.execute("SELECT COUNT(*) FROM plate_reads").fetchone()[0]
            unique = conn.execute("SELECT COUNT(DISTINCT plate_text) FROM plate_reads").fetchone()[0]
            return {"total_reads": total, "unique_plates": unique}
