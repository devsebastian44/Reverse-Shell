# Reverse Shell Repository (Educational Cybersecurity Lab)

<p align="center">
  <img src="docs/Img/Logo.png" height="300px" width="350px" alt="Reverse Shell Logo">
</p>

> **⚠️ DISCLAMER / AVISO ÉTICO**
> Este proyecto ha sido desarrollado estrictamente con fines **educativos y de investigación en ciberseguridad**. Su propósito es demostrar el funcionamiento de las conexiones inversas (Reverse Shells) para entrenar estrategias de defensa y mitigación.
> **El uso indebido de este material en entornos reales o sin autorización puede ser ilegal.** El autor no se responsabiliza del mal uso ni de los daños que puedan ocasionarse derivados del contenido de este repositorio.

Una **reverse shell** es una técnica utilizada en ciberseguridad que permite establecer una conexión entre un activo controlado por un investigador (atacante) y una máquina objetivo, otorgando acceso remoto de forma controlada para ejecutar comandos no interactivos. Este repositorio implementa laboratorios de reverse shell escalables tanto en **Windows** como en **Linux**, adoptando prácticas DevSecOps.

---

## 🏛️ Arquitectura y Estructura del Proyecto

El proyecto está diseñado bajo un enfoque profesional DevSecOps, separando los payloads, las configuraciones y los tests para facilitar su despliegue tanto en un portafolio público como en un laboratorio privado (con pipelines CI/CD).

```text
Reverse-Shell/
├── src/                   # Código de los payloads principales
│   ├── shell.py           # Payload reverse shell en Python (entornos Windows)
│   └── shell.sh           # Payload reverse shell en Bash (entornos Linux)
├── scripts/               # Scripts de automatización y herramientas auxiliares
│   └── config.sh          # Script de configuración inicial para la prueba
├── configs/               # Plantillas de configuración (.example)
│   └── settings.json.example
├── tests/                 # Pruebas automatizadas (simulación de payloads y validación de sintaxis)
│    └── test_payloads.py
├── docs/                  # Documentación técnica e imágenes
│   └── Img/
├── .gitlab-ci.yml         # Pipeline CI/CD para GitLab (Linting + Security Checks)
└── README.md
```

## 📋 Requisitos Previos

- Un entorno de control Linux (Ubuntu / Kali Linux / Parrot OS).
- **Python 3.8+** para ejecución de scripts Python.
- **Netcat (`nc`)** instalado en la máquina observadora.
- Herramientas de DevSecOps (Flake8, ShellCheck, Bandit) para ejecutar los tests locales.

---

## 🚀 Instalación y Despliegue Configurado

Clona el repositorio en tu entorno seguro de laboratorio:

```bash
git clone https://github.com/Devsebastian44/Reverse-Shell.git
cd Reverse-Shell
```

> **Nota:** Para entornos de GitLab, se dispone de un pipeline `.gitlab-ci.yml` automatizado para validar el estilo, y ejecutar verificaciones sintácticas y de seguridad simuladas. 

---

## ▶️ Uso Correcto en un Entorno Aislado

### 1. Escucha en la máquina del investigador (Linux):
Inicie el listener (Netcat) para capturar la conexión inversa:

```bash
nc -lvnp 4444
```

### 2. Configuración y Lanzamiento del Payload:

Debe configurar la IP y Puerto del investigador en el payload correspondiente (ya sea `src/shell.py` para objetivos Windows, o `src/shell.sh` para objetivos Linux).

<p align="center">
  <img src="docs/Img/config2.png" alt="Configuración de Payload">
</p>

Ejecución auxiliar del archivo de configuración inicial en la máquina objetivo:

```bash
sudo chmod +x scripts/config.sh
sudo bash scripts/config.sh
```

---

## 🔒 GitHub vs GitLab Strategy

Este repositorio sigue una estrategia híbrida:
- **GitHub (Público):** Diseñado como portafolio profesional, incluye configuraciones limpias, documentación, y ejemplos educativos con enfoques DevSecOps. (Ciertos tests o exploits funcionales reales pueden ser omitidos en ramas públicas según regulaciones).
- **GitLab (Privado):** Actúa como laboratorio. Contiene las implementaciones completas con pipelines CI/CD automatizados (`.gitlab-ci.yml`) que simulan el paso seguro a producción y el análisis dinámico de comportamiento de cada payload.

---

## 📜 Licencia

Este proyecto está bajo la licencia **MIT**. Puedes usarlo libremente con fines educativos y de investigación, siempre cumpliendo con el descargo de responsabilidad establecido al inicio de este documento.
