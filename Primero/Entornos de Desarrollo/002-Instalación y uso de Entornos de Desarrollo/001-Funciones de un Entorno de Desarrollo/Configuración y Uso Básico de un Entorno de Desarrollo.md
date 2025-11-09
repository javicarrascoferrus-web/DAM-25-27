En esta actividad el objetivo es preparar un entorno de trabajo adecuado para la programación, empezando por la instalación de un Sistema Operativo (SSOO) y una aplicación para editar código.

He elegido Linux (Ubuntu) como sistema operativo porque es gratuito, estable y muy usado en entornos de desarrollo profesional. Además, permite trabajar fácilmente con lenguajes como Python o JavaScript desde la terminal.

**Instalación del sistema operativo (Linux Ubuntu):**

Descargué la imagen ISO de Ubuntu desde su página oficial.

Creé un USB booteable para poder iniciar el sistema desde ahí.

Reinicié el ordenador y accedí al menú de arranque para iniciar desde el USB.

Seguí los pasos del asistente de instalación: elegí el idioma, configuré la red y seleccioné la opción de “instalar junto a otro sistema operativo”.

Finalmente, configuré el usuario, la contraseña y esperé a que finalizara la instalación.

Una vez instalado Ubuntu, abrí la terminal y ejecuté:
sudo apt update
sudo apt install code


Una vez configurado el entorno, creé un archivo de prueba llamado hola.py dentro de una carpeta de trabajo y escribí este código:

nombre = "Javier"
print(f"Hola, {nombre}. ¡Tu entorno de desarrollo está listo!")



Con esta práctica conseguí tener un entorno completo para programar: un sistema operativo Linux, un editor profesional y el intérprete de Python funcionando correctamente.
