import sqlite3

class DatabaseManager:
    def __init__(self, db_name="personal_hub.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # Example tables for Gym Tracker and Flashcards
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS gym_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            exercise TEXT NOT NULL,
            sets INTEGER NOT NULL,
            reps INTEGER NOT NULL,
            weight REAL NOT NULL
        )
        """)
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            category TEXT
        )
        """)
        self.connection.commit()

    def insert_gym_log(self, date, exercise, sets, reps, weight):
        self.cursor.execute("""
        INSERT INTO gym_logs (date, exercise, sets, reps, weight)
        VALUES (?, ?, ?, ?, ?)
        """, (date, exercise, sets, reps, weight))
        self.connection.commit()

    def fetch_gym_logs(self):
        self.cursor.execute("SELECT * FROM gym_logs")
        return self.cursor.fetchall()

    def insert_flashcard(self, question, answer, category):
        self.cursor.execute("""
        INSERT INTO flashcards (question, answer, category)
        VALUES (?, ?, ?)
        """, (question, answer, category))
        self.connection.commit()

    def fetch_flashcards(self):
        self.cursor.execute("SELECT * FROM flashcards")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
