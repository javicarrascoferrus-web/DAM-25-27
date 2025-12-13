En una lista de artículos almacenados en una base de datos, el orden de presentación suele controlarse con la cláusula ORDER BY de SQL. Si antes se mostraban “por fecha inversa” (DESC), para que aparezcan en orden cronológico directo basta con ordenar por la fecha ascendente (ASC).

**Cambio en SQL:**

**Antes:** ORDER BY fecha DESC (más nuevo < más viejo).

**Ahora:** ORDER BY fecha ASC (más viejo < más nuevo).

Función raiz (suposición típica): abre conexión SQLite, ejecuta la consulta, y construye un HTML sencillo.

CSS añadido: tipografía básica, ancho máximo legible, tarjetas con sombra ligera, fecha en estilo sutil y un hover suave.


Voy a realizar una serie de comandos para dar ejemplo a estas funciones.


**Código:**

## articulos por fecha inversa.py
**Versión adaptada: posts en orden cronológico directo + estilos CSS añadidos**

import sqlite3
from pathlib import Path

DB_PATH = Path("blog.db")  # ajusta si tu BD tiene otro nombre/ruta

def raiz():
    # 1) Conexión a la BD
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
		

**CONSULTA: orden cronológico directo (ASC)**
    #    Si antes estaba DESC, lo cambiamos a ASC:
    cur.execute("""
        SELECT id, titulo, contenido, fecha
        FROM posts
        ORDER BY fecha ASC
    """)

    posts = cur.fetchall()
    con.close()
		
		
**Estilos CSS adicionales (presentación mejorada)**
    estilos = """
    <style>
      :root { --fg:#1f2937; --muted:#6b7280; --bg:#f8fafc; --card:#ffffff; --accent:#3b82f6; }
      * { box-sizing: border-box; }
      body { margin:0; padding:2rem; font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
             color:var(--fg); background:var(--bg); }
      .wrap { max-width: 820px; margin: 0 auto; }
      h1 { font-size: 1.75rem; margin: 0 0 1rem 0; }
      .sub { color: var(--muted); margin-bottom: 1.25rem; }
      .grid { display: grid; gap: 1rem; }
      .card {
        background: var(--card);
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 1rem 1.25rem;
        box-shadow: 0 1px 0 rgba(0,0,0,0.04);
        transition: transform .1s ease, box-shadow .2s ease, border-color .2s ease;
      }
      .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        border-color: #d1d5db;
      }
      .titulo { font-size: 1.1rem; margin: 0 0 .35rem 0; }
      .fecha { font-size: .9rem; color: var(--muted); margin-bottom: .5rem; }
      .contenido { line-height: 1.6; }
      .badge {
        display: inline-block; font-size: .75rem; color: #fff; background: var(--accent);
        padding: .15rem .5rem; border-radius: 999px; margin-left: .5rem;
      }
    </style>
		
	
	
**Construcción del HTML sencillo**

    html = [f"<!doctype html><html><head><meta charset='utf-8'>{estilos}</head><body>"]
    html.append("<div class='wrap'>")
    html.append("<h1>Artículos</h1>")
    html.append("<div class='sub'>Orden cronológico: del más antiguo al más reciente<span class='badge'>ASC</span></div>")
    html.append("<div class='grid'>")

    for _id, titulo, contenido, fecha in posts:
        html.append("<article class='card'>")
        html.append(f"<h2 class='titulo'>{escape_html(titulo)}</h2>")
        html.append(f"<div class='fecha'>Publicado: {escape_html(str(fecha))}</div>")
        html.append(f"<div class='contenido'>{escape_html(contenido)}</div>")
        html.append("</article>")

    html.append("</div></div></body></html>")
    return "".join(html)

def escape_html(s: str) -> str:
    return (s or "").replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")

Cambiar de orden inverso a cronológico directo solo requiere ajustar ORDER BY fecha ASC. Con un CSS mínimo, la lectura de artículos mejora bastante.
