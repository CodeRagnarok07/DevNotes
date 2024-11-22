---
File: Areas/Backlog/DevNote/Enginner/Patrones de diseño/SOLID.md
tags:
  - nota-permanente
Lang: 
description: 
note-type: permanent
focus: false
---


# Solid

## 1. **Single Responsibility Principle (SRP)**

Una clase debe tener una y solo una razón para cambiar. 
Esto significa que una clase debe tener una responsabilidad única y no debe ser responsable de varias tareas.

" Hay quien define que este principio dice que una funcionalidad solo tiene que tener un uso en codigo "

## 2. **Open/Closed Principle (OCP)** 

> abierta para la extensión pero cerrada para la modificación.

 - Una clase debe estar abierta para la extensión pero cerrada para la modificación.
 -  Esto permite agregar nuevas funcionalidades sin alterar la clase original.
 - Unicamente para llamar a sus menthodos no tanto para la instanciacion


## 3. **Liskov Substitution Principle (LSP)** 

Aplicado únicamente a clases 
- Todos los hijos directos de una clase pueden ser usados en para el mismo caso de uso
- Que los hijos tengan extension pero que pueda ser nula o tenga un manejo de error

aplicable para los test
- si un test para una clase padre funcionan deberia funcionar para una clase hija


Las subclases deben ser intercambiables con sus superclases (molde). 
Esto garantiza la coherencia y la sustitución de clases sin afectar la funcionalidad del sistema.




## 4. **Interface Segregation Principle (ISP)**

Las interfaces deben ser diseñadas para ser utilizadas por un solo cliente, evitando la sobrecarga de métodos y la dependencia entre interfaces.

- Una clase no debe usar clases de elementos que no va a necesitar 
- por lo tant deberia cumplir el LSP


## 5. **Dependency Inversion Principle (DIP)**

Las dependencias deben ser invertidas, es decir, 
las clases deben ser diseñadas para ser dependientes de abstracciones en lugar de concretos.

- Una clase padre no puede estar condicionada por clases hijas
- Una clase de nivel superior no puede depender de clases mas detalladas