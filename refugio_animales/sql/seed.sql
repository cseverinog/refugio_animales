INSERT INTO especies (nombre) VALUES
('Perro'),
('Gato');

INSERT INTO razas (id_especie, nombre) VALUES
(1, 'Labrador'),
(1, 'Criollo'),
(1, 'Beagle'),
(2, 'Siames'),
(2, 'Criollo');

INSERT INTO animales (nombre, edad, sexo, estado, fecha_ingreso, id_especie, id_raza) VALUES
('Luna', 3, 'Hembra', 'Disponible', '2026-01-10', 1, 2),
('Max', 5, 'Macho', 'Adoptado', '2026-01-15', 1, 1),
('Michi', 2, 'Macho', 'Disponible', '2026-02-02', 2, 5),
('Nala', 1, 'Hembra', 'En tratamiento', '2026-02-20', 2, 4),
('Toby', 4, 'Macho', 'Adoptado', '2026-03-05', 1, 3),
('Kiara', 6, 'Hembra', 'Disponible', '2026-03-18', 1, 2);

INSERT INTO adoptantes (nombre, telefono, correo, ciudad) VALUES
('Laura Gomez', '3001112233', 'laura@email.com', 'Bogota'),
('Carlos Ruiz', '3014445566', 'carlos@email.com', 'Medellin'),
('Ana Torres', '3027778899', 'ana@email.com', 'Cali'),
('Sofia Perez', '3035556677', 'sofia@email.com', 'Bogota'),
('Miguel Rojas', '3048889900', 'miguel@email.com', 'Barranquilla');

INSERT INTO voluntarios (nombre, telefono, rol) VALUES
('Daniela Mora', '3101234567', 'Entrevistas'),
('Andres Lopez', '3117654321', 'Seguimiento'),
('Paula Castro', '3129876543', 'Cuidado animal'),
('Julian Rios', '3132223344', 'Transporte'),
('Camila Diaz', '3145556677', 'Coordinacion');

INSERT INTO vacunas_animales (id_animal, nombre_vacuna, fecha_aplicacion) VALUES
(1, 'Rabia', '2026-01-12'),
(1, 'Triple canina', '2026-01-18'),
(2, 'Rabia', '2026-01-20'),
(3, 'Triple felina', '2026-02-05'),
(4, 'Triple felina', '2026-02-22'),
(5, 'Rabia', '2026-03-08');

INSERT INTO adopciones (id_animal, id_adoptante, id_voluntario, fecha_adopcion, estado) VALUES
(2, 1, 1, '2026-02-01', 'Aprobada'),
(5, 2, 2, '2026-03-20', 'Aprobada'),
(3, 3, 1, '2026-04-01', 'En revision'),
(1, 4, 5, '2026-04-10', 'En revision'),
(6, 5, 3, '2026-04-12', 'Cancelada');
