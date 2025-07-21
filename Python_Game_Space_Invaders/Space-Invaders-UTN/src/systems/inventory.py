import sqlite3  # Módulo para conectarse a SQLite (viene con Python)
import os  # Para manejar carpetas y rutas

class Inventory:
    def __init__(self, db_path='data/game_data.db'):
        # Obtener la carpeta de la ruta (ejemplo: 'data')
        folder = os.path.dirname(db_path)
        
        # Si la carpeta no existe, crearla para evitar errores al conectar SQLite
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        # Ahora sí, conectar a la base de datos (se crea si no existe)
        self.conn = sqlite3.connect(db_path)

        # Crear tabla si no existe
        self.create_table_inventory()
        self.create_table_skins()
    def create_table_inventory(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_id INTEGER,
                item_name TEXT NOT NULL,
                quantity INTEGER DEFAULT 1
            )
        ''')  # Crear tabla "inventory" si no existe
        self.conn.commit()  # Guardar cambios

    def add_item(self, player_id, item_name, quantity=1):  # Agregar o actualizar un ítem
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT quantity FROM inventory WHERE player_id=? AND item_name=?
        ''', (player_id, item_name))
        result = cursor.fetchone()
        if result:
            cursor.execute('''
                UPDATE inventory SET quantity=quantity+?
                WHERE player_id=? AND item_name=?
            ''', (quantity, player_id, item_name))  # Si existe, aumentar cantidad
        else:
            cursor.execute('''
                INSERT INTO inventory (player_id, item_name, quantity)
                VALUES (?, ?, ?)
            ''', (player_id, item_name, quantity))  # Si no existe, insertar nuevo
        self.conn.commit()

    def get_items(self, player_id):  # Obtener todos los ítems de un jugador
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT item_name, quantity FROM inventory
            WHERE player_id=?
        ''', (player_id,))
        return cursor.fetchall()

    def clear_inventory(self, player_id):  # Eliminar todos los ítems del jugador
        self.conn.execute('DELETE FROM inventory WHERE player_id=?', (player_id,))
        self.conn.commit()

    def create_table_skins(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS skins (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE,
                unlocked INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()

    def unlock_skin(self, name):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO skins (name, unlocked) VALUES (?, 1)
        ''', (name,))
        cursor.execute('''
            UPDATE skins SET unlocked = 1 WHERE name = ?
        ''', (name,))
        self.conn.commit()

    def get_unlocked_skins(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT name FROM skins WHERE unlocked = 1')
        return [row[0] for row in cursor.fetchall()]
