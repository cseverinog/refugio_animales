from pathlib import Path
import sys

ROOT = Path(__file__).parent
SRC = ROOT / "src"
sys.path.append(str(SRC))

from dao import AdopcionDAO, AnimalDAO, Database
from dtos import AdopcionDTO, AdoptanteDTO, AnimalDTO


def print_rows(title, rows):
    print(f"\n{title}")
    for row in rows:
        print(dict(row))


def main():
    database = Database(str(ROOT / "refugio.db"))
    database.execute_script(str(ROOT / "sql" / "schema.sql"))
    database.execute_script(str(ROOT / "sql" / "seed.sql"))

    animal_dao = AnimalDAO(database)
    adopcion_dao = AdopcionDAO(database)

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
    print(f"Animal insertado con id: {id_animal}")

    nuevo_adoptante = AdoptanteDTO(
        nombre="Valentina Marin",
        telefono="3051112233",
        correo="valentina@email.com",
        ciudad="Bogota",
    )
    id_adoptante = adopcion_dao.insert_adoptante(nuevo_adoptante)
    print(f"Adoptante insertado con id: {id_adoptante}")

    nueva_adopcion = AdopcionDTO(
        id_animal=id_animal,
        id_adoptante=id_adoptante,
        id_voluntario=1,
        fecha_adopcion="2026-05-10",
        estado="Aprobada",
    )
    adopcion_dao.insert(nueva_adopcion)
    animal_dao.update_estado(id_animal, "Adoptado")
    print("Estado del animal actualizado a Adoptado")

    print_rows("Animales disponibles:", animal_dao.list_available())
    print_rows("Proyeccion de contactos de adoptantes:", adopcion_dao.list_contact_projection())


if __name__ == "__main__":
    main()
