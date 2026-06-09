from dataclasses import dataclass


@dataclass
class AnimalDTO:
    nombre: str
    edad: int
    sexo: str
    estado: str
    fecha_ingreso: str
    id_especie: int
    id_raza: int


@dataclass
class AdoptanteDTO:
    nombre: str
    telefono: str
    correo: str
    ciudad: str


@dataclass
class AdopcionDTO:
    id_animal: int
    id_adoptante: int
    id_voluntario: int
    fecha_adopcion: str
    estado: str
