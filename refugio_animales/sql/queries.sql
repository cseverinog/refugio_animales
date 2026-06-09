-- 1. Listar todos los animales registrados
SELECT id_animal, nombre, edad, sexo, estado
FROM animales;

-- 2. Animales disponibles para adopcion
SELECT nombre, edad, sexo
FROM animales
WHERE estado = 'Disponible';

-- 3. Animales con su especie y raza
SELECT a.nombre AS animal, e.nombre AS especie, r.nombre AS raza, a.estado
FROM animales a
INNER JOIN especies e ON a.id_especie = e.id_especie
INNER JOIN razas r ON a.id_raza = r.id_raza;

-- 4. Adopciones con animal, adoptante y voluntario
SELECT a.nombre AS animal, ad.nombre AS adoptante, v.nombre AS voluntario, ap.fecha_adopcion, ap.estado
FROM adopciones ap
INNER JOIN animales a ON ap.id_animal = a.id_animal
INNER JOIN adoptantes ad ON ap.id_adoptante = ad.id_adoptante
INNER JOIN voluntarios v ON ap.id_voluntario = v.id_voluntario;

-- 5. Vacunas aplicadas por animal
SELECT a.nombre AS animal, va.nombre_vacuna, va.fecha_aplicacion
FROM vacunas_animales va
INNER JOIN animales a ON va.id_animal = a.id_animal;

-- 6. Cantidad de animales por estado
SELECT estado, COUNT(*) AS cantidad
FROM animales
GROUP BY estado;

-- 7. Cantidad de animales por especie
SELECT e.nombre AS especie, COUNT(*) AS cantidad
FROM animales a
INNER JOIN especies e ON a.id_especie = e.id_especie
GROUP BY e.nombre;

-- 8. Actualizar estado de un animal cuando se adopta
UPDATE animales
SET estado = 'Adoptado'
WHERE id_animal = 1;

-- 9. UNION entre nombres de adoptantes y voluntarios
SELECT nombre, 'Adoptante' AS tipo_persona
FROM adoptantes
UNION
SELECT nombre, 'Voluntario' AS tipo_persona
FROM voluntarios;

-- 10. Proyeccion de datos de contacto de adoptantes
SELECT nombre, correo
FROM adoptantes;
