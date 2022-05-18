# md

**# Encabezadosencabezados**

Markdown dispone de cuatro niveles de encabezados definidos por el número de # antes del texto del encabezado. Pega los siguientes ejemplos en la caja de texto de la izquierda:

```
# Primer nivel de encabezado

## Segundo nivel de encabezado

### Tercer nivel de encabezado

#### Cuarto nivel de encabezado
```

El primer y segundo nivel de encabezado también se pueden escribir como sigue:

Primer nivel de encabezado

`**==========================**`

---

Segundo nivel de encabeado

`- **-------------------------**`

Estos se representarán como:

# Añadir énfasisañadir-énfasis

El texto se puede poner en cursivas encerrándolo entre los símbolos * o -. De la misma forma, el texto en negritas se escribe encerrando la palabra entre **o __.

Añade énfasis a una frase utilizando estos métodos:

¡Estoy `****muy****` entusiasmado con los tutoriales de `*_The Programming Historian en español_*!`

Lo cual queda representado así:

¡Estoy muy entusiasmado con los tutoriales de The Programming Historian en español!

Listadoslistados

Markdown soporta la creación de listas ordenadas y sin ordenar. Escribe la siguiente lista dentro de la caja de texto:

---

# Lista

- --------------
```
- Frutas

* Manzanas

* Naranjas

* Uvas

- Lácteos

* Leche

* Queso
```

Poner sangría al * te permite crear listas anidadas.

---

# Lista ordenadas**

- -----------------
```
1. Terminar el tutorial de Markdown
1. Ir a la tienda de abarrotes
2. Preparar el almuerzo
```
# codigo**

representamos los fragmentos de código encerrados entre dos signos de acento grave . Por ejemplo: `<br/>`. Cuando queremos representar un bloque completo de código lo debemos encerrar entre dos líneas de tres acentos graves.

`html`

<html>

<head>

<title>Título del sitio Web</title>

</head>
<body>
</body>
</html>


# Bloque de citasbloque-de-citas >**

`> Hola. Éste es un párrafo de texto incluido en un bloque de cita. Fíjate que tengo una sangría con respecto al margen izquierdo.`

# Enlaces de Internetenlaces-de-internet

Los enlaces de Internet se pueden escribir de dos maneras.

El título del enlace se encierra primero entre corchetes y después se incluye la dirección completa del URL entre paréntesis.

Para más tutoriales visita la página `[The Programming Historian en español](/es).`

Lo cual se representa así:

Los enlaces también se utilizan para crear notas a pie de página y son útiles porque, además, ayudan a mantener más ordenado tu documento en texto plano. Las notas a pie se escriben con un par adicional de corchetes con el número de referencia para establecer el vínculo que identifique la etiqueta.

Un ejemplo es el sitio `**[The Programming Historian en español][1]**`

Entonces puedes incluir el URL en otra parte del documento:

[1]: http://programminghistorian.org/

# Imágenes

Se pueden referir las imágenes mediante el uso de !, seguido de un texto alternativo entre corchetes, seguido a su vez por el URL de la imagen y un título opcional entre comillas. Esto no se representará como texto en tu documento pero te permitirá incluir la imagen en la visualización de una página en HTML.

![Logo de Wikipedia](https://upload.wikimedia.org/wikipedia/en/8/80/Wikipedia-logo-v2.svg "Wikipedia logo")


# Reglas y líneas horizontalesreglas-y-líneas-horizontales

Puedes incluir líneas horizontales si escribes en una misma línea cualquiera de los siguientes tres signos: -. * o _, sin importar los espacios que dejes entre ellos. Cualquiera de estas combinaciones generarán una línea horizontal:

"como decir el hr de html"

___

- * *
- - - - - -

# Tablas

La versión básica de Markdown no incluye tablas; sin embargo, algunos sitios web y aplicaciones usan variantes de Markdown que pueden incluir tablas y otras características especiales. GitHub Flavored Markdown es una de estas variantes y es utilizado para visualizar archivos .md en el navegador del sitio de GitHub.

Para crear una tabla en GitHub, usa barras verticales |para separar columnas y guiones entre los encabezados y el resto del contenido de la tabla. Dado que las barras verticales son sólo estrictamente necesarias entre columnas, puedes usarlas en los extremos de la tabla para darle una vista más acabada. Las celdas pueden tener contenido de cualquier extensión, y no es necesario que las barras verticales estén alineadas verticalmente entre sí.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |

| --------- | --------- | --------- |

| renglón 1, columna 1 | renglón 1, columna 2 | renglón 1, columna 3|

| renglón 2, columna 1 | renglón 2, columna 2 | renglón 2, columna 3|

| renglón 3, columna 1 | renglón 3, columna 2 | renglón 3, columna 3|

Para especificar la alineación del contenido de cada columna se pueden agregar dos puntos :al renglón de los encabezados como sigue:

| Alineado-izquierda | Centrado | Alineado-derecha |

| :-------- | :-------: | --------: |

| Manzanas | rojo | 5000 |

| Plátanos | amarillo | 75 |