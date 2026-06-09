from pathlib import Path
import sys

ROOT = Path(__file__).parent
SRC = ROOT / "src"
sys.path.append(str(SRC))

from dao import AdopcionDAO, AnimalDAO, Database
from dtos import AdopcionDTO, AdoptanteDTO, AnimalDTO


def pause():
    try:
        input("\nPresiona Enter para continuar...")
    except EOFError:
        pass


def print_rows(rows):
    for row in rows:
        print(dict(row))


def run_query(database, title, query):
    print(f"\n{title}")
    with database.connect() as connection:
        rows = connection.execute(query).fetchall()
    print_rows(rows)


def main():
    database = Database(str(ROOT / "refugio.db"))
    animal_dao = AnimalDAO(database)
    adopcion_dao = AdopcionDAO(database)

    print("DEMO INTERACTIVA - REFUGIO DE ANIMALES")
    print("Esta demo muestra base de datos, consultas, DAO y DTO paso a paso.")
    pause()

    print("\n1. Crear base de datos y tablas")
    print("Se ejecuta sql/schema.sql para crear el modelo relacional.")
    database.execute_script(str(ROOT / "sql" / "schema.sql"))
    print("Tablas creadas correctamente.")
    pause()

    print("\n2. Insertar datos iniciales")
    print("Se ejecuta sql/seed.sql con especies, razas, animales, adoptantes, voluntarios, vacunas y adopciones.")
    database.execute_script(str(ROOT / "sql" / "seed.sql"))
    print("Datos iniciales insertados correctamente.")
    pause()

    run_query(
        database,
        "3. Consulta INNER JOIN: animales con especie y raza",
        """
        SELECT a.nombre AS animal, e.nombre AS especie, r.nombre AS raza, a.estado
        FROM animales a
        INNER JOIN especies e ON a.id_especie = e.id_especie
        INNER JOIN razas r ON a.id_raza = r.id_raza
        """,
    )
    pause()

    print("\n4. Insercion usando DTO y DAO")
    print("Se crea un AnimalDTO para Rocky y AnimalDAO lo inserta en la base de datos.")
    nuevo_animal = AnimalDTO(
        nombre="Rocky",
        edad=2,
        sexo="Macho",
        estado="Disponible",
        fecha_ingreso="2026-05-01",
        id_especie=1,
        id_raza=2,
    )
    id_animal = animal_dao.insert(nuevo_animal)
    print(f"Animal insertado: Rocky con id {id_animal}")

    print("\nTambien se crea un AdoptanteDTO para registrar a la persona interesada.")
    nuevo_adoptante = AdoptanteDTO(
        nombre="Valentina Marin",
        telefono="3051112233",
        correo="valentina@email.com",
        ciudad="Bogota",
    )
    id_adoptante = adopcion_dao.insert_adoptante(nuevo_adoptante)
    print(f"Adoptante insertada: Valentina Marin con id {id_adoptante}")
    pause()

    print("\n5. Registrar adopcion usando DTO y DAO")
    nueva_adopcion = AdopcionDTO(
        id_animal=id_animal,
        id_adoptante=id_adoptante,
        id_voluntario=1,
        fecha_adopcion="2026-05-10",
        estado="Aprobada",
    )
    adopcion_dao.insert(nueva_adopcion)
    print("Adopcion registrada correctamente.")

    print("\nAhora se usa UPDATE para cambiar el estado de Rocky a Adoptado.")
    animal_dao.update_estado(id_animal, "Adoptado")
    print("Estado actualizado correctamente.")
    pause()

    run_query(
        database,
        "6. UNION: adoptantes y voluntarios en una sola lista",
        """
        SELECT nombre, 'Adoptante' AS tipo_persona FROM adoptantes
        UNION
        SELECT nombre, 'Voluntario' AS tipo_persona FROM voluntarios
        """,
    )
    pause()

    run_query(
        database,
        "7. Proyeccion: solo nombre y correo de adoptantes",
        "SELECT nombre, correo FROM adoptantes",
    )
    pause()

    print("\nDemo finalizada.")
    print("Con esto se evidencia modelo relacional, datos, consultas, UPDATE, UNION, DAO y DTO.")


if __name__ == "__main__":
    main()
