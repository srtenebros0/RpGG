██████╗ ██████╗  ██████╗  ██████╗ 
██╔══██╗██╔══██╗██╔════╝ ██╔════╝ 
██████╔╝██████╔╝██║  ███╗██║  ███╗
██╔══██╗██╔═══╝ ██║   ██║██║   ██║
██║  ██║██║     ╚██████╔╝╚██████╔╝
╚═╝  ╚═╝╚═╝      ╚═════╝  ╚═════╝ 

🧙‍♂️ RPG de Texto en Python

Un juego RPG basado en consola desarrollado en Python, con arquitectura modular y sistemas escalables como combate, inteligencia artificial de enemigos, estados y efectos.

⸻

📌 Características
	•	⚔️ Sistema de combate por turnos
	•	🤖 IA de enemigos basada en estados (FSM)
	•	📈 Escalado dinámico de enemigos
	•	🧪 Sistema de estados y efectos (veneno, quemadura, etc.)
	•	🧱 Arquitectura modular y mantenible
	•	🧩 Fácil de expandir (habilidades, inventario, historia)

⸻

🧠 Sistema de IA

Los enemigos utilizan una máquina de estados finitos (FSM) para tomar decisiones dinámicas:

Estados disponibles:
	•	AGRESIVO → Ataque constante
	•	DEFENSIVO → Se protege o cura
	•	HUYENDO → Intenta escapar
	•	ENFURECIDO → Aumenta daño cuando tiene poca vida

La IA evalúa condiciones como:
	•	Vida actual
	•	Efectos activos
	•	Estado del jugador

⸻

🧪 Sistema de efectos

Los efectos modifican el comportamiento durante el combate:
	•	☠️ Poison → Daño por turno
	•	🔥 Burn → Daño + reducción de ataque
	•	🛡️ Shield → Reducción de daño recibido

Cada efecto tiene:
	•	Duración
	•	Impacto por turno
	•	Posibles interacciones con la IA

⸻

⚙️ Instalación
	1.	Clona el repositorio:

git clone https://github.com/tu-usuario/rpg-texto.git
cd rpg-texto

	2.	Ejecuta el juego:

python main.py


⸻

🚀 Roadmap
	•	Sistema de combate
	•	Enemigos básicos
	•	Escalado de dificultad
	•	Estados y efectos
	•	IA con estados
	•	Sistema de habilidades
	•	Inventario
	•	Sistema de loot
	•	Historia / narrativa
	•	Guardado de partida

⸻

🧩 Futuras mejoras
	•	Sistema de clases (guerrero, mago, etc.)
	•	Árbol de habilidades
	•	Eventos aleatorios
	•	Interfaz mejorada (colores, UI en consola)

⸻

🤝 Contribuciones

Las contribuciones son bienvenidas. Puedes abrir un issue o enviar un pull request.

⸻

📄 Licencia

Este proyecto está bajo la licencia MIT.

⸻

🧠 Nota del desarrollador

Este proyecto está diseñado no solo como un juego, sino como una base sólida para aprender:
	•	Arquitectura de software
	•	Diseño de sistemas
	•	Lógica de videojuegos

Si lo rompes… es porque ya estás aprendiendo 😉
:::