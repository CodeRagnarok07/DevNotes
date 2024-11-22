# Scrum

Tags: Productividad
Fuentes: Curso Práctico de Project Management (../Fuentes%20521e7fa667264cc69ca57be2edb5df61/Curso%20Pra%CC%81ctico%20de%20Project%20Management%20376709ea33224e9da20a32da3d2c6b9f.md), Curso de Fundamentos de Project Management (../Fuentes%20521e7fa667264cc69ca57be2edb5df61/Curso%20de%20Fundamentos%20de%20Project%20Management%205a33401d631542dbb28cc43d37043b4b.md)
State: Backlog

# Roles y actividades:

### Product Owner:

> 
> 
> - Crea la lista de Producto o backlog
> - Crea las users History
> - asigna prioridades
> - Revision del sprint

### Scrum Master:

> 
> 
> - Organiza los eventos [Sprints, planning, revision, retrospectiva]
> - encuentra optima el desarrollo

### Equipo de desarrollo:

> 
> 
> - Encargados de desarrollar el producto
> - elijen el alcance de sus capacidades
> - Asignan tareas no dependientes para el desarrollo

# Eventos

### 0.- Sprint [ 1 a 2 semanas ]

- periodo de tiempo para entregar un producto funcional
- Debe tener un propósito claro de producto funcional
- Puede ser modificado o cancelado por consenso entre desarrolladores y Product owner

### 1.- Planning [ **lunes** max 2 horas]

- Define el propósito del sprint
- Se mide el alcance del equipo de desarrollo para completar el sprint
- se elige el nivel de dificultad de cada actividad
- Se agregan al sprint las actividades desde el backlog
- Deben estar definidas las user history previamente

### 2.- Daily [Historia por escrito] [ - hilo de discord diario o documento de exel  ]

- Responder 3 preguntas
    - que hice ayer?
    - que hare hoy?
    - tengo algún impedimento?
- Los desarrolladores ofrecen su ayuda a los que tienen problemas
- con las actividades completadas se va actualizando el medidor del scrum

### 3.- Revision del producto

- El producto debe estar en producción
- El product Owner se encarga de revisar que todas las funcionalidades esten completas, y anotar todo lo que no funcione bien
- Debe ser consultado con el equipo de desarrollo todas la lista redactada anteriormente
- se actualiza la lista de producto para el próximo sprint

### 4.- Retrospectiva

- Participa todo el equipo
- se responden 3 preguntas
    - que hicimos bien
    - que no hicimos tan bien
    - que podemos mejorar
- No se deben buscar culpables

# Medición de alcance del equipo de desarrollo

para  la planificación del sprint hay que conocer el alcance de las capacidades del equipo de desarrollo, para no agregar actividades que seran imposibles de completar en el tiempo estipulado, a menos que se centren en solo esa actividad

en base a 10 puntos

### Experiencia

- ¿Tienes experiencia realizando esta actividad? 5pts
- ¿Tienes conocimientos sobre dicha actividad pero no la as realizado? 3pts
- ¿No tienes conocimientos sobre dicha actividad? 1pts

### Problemas

- ¿no hay impedimentos para su desarrollo? 5pts
- ¿Crees que existe algún impedimento para desarrollar la actividad? 3pts
- ¿no conoces que posibles problemas traerá el desarrollo de esta actividad? 1pts

# Medición del sprint

# Scrum En GitHub

## Kanban:

### **GitHub projects para lista de productos**

- se anotan toda la lista de productos con su descripción como user history
    
    ```python
    Titulo de la tarea
    - que quiero?
    - Como lo queremos?
    - accion o para que lo queremos?
    
    Criterio de aceptacion para que este completada
    
    ```
    

### **Issues para historias de usuarios**:

- Los issues son la lista de producto, se deben discutir con la información disponible sobre la actividad,
- Una ves completada la actividad deberá ser documentada en la wiki y debe ser cerrado el tema