# Reverse-Shell

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-Automation-5391FE?style=flat&logo=powershell&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab_CI-DevSecOps-FC6D26?style=flat&logo=gitlab&logoColor=white)
![Bandit](https://img.shields.io/badge/SAST-Bandit-critical?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-GPL--3.0-red?style=flat&logo=gnu&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-0078D6?style=flat&logo=windows&logoColor=white)

---

## 🧠 Overview

Este proyecto implementa una **Reverse Shell multiplataforma** (Windows 10 y Linux) desarrollada en Python 3.9+, orientada a entornos de **laboratorio de ciberseguridad**, Red Teaming y análisis de seguridad ofensiva. La herramienta establece un canal de comunicación TCP inverso entre una máquina víctima y un atacante controlado, permitiendo la ejecución remota de comandos desde el host oyente.

El proyecto se rige por una **estrategia DevSecOps dual**: el código operativo completo reside en un laboratorio GitLab (fuente de la verdad), mientras que GitHub actúa como portafolio arquitectónico sanitizado. La transición entre entornos está gobernada por un script PowerShell automatizado (`publish_public.ps1`) que elimina artefactos sensibles antes de cualquier publicación pública.

> ⚠️ **Uso Responsable:** Este proyecto es exclusivamente para fines educativos, investigación y laboratorios controlados. Su ejecución en sistemas sin autorización explícita del propietario es ilegal.

---

## ⚙️ Features

- **Reverse Shell TCP** implementada en Python mediante los módulos `socket` y `subprocess`, con soporte para comunicación bidireccional entre cliente y listener
- **Soporte multiplataforma**: payloads funcionales tanto para Windows 10 (scripts Batch/PowerShell) como para entornos Linux (Bash/Shell)
- **Pipeline CI/CD de seguridad** en GitLab con etapas de linting (`flake8`, `shellcheck`), pruebas funcionales (`pytest`) y análisis estático de seguridad (`bandit`)
- **Script de publicación sanitizada** (`publish_public.ps1`) que genera ramas efímeras, expurga código ofensivo y sincroniza únicamente artefactos seguros hacia GitHub
- **Suite de pruebas automatizadas** en `tests/` basada en `pytest` para verificar el comportamiento funcional de los módulos Python
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
| Análisis estático (SAST) | Bandit | Detección de vulnerabilidades en código Python |
| Linting Python | Flake8 | Verificación de estilo y errores sintácticos |
| Linting Shell | Shellcheck | Análisis estático de scripts Bash |
| Testing | Pytest | Suite de pruebas funcionales automatizadas |
| CI/CD | GitLab CI (`.gitlab-ci.yml`) | Pipeline de integración continua y validación |
| Control de versiones | Git (GitHub + GitLab) | Gestión de fuente con estrategia dual-repo |

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

### Clonar el repositorio completo (desde GitLab)

```bash
git clone https://gitlab.com/group-cybersecurity-lab/Reverse-Shell.git
cd Reverse-Shell
```

### Configurar el entorno

```bash
# Configuración inicial del entorno (Linux)
sudo bash scripts/config.sh

# Instalar dependencias Python para pruebas y análisis
pip install -r requirements.txt   # si existe en el entorno GitLab
```

### Instalar herramientas de análisis (opcional, para CI local)

```bash
pip install flake8 bandit pytest
apt install shellcheck   # Debian/Ubuntu
```

---

## ▶️ Usage

### 1. Iniciar el listener en la máquina atacante

```bash
# Escucha en todas las interfaces, puerto 4444, modo verboso
nc -lvnp 4444
```

### 2. Ejecutar el payload en la máquina víctima

**Opción A — Python (Windows/Linux):**
```bash
python3 src/reverse_shell.py
```

**Opción B — Batch script (Windows 10):**
```cmd
shell.bat
```

### 3. Verificar la conexión

Una vez que el payload se ejecuta en la víctima, la máquina atacante recibe una shell interactiva. Los comandos se ejecutan remotamente en el sistema objetivo y la salida se devuelve al listener.

### Ejecutar el pipeline de seguridad localmente

```bash
# Linting Python
flake8 src/

# Análisis estático de seguridad
bandit -r src/

# Linting de scripts Bash
shellcheck scripts/*.sh

# Suite de pruebas
pytest tests/ -v
```

### Publicar versión sanitizada a GitHub

```powershell
# Desde PowerShell en el entorno GitLab
.\scripts\publish_public.ps1
```

> Este script genera una rama temporal, elimina `src/`, `tests/`, `scripts/` y `.gitlab-ci.yml`, y realiza un push forzado hacia GitHub con solo la arquitectura documental.

---

## 📁 Project Structure

```
Reverse-Shell/
│
├── src/                        # Payloads operativos (solo en GitLab)
│   └── reverse_shell.py        # Implementación Python de la reverse shell (socket + subprocess)
│
├── scripts/                    # Automatización DevSecOps (solo en GitLab)
│   ├── publish_public.ps1      # Script PowerShell de publicación sanitizada a GitHub
│   └── config.sh               # Script Bash de configuración del entorno listener
│
├── configs/                    # Plantillas de configuración de infraestructura (solo en GitLab)
│   └── *.conf / *.env          # Variables de entorno y parámetros de red
│
├── tests/                      # Suite de pruebas automatizadas con pytest (solo en GitLab)
│   └── test_*.py               # Pruebas funcionales de los módulos Python
│
├── docs/                       # Documentación técnica y pseudocódigo
│   └── *.md                    # Manuales de arquitectura e instrucciones de laboratorio
│
├── diagrams/                   # Diagramas de flujo y topología de red en Markdown
│   └── *.md                    # Representaciones de arquitectura de conexión TCP inversa
│
├── .gitlab-ci.yml              # Pipeline CI/CD (linting + SAST + tests) — solo en GitLab
├── .gitignore                  # Exclusión de binarios, secretos y artefactos locales
├── LICENSE                     # GNU General Public License v3.0
└── README.md                   # Documentación pública del portafolio
```

> **Nota:** Los directorios `src/`, `scripts/`, `configs/`, `tests/` y el archivo `.gitlab-ci.yml` están presentes únicamente en el repositorio GitLab. El repositorio GitHub contiene exclusivamente `docs/`, `diagrams/`, `.gitignore`, `LICENSE` y `README.md` como portafolio arquitectónico sanitizado.

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

Este proyecto sigue una arquitectura distribuida de doble repositorio orientada a DevSecOps:

- **GitHub** → Portafolio público: documentación arquitectónica, diagramas y presentación profesional (sin código operativo)
- **GitLab** → Laboratorio educativo completo: implementación funcional, pipeline CI/CD, tests y automatización

```
GitLab (Fuente de la Verdad)          GitHub (Portafolio Público)
┌─────────────────────────┐           ┌──────────────────────────┐
│ src/     → Payloads     │           │ docs/    → Documentación │
│ scripts/ → Automatiz.   │──push──►  │ diagrams/→ Arquitectura  │
│ tests/   → pytest       │ sanitiz.  │ LICENSE  → GPL-3.0       │
│ .gitlab-ci.yml → CI/CD  │           │ README.md                │
└─────────────────────────┘           └──────────────────────────┘
         ▲
    publish_public.ps1
    (rama efímera + expurgo)
```

### 🔗 Full Source Code

👉 Código operativo completo disponible en GitLab: [https://gitlab.com/group-cybersecurity-lab/Reverse-Shell](https://gitlab.com/group-cybersecurity-lab/Reverse-Shell)

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

## 👨‍💻 Author

**Sebastian** — [`@devsebastian44`](https://github.com/devsebastian44)

Desarrollador e investigador en ciberseguridad con enfoque en Red Teaming, automatización de pipelines DevSecOps y técnicas de análisis ofensivo en entornos controlados.

| Plataforma | Enlace |
|---|---|
| GitHub | [github.com/devsebastian44](https://github.com/devsebastian44) |
| GitLab | [gitlab.com/group-cybersecurity-lab](https://gitlab.com/group-cybersecurity-lab) |

---

> *Este repositorio es un portafolio educativo. Todo el contenido ha sido diseñado para laboratorios de ciberseguridad en entornos controlados y con fines de investigación responsable.*