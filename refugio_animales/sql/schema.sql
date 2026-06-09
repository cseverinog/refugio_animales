PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS adopciones;
DROP TABLE IF EXISTS vacunas_animales;
DROP TABLE IF EXISTS animales;
DROP TABLE IF EXISTS razas;
DROP TABLE IF EXISTS especies;
DROP TABLE IF EXISTS adoptantes;
DROP TABLE IF EXISTS voluntarios;

CREATE TABLE especies (
    id_especie INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE
);

CREATE TABLE razas (
    id_raza INTEGER PRIMARY KEY AUTOINCREMENT,
    id_especie INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    FOREIGN KEY (id_especie) REFERENCES especies(id_especie),
    UNIQUE (id_especie, nombre)
);

CREATE TABLE animales (
    id_animal INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    sexo TEXT NOT NULL,
    estado TEXT NOT NULL,
    fecha_ingreso TEXT NOT NULL,
    id_especie INTEGER NOT NULL,
    id_raza INTEGER NOT NULL,
    FOREIGN KEY (id_especie) REFERENCES especies(id_especie),
    FOREIGN KEY (id_raza) REFERENCES razas(id_raza)
);

CREATE TABLE adoptantes (
    id_adoptante INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL,
    correo TEXT NOT NULL UNIQUE,
    ciudad TEXT NOT NULL
);

CREATE TABLE voluntarios (
    id_voluntario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL,
    rol TEXT NOT NULL
);

CREATE TABLE vacunas_animales (
    id_vacuna INTEGER PRIMARY KEY AUTOINCREMENT,
    id_animal INTEGER NOT NULL,
    nombre_vacuna TEXT NOT NULL,
    fecha_aplicacion TEXT NOT NULL,
    FOREIGN KEY (id_animal) REFERENCES animales(id_animal)
);

CREATE TABLE adopciones (
    id_adopcion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_animal INTEGER NOT NULL,
    id_adoptante INTEGER NOT NULL,
    id_voluntario INTEGER NOT NULL,
    fecha_adopcion TEXT NOT NULL,
    estado TEXT NOT NULL,
    FOREIGN KEY (id_animal) REFERENCES animales(id_animal),
    FOREIGN KEY (id_adoptante) REFERENCES adoptantes(id_adoptante),
    FOREIGN KEY (id_voluntario) REFERENCES voluntarios(id_voluntario)
);
