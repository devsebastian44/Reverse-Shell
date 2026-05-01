# Reverse-Shell

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-Automation-5391FE?style=flat&logo=powershell&logoColor=white)
![Bandit](https://img.shields.io/badge/SAST-Bandit-critical?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-GPL--3.0-red?style=flat&logo=gnu&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=flat&logo=github-actions&logoColor=white)

---

## 🧠 Overview

Este proyecto implementa una **Reverse Shell multiplataforma** (Windows 10 y Linux) desarrollada en Python 3.9+, orientada a entornos de **laboratorio de ciberseguridad**, Red Teaming y análisis de seguridad ofensiva. La herramienta establece un canal de comunicación TCP inverso entre una máquina víctima y un atacante controlado, permitiendo la ejecución remota de comandos desde el host oyente.

El proyecto sigue una **estrategia DevSecOps moderna**, integrando controles de seguridad y calidad directamente en el flujo de desarrollo. GitHub actúa como el repositorio central tanto para el desarrollo como para la presentación profesional.

> [!IMPORTANT]
> **Uso ético:** Este proyecto tiene fines exclusivamente educativos y éticos en materia de ciberseguridad. El uso no autorizado de estas técnicas contra sistemas sin permiso explícito es ilegal y poco ético. El autor no se responsabiliza del mal uso de esta herramienta.

---

## ⚙️ Features

- **Reverse Shell TCP** implementada en Python mediante los módulos `socket` y `subprocess`, con soporte para comunicación bidireccional entre cliente y listener
- **Soporte multiplataforma**: payloads funcionales tanto para Windows 10 (scripts Batch/PowerShell) como para entornos Linux (Bash/Shell)
- **Pipeline CI/CD de seguridad** con etapas de linting (`ruff`, `shellcheck`), validación de secretos, pruebas funcionales (`pytest`) y análisis estático (`bandit`)

- **Documentación técnica estructurada** en `docs/` con pseudocódigo y manuales de arquitectura
- **Diagramas de arquitectura** en formato Markdown dentro de `diagrams/` para representar flujos de conexión y topología de red
- **Control estricto de secretos** mediante `.gitignore` configurado para excluir binarios compilados, configuraciones locales y artefactos de entorno

---

## 🛠️ Tech Stack

| Capa | Tecnología | Propósito |
|---|---|---|
| Lenguaje principal | Python 3.9+ | Implementación del payload y lógica de la reverse shell |
| Scripting Windows | PowerShell (.ps1) | Automatización del flujo de publicación y configuración |
| Scripting Windows (payload) | Batch (.bat) | Ejecución y persistencia del agente en Windows 10 |
| Scripting Linux | Bash (.sh) | Configuración del entorno y listener en sistemas Unix |
| Listener de red | Netcat (`nc`) | Receptor de conexiones inversas TCP |
| Análisis estático (SAST) | Bandit / Detect-Secrets | Detección de vulnerabilidades y secretos en código |
| Linting / Format Python | Ruff | Linter ultrarrápido y formateador de código |
| Linting Shell | Shellcheck | Análisis estático de scripts Bash |
| Testing | Pytest | Suite de pruebas funcionales automatizadas |
| Code Quality | Pre-commit | Pipeline local automático antes de cada commit |
| CI/CD | GitHub Actions | Pipeline de integración continua y validación |
| Control de versiones | Git (GitHub) | Gestión de fuente centralizada |

---

## 📦 Installation

### Requisitos previos

**Máquina atacante / Listener (Linux recomendado: Kali / Ubuntu):**
- Python 3.9 o superior
- Netcat instalado (`ncat` o `nc`)
- Git

**Máquina objetivo (Windows 10):**
- Python 3.9+ (si se ejecuta el payload `.py`)
- O bien solo el intérprete de comandos (`cmd.exe`) si se usa el payload Batch

### Configurar el entorno

1. Clone el repositorio:
   ```bash
   git clone https://github.com/devsebastian44/Reverse-Shell.git
   cd Reverse-Shell
   ```

2. Configure las variables de entorno:
   ```bash
   cp .env.example .env
   # Edite el archivo .env con su LHOST y LPORT
   ```

3. Instale las dependencias:
   ```bash
   pip install .[dev]
   pre-commit install
   ```

---

## ▶️ Usage

### 1. Iniciar el listener
En la máquina atacante, use Netcat o una herramienta similar:
```bash
nc -lvnp 4444
```

### 2. Ejecutar el payload
En la máquina víctima:
```bash
python src/reverse_shell.py
```

### Ejecutar Pruebas y QA
```bash
# Ejecutar tests funcionales (usando mocks)
pytest tests/ -v

# Ejecutar linting y seguridad manual
ruff check .
bandit -r src/
```


---

## 📁 Project Structure

```
Reverse-Shell/
│
├── src/                        # Payloads operativos
│   └── reverse_shell.py        # Implementación Python de la reverse shell (socket + subprocess)
│
├── scripts/                    # Automatización DevSecOps
│   └── config.sh               # Script Bash de configuración del entorno listener
│
├── configs/                    # Plantillas de configuración de infraestructura
│   └── *.conf / *.env          # Variables de entorno y parámetros de red
│
├── tests/                      # Suite de pruebas automatizadas con pytest
│   └── test_*.py               # Pruebas funcionales de los módulos Python
│
├── docs/                       # Documentación técnica y pseudocódigo
│   └── *.md                    # Manuales de arquitectura e instrucciones de laboratorio
│
├── diagrams/                   # Diagramas de flujo y topología de red en Markdown
│   └── *.md                    # Representaciones de arquitectura de conexión TCP inversa
│
├── .github/workflows/          # Pipeline CI/CD (GitHub Actions)
├── .gitignore                  # Exclusión de binarios, secretos y artefactos locales
├── LICENSE                     # GNU General Public License v3.0
└── README.md                   # Documentación principal del proyecto
```


---

## 🔐 Security

### Contexto de uso responsable

Este proyecto implementa técnicas de **acceso remoto no autorizado simulado** con fines exclusivamente educativos. Las mismas técnicas utilizadas en esta herramienta son empleadas por equipos de Red Team para evaluar la postura de seguridad de organizaciones con consentimiento explícito.

### Implicaciones técnicas

- **Vector de ataque:** Conexión TCP inversa iniciada desde la víctima hacia el atacante, eludiendo posibles reglas de firewall que bloqueen conexiones entrantes
- **Módulos Python utilizados:** `socket` (comunicación de red) y `subprocess` (ejecución de comandos en el SO), considerados de alto riesgo en análisis SAST
- **Detección antivirus:** Los payloads Python compilados o los scripts Batch pueden ser detectados por soluciones EDR/AV modernas; su uso en laboratorio aislado es mandatorio
- **Pipeline SAST integrado:** `bandit` analiza automáticamente el código Python en busca de llamadas peligrosas (`subprocess.shell=True`, `exec`, `eval`) antes de cada merge

### Buenas prácticas de laboratorio

- Ejecutar **exclusivamente en máquinas virtuales aisladas** sin conexión a redes de producción
- Utilizar rangos de red privados (`192.168.x.x`, `10.0.x.x`) y entornos como VirtualBox, VMware o redes host-only
- Nunca ejecutar el payload en sistemas de terceros sin **autorización escrita documentada**
- Destruir el entorno de laboratorio tras cada sesión de pruebas

---

## 🌐 Repository Architecture

Este proyecto está centralizado en GitHub, utilizando GitHub Actions para la validación continua y asegurando que tanto la documentación como el código fuente sigan estándares de calidad profesional.

```
          GitHub (Repositorio Central)
          ┌──────────────────────────┐
          │ src/     → Payloads      │
          │ scripts/ → Automatiz.    │
          │ tests/   → pytest        │
          │ .github/ → CI/CD         │
          │ README.md / docs/        │
          └──────────────────────────┘
```
---

## 🚀 Roadmap

- [ ] **Cifrado del canal de comunicación** — Implementar TLS/SSL sobre el socket TCP para evitar inspección de tráfico en red
- [ ] **Soporte para múltiples conexiones simultáneas** — Arquitectura multi-hilo para gestionar sesiones concurrentes desde el listener
- [ ] **Ofuscación del payload** — Técnicas de encoding (base64, XOR) para reducir detección por soluciones AV/EDR
- [ ] **Persistencia automatizada en Windows** — Integración con el registro de Windows o tareas programadas mediante los scripts Batch existentes
- [ ] **Panel de control CLI interactivo** — Interfaz de línea de comandos mejorada para gestión de sesiones en el listener
- [ ] **Dockerización del entorno de laboratorio** — Contenedores Docker para atacante y víctima, facilitando reproducibilidad sin VMs
- [ ] **Cobertura de tests ampliada** — Incrementar el coverage de `pytest` al 80%+ con pruebas de integración de red
- [ ] **Soporte macOS** — Extensión de los payloads para cubrir entornos Darwin/macOS

---

## 📄 License

Este proyecto está licenciado bajo la **GNU General Public License v3.0** (GPL-3.0).

La licencia permite el uso, modificación y distribución del código bajo las mismas condiciones de la GPL-3.0, incluyendo la obligación de mantener el código fuente disponible en cualquier distribución derivada. Cualquier uso de este software en actividades ilícitas o sin autorización del propietario del sistema objetivo queda expresamente prohibido y es responsabilidad exclusiva del usuario.

Consulta el archivo [`LICENSE`](./LICENSE) para los términos completos.

---

## 🤝 Contributing

¡Las contribuciones son bienvenidas! Para colaborar:

1. Realice un **Fork** del proyecto.
2. Cree una rama para su mejora (`git checkout -b feature/AmazingFeature`).
3. Realice sus cambios y haga commit siguiendo los [Conventional Commits](https://www.conventionalcommits.org/).
4. Haga **Push** a su rama (`git push origin feature/AmazingFeature`).
5. Abra un **Pull Request** detallando sus cambios.

---

## 👨‍💻 Author

**Sebastian** — [`@devsebastian44`](https://github.com/devsebastian44)

Desarrollador e investigador en ciberseguridad con enfoque en Red Teaming, automatización de pipelines DevSecOps y técnicas de análisis ofensivo en entornos controlados.

| Plataforma | Enlace |
|---|---|
| GitHub | [github.com/devsebastian44](https://github.com/devsebastian44) |

---

> *Este repositorio es un portafolio educativo. Todo el contenido ha sido diseñado para laboratorios de ciberseguridad en entornos controlados y con fines de investigación responsable.*