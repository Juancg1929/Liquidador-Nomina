# Liquidador de Nómina

## Integrantes

-Juan Camilo García Castro

## Descripción

Aplicación desarrollada en Python que permite calcular la liquidación de nómina de un empleado teniendo en cuenta el salario básico, los días trabajados, las bonificaciones, las comisiones y otros descuentos.

El sistema calcula las deducciones correspondientes a salud y pensión y obtiene el valor neto a pagar.

El proyecto incluye pruebas unitarias desarrolladas con `unittest` para validar el correcto funcionamiento de la lógica del sistema.

Además, cuenta con dos interfaces: una de consola y una interfaz gráfica (GUI) desarrollada con **Kivy**.

## Entradas

- Salario básico.
- Días trabajados.
- Bonificación.
- Comisión.
- Otros descuentos.

## Procesos

- Validar los datos ingresados.
- Calcular el salario proporcional según los días trabajados.
- Sumar bonificaciones y comisiones.
- Obtener el total devengado.
- Calcular el descuento de salud.
- Calcular el descuento de pensión.
- Calcular el total de deducciones.
- Obtener el neto a pagar.

## Salidas

- Total devengado.
- Total de deducciones.
- Neto a pagar.

## Arquitectura del proyecto

El proyecto está organizado por capas: la lógica de negocio en `src/model`, las interfaces en `src/view` (consola y GUI) y las pruebas en `tests`.

```text
Liquidador-Nomina/
├── src/
│   ├── model/
│   │   ├── constantes.py
│   │   ├── errores.py
│   │   ├── datos_nomina.py  
│   │   ├── logica_nomina.py
│   │   └── validacion.py
│   └── view/
│       ├── console/
│       │   └── consola.py
│       └── GUI/
│           ├── __init__.py
│           └── liquidador_gui.py
├── tests/
│   └── tests_nomina.py
├── docs/
├── .gitignore
├── requirements.txt
└── README.md
```

## Descripción de los archivos

### Lógica de Negocio (src/model/)

- `src/model/constantes.py`: contiene las constantes del cálculo (días del mes, tasas de descuento).
- `src/model/errores.py`: contiene los errores personalizados e indica qué sucedió, por qué, dónde y cómo se soluciona.
- `src/model/datos_nomina.py`: contiene la clase `DatosNomina` que estructura los datos del empleado.
- `src/model/logica_nomina.py`: contiene la lógica principal de cálculo dividida en funciones con responsabilidades específicas.
- `src/model/validacion.py`: contiene la clase que valida las entradas antes de calcular.

### Interfaz de Usuario (src/view/)

- `src/view/console/consola.py`: interfaz de consola para ingresar los datos y mostrar el resultado.
- `src/view/GUI/liquidador_gui.py`: interfaz gráfica (GUI) desarrollada con Kivy para una experiencia más amigable.

### Pruebas y Documentación

- `tests/tests_nomina.py`: contiene las pruebas unitarias desarrolladas con `unittest`.
- `docs/`: contiene la matriz de casos de prueba y demás documentación del proyecto.
- `README.md`: contiene la descripción general del proyecto y las instrucciones para su ejecución.

## Instalación de dependencias

Antes de ejecutar la aplicación, instala las dependencias necesarias:

```bash
pip install kivy
```

O si tienes un archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Ejecución de las pruebas unitarias

Para ejecutar las pruebas unitarias, ubicarse desde la terminal en la carpeta principal del proyecto y ejecutar:

```bash
py -m unittest tests.tests_nomina
```

Actualmente el proyecto cuenta con 10 pruebas unitarias:

- 3 casos normales.
- 3 casos extraordinarios.
- 4 casos de error.

Si todas las pruebas se ejecutan correctamente, la terminal mostrará un resultado similar a:

```text
..........
Ran 10 tests in ...
OK
```

## Ejecución de la interfaz de consola

Para ejecutar la interfaz de consola, ubicarse desde la terminal en la carpeta principal del proyecto y ejecutar:

```bash
python -m src.view.console.consola
```

La aplicación solicitará los siguientes datos:

- Salario básico.
- Días trabajados.
- Bonificación.
- Comisión.
- Otros descuentos.

Después de ingresar los datos, el programa calculará y mostrará el neto a pagar.

### Ejemplo de ejecución de consola

```text
=== LIQUIDADOR DE NÓMINA ===
Ingrese el salario básico: 3000000
Ingrese los días trabajados: 30
Ingrese la bonificación: 0
Ingrese la comisión: 0
Ingrese otros descuentos: 0

=== RESULTADO ===
Neto a pagar: $2,760,000.00
```

## Ejecución de la interfaz gráfica (GUI)

### Requisitos previos

Asegúrate de tener Kivy instalado:

```bash
pip install kivy
```

### Ejecutar la GUI

Desde la terminal en la carpeta principal del proyecto, ejecuta:

```bash
python -m src.view.GUI.liquidador_gui
```

Alternativamente, si estás en la carpeta `src/view/GUI`, puedes ejecutar directamente:

```bash
python liquidador_gui.py
```

### Interfaz de la GUI

La interfaz gráfica proporciona:

- **Campos de entrada** claramente etiquetados para cada dato.
- **Botón "Calcular"** para realizar el cálculo.
- **Mostrar resultado** con el neto a pagar.
- **Manejo de errores** con ventanas emergentes (popup) informativas.
- **Validación de datos** antes de procesar el cálculo.

## Estructura del flujo de datos

```
Entrada de datos (Consola o GUI)
         ↓
   Validación (ValidadorNomina)
         ↓
   Cálculo (calcular_nomina)
         ↓
   Resultado (neto a pagar)
```


