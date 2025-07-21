import sqlite3  # Para conectar a la base SQLite

class Upgrades:
    def __init__(self, db_path='data/game_data.db'):  # Ruta a la base
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS upgrades (
                player_id INTEGER,
                upgrade_name TEXT,
                level INTEGER DEFAULT 1,
                PRIMARY KEY (player_id, upgrade_name)
            )
        ''')  # Crear tabla para mejoras desbloqueadas
        self.conn.commit()

    def unlock_upgrade(self, player_id, upgrade_name):  # Registrar nueva mejora
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO upgrades (player_id, upgrade_name, level)
            VALUES (?, ?, 1)
        ''', (player_id, upgrade_name))  # Si ya existe, no la inserta
        self.conn.commit()

    def upgrade_level(self, player_id, upgrade_name):  # Subir de nivel una mejora
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE upgrades SET level = level + 1
            WHERE player_id = ? AND upgrade_name = ?
        ''', (player_id, upgrade_name))
        self.conn.commit()

    def get_upgrades(self, player_id):  # Obtener todas las mejoras de un jugador
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT upgrade_name, level FROM upgrades
            WHERE player_id = ?
        ''', (player_id,))
        return cursor.fetchall()
