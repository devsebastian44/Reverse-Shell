# 🛡️ Reverse Shell & DevSecOps Strategy

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![GitLab](https://img.shields.io/badge/GitLab-Repository-orange?logo=gitlab)
![License](https://img.shields.io/badge/License-GPL--3.0-red)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![Pentesting](https://img.shields.io/badge/Type-Pentesting-darkred)
![Warning](https://img.shields.io/badge/⚠-Authorized%20Use%20Only-critical)

Este repositorio contiene una implementación educativa de una **Reverse Shell** multiplataforma (Windows/Linux) y ejemplifica un ciclo de vida **DevSecOps** profesional, con separación estructurada entre un laboratorio de desarrollo (GitLab) y un entorno de exhibición pública (GitHub).

---

## 🎯 Objetivo Técnico y Profesional

El objetivo de este proyecto es dual:
1. Proveer una herramienta funcional para laboratorios de Red Teaming y Pentesting (Reverse Shell).
2. Demostrar una arquitectura **DevSecOps** madura, enfocada en la publicación segura de artefactos sensibles, pipelines CI/CD de análisis de seguridad y código (SAST, Linting) y separación lógica de entornos mediante estrategias de Git.

---

## 🏗️ Arquitectura del Repositorio

El proyecto está organizado profesionalmente para escalar garantizando el menor riesgo operativo:

```text
Reverse-Shell/
├── src/               # Código fuente (Payloads operativos de la reverse shell)
├── scripts/           # Automatización y scripts de DevSecOps (ej. publish_public.ps1)
├── configs/           # Plantillas y configuraciones de infra
├── tests/             # Batería de pruebas automatizadas (Unitarias, funcionales)
├── docs/              # Documentación técnica, manuales de arquitectura y pseudocódigo
├── diagrams/          # Diagramas de arquitectura en Markdown
├── .gitlab-ci.yml     # Pipeline DevSecOps privado
└── .gitignore         # Control estricto de exclusión de artefactos y secretos
```

*(Nota: Ciertas carpetas como `src/`, `tests/`, y configuraciones quedan reservadas exclusivamente para el entorno privado y automatizado).*

---

## 🔒 Flujo DevSecOps: GitLab ➔ GitHub

El proyecto se rige por un pipeline de **Seguridad por Diseño (Security by Design)** que divide el código en dos planos: el Laboratorio Privado (GitLab) como la "Fuente de la Verdad", y el Portafolio Público (GitHub) como presentación sanitizada.

### Script de Publicación: `publish_public.ps1`
Ubicado en la carpeta `scripts/`, este script gestiona la promoción del código hacia plataformas públicas mitigando riesgos éticos y problemas de baneos o exposición de secretos:

1. **Desarrollo en main (GitLab):** El código completo, tests unitarios y la automatización CI residen de forma privada.
2. **Validación CI/CD:** GitLab CI ejecuta linting (*flake8*, *shellcheck*), pruebas en `tests/` con *pytest* y análisis SAST mediante *bandit*.
3. **Despliegue Sanitizado (`publish_public.ps1`):** 
   - Genera una rama intermedia efímera.
   - **Eliminación Intencionada:** Remueve código ofensivo crítico (`src/`), configuraciones locales/sensibles (`configs/`), lógica de despliegue interno (`scripts/`), y los pipelines CI (`.gitlab-ci.yml` y `tests/`).
4. **Push Forzado a GitHub:** La variante segura, conteniendo solo arquitectura, dependencias abstractas, `docs/` y el README, es sincronizada forzosamente.

**Justificación Profesional:** Exhibir código ofensivo completo puede romper políticas de plataformas e incrementar la superficie de ataque accidental. Esta estrategia aísla el conocimiento arquitectónico del ejecutable accionable.

---

## 🚀 Uso e Instalación (Entorno Privado)

> [!IMPORTANT]
> El repositorio completo con todo el código funcional (tests, src, binarios construíbles) está disponible operativamente en **GitLab** para su análisis y ejecución integral.

### Instalación Básica

* **Requisitos (Oyente):** Linux (Kali/Ubuntu), Python 3.9+, Netcat.

```bash
# Acceso exclusivo desde el pipeline / entorno controlado de GitLab
git clone https://gitlab.com/group-cybersecurity-lab/Reverse-Shell.git
cd Reverse-Shell

# Configuración inicial
sudo bash scripts/config.sh
```

### Ejecución de Laboratorio
> **Advertencia:** Ejecutar exclusivamente en máquinas virtuales aisladas.

1. Configurar IP / Puerto del Atacante.
2. Iniciar el listener:
```bash
nc -lvnp 4444
```

---

## ⚠️ Declaración Ética y Legal (Disclaimer)

Este proyecto, sus scripts operativos y su arquitectura han sido desarrollados **exclusivamente con fines educativos y de investigación en ciberseguridad** (Red Teaming, Malware Research y DevSecOps). 
Queda estrictamente prohibido el uso de este material para atacar infraestructuras sin el consentimiento expreso y documentado de sus propietarios. Los autores no asumen responsabilidad frente uso negligente, ilícito o no autorizado de ninguna de las partes del código proporcionadas.
