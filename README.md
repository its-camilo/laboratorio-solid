# Laboratorio SOLID — SOLID Race Lab

Taller práctico de los principios SOLID para **Ingeniería de Software II** (Universidad Nacional de Colombia, 2026-2). Se completa código real de una carrera de vehículos animada en consola; cada ejercicio se valida con pytest y se puede ver correr en la terminal.

**Objetivo:** reconocer una violación de cada principio SOLID en código existente, explicar por qué es un problema y refactorizar/extender el código para corregirla, manteniendo el programa funcionando.

## Instalación

Requiere Python 3.9+.

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Cómo trabajar cada ejercicio

1. Abre el archivo en `exercises/` y lee su docstring (problema + tareas numeradas; los `TODO(...)` marcan dónde completar).
2. Completa los TODO directamente en ese archivo. **No modifiques `engine/track.py`.**
3. Corre la demo visual: `python -m exercises.exN_xxx`
4. Corre las pruebas: `pytest tests/test_exN_xxx.py -v`

Un ejercicio está terminado cuando sus pruebas pasan **y** la demo corre sin errores ni comportamiento inesperado (sin excepciones, ningún vehículo retrocede).

## Qué hay que hacer

| # | Principio | Archivo | Tarea |
|---|-----------|---------|-------|
| 1 | SRP | `exercises/ex1_srp.py` | Dejar `Car` solo con estado y movimiento. Crear `RaceLogger` (`record(tick, racers)`, `save(path)`, `entries`). Pasar `logger.record` como `on_tick` a `Track.run(...)` y llamar `logger.save()` al final. |
| 2 | OCP | `exercises/ex2_ocp.py` | Implementar `Motorcycle.move()` (paso notablemente variable, rápido pero errático) y `Bicycle.move()` (paso que decrece con el cansancio, nunca menor a 1), sin editar `Vehicle`, `Car`, `Truck` ni `Track`. |
| 3 | LSP | `exercises/ex3_lsp.py` | Rediseñar `UnreliableCar.move()` para respetar el contrato de `Vehicle` (nunca disminuye la posición, nunca lanza excepción), p. ej. no avanzando en algunos ticks. No tocar `Vehicle` ni `Track`. |
| 4 | ISP | `exercises/ex4_isp.py` | Reemplazar `VehicleActions` por `Movable`, `Refuelable`, `Flyable`, `Pedalable`. `GasCar` = Movable + Refuelable; `Bicycle` = Movable + Pedalable; borrar sus stubs. Agregar `Drone` (Movable + Flyable) a la carrera en `main()`. |
| 5 | DIP | `exercises/ex5_dip.py` | `Race` recibe sus corredores (y opcionalmente un `Track`) por constructor, guardados en `self.racers`, sin importar clases concretas. Agregar `RocketSled`. En `main()`, correr dos rosters distintos con la misma `Race`. |

### Preguntas de discusión (en grupo)

1. **SRP:** ¿Por qué es mejor que `Car` no sepa de logging ni impresión? ¿Qué se rompería primero si pidieran el log en JSON?
2. **OCP:** Si quisiste editar `Vehicle` o `Track` para terminar, ¿qué dice eso de tu diseño?
3. **LSP:** ¿Qué habría que añadir a `Track` (try/except, clamping) si no arreglaras `UnreliableCar`? ¿Por qué es mejor arreglar la subclase?
4. **ISP:** ¿Qué interfaces necesitaría un futuro `Submarine` o `Airplane`? ¿Obliga a tocar vehículos existentes?
5. **DIP:** ¿Cómo facilita inyectar el roster probar `Race` sin animación real en terminal?

## Listado de entregables

- [x] **Ex1 — SRP:** `exercises/ex1_srp.py` completo; `pytest tests/test_ex1_srp.py` en verde; demo corre y genera el log vía `RaceLogger`.
- [ ] **Ex2 — OCP:** `exercises/ex2_ocp.py` completo (`Motorcycle`, `Bicycle`); tests en verde; demo sin errores; sin cambios en `Vehicle`/`Car`/`Truck`/`Track`.
- [ ] **Ex3 — LSP:** `exercises/ex3_lsp.py` completo; tests en verde; ningún vehículo retrocede ni lanza excepción.
- [ ] **Ex4 — ISP:** `exercises/ex4_isp.py` completo (4 interfaces, `GasCar`, `Bicycle`, `Drone` en la carrera); tests en verde.
- [ ] **Ex5 — DIP:** `exercises/ex5_dip.py` completo (`Race` inyectada, `RocketSled`, dos rosters en `main()`); tests en verde.
- [ ] **Suite completa:** `pytest -v` con los 5 ejercicios en verde, y `engine/track.py` sin modificar.
- [ ] **Respuestas a las preguntas de discusión** de cada ejercicio (en grupo).
- [ ] **Cierre (wrap-up):** identificar un lugar de tu proyecto del curso (o uno pasado) donde se viole uno de los cinco principios y describir qué cambiarías.

> Confirma con el profesor el formato y medio de entrega de las respuestas escritas y del wrap-up.

## Estructura del repositorio

```
engine/       Motor de animación (completo, no modificar)
exercises/    Los 5 ejercicios (aquí se trabaja)
tests/        Pruebas automáticas por ejercicio
docs/         Enunciado y material de estudio (PDF)
AGENTS.md     Guía para agentes de IA que trabajen en este repo
```

## Material de apoyo

- `docs/Taller-SOLID-Enunciado.pdf` y `docs/SOLID Race Lab.pdf` — enunciado del taller.
- `docs/Material-Estudio-SOLID.pdf` y `docs/SOLID Study Guide.pdf` — repaso teórico con ejemplos de este mismo proyecto.
