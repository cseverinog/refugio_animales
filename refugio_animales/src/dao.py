import sqlite3
from pathlib import Path

from dtos import AdopcionDTO, AdoptanteDTO, AnimalDTO


class Database:
    def __init__(self, db_path: str = "refugio.db"):
        self.db_path = db_path

    def connect(self):
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def execute_script(self, script_path: str):
        sql = Path(script_path).read_text(encoding="utf-8")
        with self.connect() as connection:
            connection.executescript(sql)


class AnimalDAO:
    def __init__(self, database: Database):
        self.database = database

    def insert(self, animal: AnimalDTO):
        query = """
        INSERT INTO animales (nombre, edad, sexo, estado, fecha_ingreso, id_especie, id_raza)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        with self.database.connect() as connection:
            cursor = connection.execute(
                query,
                (
                    animal.nombre,
                    animal.edad,
                    animal.sexo,
                    animal.estado,
                    animal.fecha_ingreso,
                    animal.id_especie,
                    animal.id_raza,
                ),
            )
            return cursor.lastrowid

    def update_estado(self, id_animal: int, estado: str):
        with self.database.connect() as connection:
            connection.execute(
                "UPDATE animales SET estado = ? WHERE id_animal = ?",
                (estado, id_animal),
            )

    def list_available(self):
        query = """
        SELECT a.id_animal, a.nombre, a.edad, e.nombre AS especie, r.nombre AS raza
        FROM animales a
        INNER JOIN especies e ON a.id_especie = e.id_especie
        INNER JOIN razas r ON a.id_raza = r.id_raza
        WHERE a.estado = 'Disponible'
        """
        with self.database.connect() as connection:
            return connection.execute(query).fetchall()


class AdopcionDAO:
    def __init__(self, database: Database):
        self.database = database

    def insert_adoptante(self, adoptante: AdoptanteDTO):
        query = """
        INSERT INTO adoptantes (nombre, telefono, correo, ciudad)
        VALUES (?, ?, ?, ?)
        """
        with self.database.connect() as connection:
            cursor = connection.execute(
                query,
                (adoptante.nombre, adoptante.telefono, adoptante.correo, adoptante.ciudad),
            )
            return cursor.lastrowid

    def insert(self, adopcion: AdopcionDTO):
        query = """
        INSERT INTO adopciones (id_animal, id_adoptante, id_voluntario, fecha_adopcion, estado)
        VALUES (?, ?, ?, ?, ?)
        """
        with self.database.connect() as connection:
            cursor = connection.execute(
                query,
                (
                    adopcion.id_animal,
                    adopcion.id_adoptante,
                    adopcion.id_voluntario,
                    adopcion.fecha_adopcion,
                    adopcion.estado,
                ),
            )
            return cursor.lastrowid

    def list_contact_projection(self):
        with self.database.connect() as connection:
            return connection.execute("SELECT nombre, correo FROM adoptantes").fetchall()
