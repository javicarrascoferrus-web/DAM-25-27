El objetivo es practicar el flujo básico de Git: clonar un repositorio, editar un archivo, guardar cambios con commit, subirlos  y traer actualizaciones remotas.

**Las herramientas que vamos a utilizar son:**

GitHub Desktop para clonar y visualizar cambios de forma gráfica.

Git (línea de comandos) para ejecutar commit, push, fetch, pull con los comandos que te piden.

**Clonar el repositorio (GitHub Desktop)**

Abre GitHub Desktop.

Ve a File → Clone repository….

En URL, pega la dirección del repo que te pasó el profesor.

Elige una carpeta local donde guardarlo → Clone.

Verás el repositorio listado en la barra izquierda de GitHub Desktop.


**Hacer commit (desde la terminal como pide el enunciado)**

Abre una terminal en la carpeta del repo (desde GitHub Desktop puedes hacer Repository < Open in Terminal):

En el terminal tecleamos lo siguiente:

git status
git add "segund version.py"
git commit -m "Cambio en el archivo segund version.py"


**Subir cambios (push) a GitHub**
git push origin main


**Fetch y Pull (traer cambios remotos)**

Primero consulto si hay novedades en el servidor:

git fetch origin


Después actualizo mi rama local con lo que haya en remoto:

git pull origin main


Con estos pasos completé el ciclo básico de trabajo con Git y GitHub: clonar → editar → commit → push → fetch/pull. Este flujo garantiza que mis cambios queden bien documentados y que mi copia local esté sincronizada con la versión remota, evitando sobrescribir el trabajo de compañeros.
