# AGENTS.md

Guía para agentes de IA que trabajen en este repositorio (Laboratorio SOLID, Ingeniería de Software II, UNAL 2026-2). Léela completa antes de editar nada.

## Contexto

Taller **evaluable** y pedagógico: el estudiante debe aprender a reconocer y corregir violaciones de SOLID. El repo es Python 3.9+ con pytest. Dominio: carrera de vehículos animada en consola.

- `engine/track.py`: motor de animación. **Completo. NO modificar** (lo exige el enunciado). Define el protocolo `Racer` (`name`, `symbol`, `position`, `move()`) y `Track.run(racers, max_ticks, on_tick)`.
- `exercises/ex1_srp.py` … `ex5_dip.py`: un ejercicio por principio. El docstring de cada archivo explica el problema y las tareas; los `TODO(SRP|OCP|LSP|ISP|DIP)` marcan dónde completar.
- `tests/test_exN_*.py`: pruebas que validan cada ejercicio. `tests/conftest.py` solo ajusta `sys.path`.
- `docs/`: enunciado y guías de estudio en PDF (fuente de verdad de lo que se pide).
- `README.md`: instrucciones y lista de entregables.

## Reglas de trabajo

1. **Fuente de verdad**: `docs/Taller-SOLID-Enunciado.pdf` y `docs/SOLID Race Lab.pdf`, luego el docstring de cada ejercicio. Si algo se contradice, pregunta al usuario.
2. **Edita solo `exercises/`** (y crea archivos de entregables si el usuario lo pide). Nunca `engine/track.py`. No debilites, borres ni modifiques los tests para que pasen.
3. **Restricciones por ejercicio** (se evalúan):
   - Ex1 SRP: `Car` solo guarda estado y se mueve (sin `print` ni escritura de archivos). `RaceLogger` con `record(tick, racers)`, `save(path)`, `entries`. En `main()` pasar `logger.record` como `on_tick` y llamar `logger.save()`.
   - Ex2 OCP: implementar `Motorcycle.move()` (paso variable/errático) y `Bicycle.move()` (paso decreciente, nunca < 1) **sin tocar** `Vehicle`, `Car`, `Truck` ni `Track`.
   - Ex3 LSP: `UnreliableCar.move()` nunca retrocede ni lanza excepción (p. ej. simplemente no avanza en algunos ticks). No tocar `Vehicle` ni `Track`.
   - Ex4 ISP: reemplazar `VehicleActions` por `Movable`, `Refuelable`, `Flyable`, `Pedalable` (un método abstracto cada una). `GasCar` = Movable+Refuelable, `Bicycle` = Movable+Pedalable, nuevo `Drone` = Movable+Flyable (añadido a la carrera en `main()`). Eliminar los métodos stub "no puedo hacer eso".
   - Ex5 DIP: `Race` recibe los corredores (y opcionalmente `Track`) por constructor y los guarda en `self.racers`; no importa ni conoce clases concretas. Añadir `RocketSled`. `main()` corre dos rosters distintos.
4. **Estilo**: nombres y código en inglés (como el material); comentarios y docs en español o inglés, pero consistentes. Type hints donde ya existan. Sin dependencias nuevas salvo pytest.
5. **Eliminar los `TODO(...)`** resueltos; no dejar código muerto ni `pass` de relleno.

## Comandos

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -v                          # toda la suite
pytest tests/test_ex1_srp.py -v    # un ejercicio
python -m exercises.ex1_srp        # demo visual (ex1..ex5)
```

Los demos usan `clear` y `time.sleep`; en entornos sin TTY, puedes validar con pytest y con `Track(animate=False, tick_seconds=0)`. Ejecutar siempre desde la raíz del repo (los imports son `engine.track`, `exercises.*`).

## Antes de dar algo por terminado

- `pytest -v` en verde y cada demo corre sin excepciones ni vehículos retrocediendo.
- `git diff --stat` no muestra cambios en `engine/` ni en `tests/`.
- No se generaron `race_log.txt`, `__pycache__`, `.venv` en commits (están en `.gitignore`).

## Git

Commits pequeños, uno por ejercicio, en imperativo (p. ej. `Solve ex1 SRP: extract RaceLogger`). No reescribir historia ni forzar push. No subir soluciones ajenas ni la rama `solution` del profesor (no forma parte de este repo).

## Enfoque pedagógico

El estudiante debe poder explicar cada cambio. Al ayudar, explica **por qué** la solución respeta el principio y responde las preguntas de discusión de cada ejercicio (están en el enunciado). Si el usuario pide solo la solución, entrégala, pero resume brevemente la violación original y el principio aplicado.
