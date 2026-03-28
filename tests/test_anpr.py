import os, unittest
from src.database import PlateDatabase

class TestDB(unittest.TestCase):
    def setUp(self): self.db = PlateDatabase("test.db")
    def tearDown(self):
        if os.path.exists("test.db"): os.remove("test.db")
    def test_add(self):
        self.db.add_read("34ABC123", 0.95)
        self.assertEqual(len(self.db.search("34ABC")), 1)

if __name__ == "__main__": unittest.main()
