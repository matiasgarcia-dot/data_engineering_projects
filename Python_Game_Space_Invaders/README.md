# 🚀 Space Invaders - Juego en Python con Pygame

Este es un proyecto académico para la materia Programacion 3 en UTN San Rafael.  
Se trata de una versión simple y personalizada del clásico **Space Invaders**, desarrollado completamente en Python usando la librería **Pygame**.

**VIDEO DEMOSTRACIÓN DEL PROYECTO**: [click aquí 🔗](https://drive.google.com/file/d/1MJLILGkoGaGpMZW0b_3PS-NrMR8TpJsg/view?usp=drive_link)

---

## 🎮 Características

- Movimiento y disparos del jugador
- Enemigos con comportamiento básico
- Power-ups e ítems recolectables
- Sistema de progreso y niveles
- Inventario persistente
- Guardado de puntaje y mejoras

---

## 🛠️ Tecnologías usadas

- [Python 3.x](https://www.python.org/)
- [Pygame](https://www.pygame.org/) para la lógica gráfica y del juego
- SQLite (via `sqlite3`) para persistencia local de progreso
- Git + GitHub para control de versiones y trabajo colaborativo

---

## 📁 Estructura del proyecto

```text
space_invaders/
│
├── assets/                  # Archivos multimedia
│   ├── images/              # Imágenes PNG, sprites, etc.
│   ├── sounds/              # Efectos de sonido y música
│   └── fonts/               # Tipografías personalizadas
│
├── data/                    # Datos persistentes del jugador
│   └── game_data.db         # Base de datos SQLite (o archivos JSON)
│
├── src/                     # Código fuente principal
│   ├── __init__.py
│   ├── main.py              # Loop principal del juego
│   ├── settings.py          # Configuración general (pantalla, FPS, colores)
│   ├── database.py          # Conexión y acceso a datos (SQLite)
│
│   ├── core/                # Motor de juego (control general)
│   │   ├── game.py          # Clase Game: controla niveles, reinicios, etc.
│   │   └── hud.py           # Dibujo de interfaz (puntaje, vidas, inventario)
│
│   ├── entities/            # Entidades del juego
│   │   ├── player.py        # Clase Player y sus disparos
│   │   ├── enemy.py         # Clase Enemy
│   │   ├── bullet.py        # Disparos de jugador/enemigos
│   │   └── item.py          # Power-ups u objetos
│
│   ├── systems/             
│   │   ├── inventory.py     # Manejo de ítems recolectados
│   │   ├── progress.py      # Guardado de nivel, score, estado
│   │   └── upgrades.py      # Mejoras desbloqueables (vida, armas, etc.)
│
│   └── utils/               # Utilidades varias
│       └── helpers.py       # Funciones auxiliares
│
├── README.md                # Documentación del proyecto
├── requirements.txt         # Librerías necesarias
└── .gitignore               # Archivos a ignorar por Git
```

---

## 🧑‍💻 División del trabajo

| Integrantes                 | Rol                                                                  |
|----------------------------|----------------------------------------------------------------------|
| 🎯 Alexander Montenegro    | Player y mecánicas principales (`player.py`)                         |
| 💥 Marina Evangelista      | Enemigos y disparos (`enemy.py`, `bullet.py`)                        |
| 🎮 Matias Garcia           | Loop del juego y niveles (`game.py`, `main.py`)                      |
| 🖥️ Franco Moyano           | HUD e interfaz visual (`hud.py`, menús)                              |
| 🧠 Manolo Bassot           | Inventario, progreso, mejoras (`inventory.py`, `progress.py`, etc.) |

---

## ▶️ Cómo ejecutar el juego

1. Cloná el repositorio:

```bash
git clone https://github.com/usuario/space-invaders.git
cd space-invaders

pip install -r requirements.txt

cd .\Proyecto-Integrador-Python\Space-Invaders-UTN\src\

python main.py
```
## 🎮 Instrucciones del Juego

### 🔫 Controles Básicos
| Tecla           | Acción                  |
|-----------------|-------------------------|
| `←` o `A`       | Mover nave a la izquierda |
| `→` o `D`       | Mover nave a la derecha   |
| `ESPACIO`       | Disparar                 |
| `ESC`           | Volver al menú           |

### 🎯 Objetivo
- Destruye oleadas de naves enemigas
- Sobrevive el mayor tiempo posible
- Alcanza el top 5 de puntuaciones

### 🛸 Sistema de Skins

#### 🔓 Desbloqueo de Naves
| Nivel | Skin Desbloqueada |
|-------|-------------------|
| 3     | Nave 1         |
| 6     | Nave 2         |
| 9     | Nave 3         |

#### ✨ Cómo cambiar tu nave
1. En el menú principal → "Seleccionar Nave"
2. Usa `←` `→` para ver las skins disponibles
3. Presiona `ENTER` para confirmar
4. ¡Juega con tu nueva nave!

### 🏆 Consejos Pro
- Dispara a los enemigos desde abajo para mayor precisión
- Las naves enemigas aceleran cada nivel completado
