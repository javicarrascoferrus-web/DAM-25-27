En los simulacros solemos tener programas “todo en uno” donde la lógica está mezclada. Eso hace el código difícil de leer, probar y mantener.
Aquí aplico refactorización por extracción de funciones: separo la lógica en funciones pequeñas con responsabilidad única, además documento con: docstring de módulo, docstrings de función y comentarios de línea donde aportan contexto puntual.

A continuación pondré dos lineas de codigo, una original y la otra refactorizada, para que hayan cambios diferentes:

**Versión original:**


suma = 0
for t in tiempos:
    suma += t
media = suma / len(tiempos)

mejor = tiempos
mejor_idx = 0
i = 0
for t in tiempos:
    if t < mejor:
        mejor = t
        mejor_idx = i
    i += 1

distancia_total_m = 25 * len(tiempos)  # piscina 25m
ritmo_promedio_s_100m = (media * 100) / 25

print("INFORME ENTRENAMIENTO")
print("Vueltas:", len(tiempos))
print("Media (s/vuelta):", round(media, 2))
print("Mejor vuelta:", mejor_idx + 1, "con", mejor, "s")
print("Distancia total (m):", distancia_total_m)
print("Ritmo medio (s/100m):", round(ritmo_promedio_s_100m, 2))


**Versión refactorizada:**


def calcular_media(tiempos):
    """Devuelve la media de los tiempos."""
    return sum(tiempos) / len(tiempos)

def mejor_vuelta(tiempos):
    """Devuelve la mejor vuelta (posición y tiempo)."""
    mejor = min(tiempos)
    vuelta = tiempos.index(mejor) + 1
    return vuelta, mejor

def generar_informe(tiempos):
    """Genera un pequeño informe con los datos del entrenamiento."""
    media = calcular_media(tiempos)
    vuelta, mejor = mejor_vuelta(tiempos)
    print("INFORME DE ENTRENAMIENTO")
    print(f"Vueltas: {len(tiempos)}")
    print(f"Media: {round(media, 2)} s/vuelta")
    print(f"Mejor vuelta: {vuelta} con {mejor} s")

def main():
    """Función principal."""
    generar_informe(tiempos)

if __name__ == "__main__":
    main()

La refactorización por extracción de funciones mejoró:

**Legibilidad:** cada función tiene un nombre y propósito claros.

**Mantenibilidad:** puedo cambiar un cálculo sin tocar el resto.

Este enfoque me permite defender el diseño y argumentar cómo la refactorización reduce errores futuros y acelera cambios
Esto encaja con lo visto en la unidad: responsabilidad única, docstring de módulo y de función, y comentarios donde aportan.
