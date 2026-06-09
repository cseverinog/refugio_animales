# Refugio animales

Este proyecto presenta un modelo logico relacional para un refugio de animales. La problematica social consiste en organizar la información de animales rescatados, adoptantes, voluntarios, vacunas y procesos de adopcion. 


Archivos: 
- sql/schema.sql:  creación de tablas y relaciones. 
- sql/seed.sql: datos iniciales. 
- sql/queries.sql: consultas solicitadas. 
- src/dtos.py: objetos DTO. 
- src/dao.py: acceso a datos con DAO. 
- main.py: demostración de inserción, actualización y proyección. 

 

Tablas principales: 
- especies: tipos de animales. 
- razas: razas asociadas a una especie. 
- animales: animales registrados en el refugio. 
- adoptantes: personas interesadas en adoptar. 
- voluntarios: personas que apoyan procesos del refugio. 
- vacunas_animales: vacunas aplicadas a cada animal. 
- adopciones: procesos de adopción.
