import sqlite3  # Módulo estándar para bases de datos SQLite
import json
import os

class Progress:
    def __init__(self, db_path='data/game_data.db'):  # Ruta a la base
        self.conn = sqlite3.connect(db_path)
        self.create_table()
        # Para scores tipo ranking
        self.scores_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data'))
        self.scores_file = os.path.join(self.scores_dir, 'scores.json')

    def create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS progress (
                player_id INTEGER PRIMARY KEY,
                level INTEGER DEFAULT 1,
                score INTEGER DEFAULT 0,
                lives INTEGER DEFAULT 3
            )
        ''')  # Tabla para guardar el progreso del jugador
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS max_score (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                score INTEGER DEFAULT 0
            )
        ''')
        # Nueva tabla para scores tipo ranking
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        ''')
        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS player_settings (
            id INTEGER PRIMARY KEY,
            selected_skin TEXT DEFAULT "player0.png"
        )
        ''')
        self.conn.commit()

    def save_progress(self, player_id, level, score, lives):  # Guardar datos
        self.conn.execute('''
            INSERT INTO progress (player_id, level, score, lives)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(player_id) DO UPDATE SET
                level=excluded.level,
                score=excluded.score,
                lives=excluded.lives
        ''', (player_id, level, score, lives))  # Insertar o actualizar
        self.conn.commit()

    def load_progress(self, player_id):  # Cargar datos de un jugador
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT level, score, lives FROM progress WHERE player_id=?
        ''', (player_id,))
        return cursor.fetchone() or (1, 0, 3)  # Si no hay datos, usar valores por defecto

    def get_max_score(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT score FROM max_score WHERE id=1')
        row = cursor.fetchone()
        return row[0] if row else 0

    def set_max_score(self, score):
        self.conn.execute('''
            INSERT INTO max_score (id, score)
            VALUES (1, ?)
            ON CONFLICT(id) DO UPDATE SET score=excluded.score
        ''', (score,))
        self.conn.commit()

    # --- SCOREBOARD tipo ranking en SQLite ---
    def save_score(self, name, score):
        self.conn.execute('''
            INSERT INTO scores (name, score) VALUES (?, ?)
        ''', (name, score))
        self.conn.commit()

    def load_scores(self, limit=5):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT name, score FROM scores ORDER BY score DESC, id ASC LIMIT ?
        ''', (limit,))
        rows = cursor.fetchall()
        return [{'name': row[0], 'score': row[1]} for row in rows]
    def save_selected_skin(self, skin_name):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO player_settings (id, selected_skin) 
            VALUES (1, ?)
        ''', (skin_name,))
        self.conn.commit()

    def get_selected_skin(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT selected_skin FROM player_settings WHERE id = 1
        ''')
        result = cursor.fetchone()
        return result[0] if result else "player0.png"