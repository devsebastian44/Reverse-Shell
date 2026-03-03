# 🛡️ Reverse Shell & DevSecOps Strategy

Este repositorio contiene una implementación educativa de una **Reverse Shell** multiplataforma (Windows/Linux) y ejemplifica un ciclo de vida **DevSecOps** profesional, con separación estructurada entre un laboratorio de desarrollo (GitLab) y un entorno de exhibición pública (GitHub).

---

## 🎯 Arquitectura DevSecOps (GitLab ➔ GitHub)

Este proyecto está diseñado bajo un modelo de **Seguridad por Diseño (Security by Design)**.
La fuente de verdad (Source of Truth) reside en un entorno de laboratorio privado (**GitLab**), que incluye los componentes críticos: automatización de CI/CD, pruebas de seguridad estáticas (SAST) y scripts de despliegue.

### El flujo de publicación controlada

Para garantizar que el código ofensivo y los componentes privados de automatización no queden expuestos de manera inadecuada, el proyecto emplea el script **`scripts/publish_public.ps1`**.

1. **Desarrollo en main (GitLab):** El desarrollo, refactorización y battery tests ocurren en el lab privado.
2. **Validación CI/CD:** `.gitlab-ci.yml` ejecuta linter (*flake8*, *shellcheck*) y análisis SAST (*bandit*).
3. **Despliegue Sanitizado:** `publish_public.ps1` crea una rama efímera `public`, retira el código fuente conflictivo (`src/`), configuraciones locales y CI de GitLab, y realiza un **push forzado** a GitHub.
4. **Resultado:** En GitHub, el repositorio actúa de portafolio limpio (diagramas, docs, README) mitigando riesgos éticos o baneos por políticas de la plataforma.

---

## 📂 Estructura del Proyecto

El proyecto está organizado profesionalmente para su escalabilidad:

```text
Reverse-Shell/
├── src/               # Código fuente (payloads operativos - Oculto en GitHub)
│   ├── shell.py       # Script de reverse shell en Python (Windows)
│   ├── shell.sh       # Script de bash (Linux)
├── scripts/           # Automatización y flujos de trabajo DevSecOps
│   ├── config.sh              # Configuración de dependencias (pyinstaller)
│   ├── publish_public.ps1     # Script de sanitización y despliegue a GitHub
├── configs/           # Plantillas y configuraciones de infra (Oculto en GitHub)
├── tests/             # Batería de pruebas automatizadas (Oculto en GitHub)
├── docs/              # Documentación técnica, manuales y pseudocódigo
├── diagrams/          # Diagramas de arquitectura de red y despliegue
├── .gitlab-ci.yml     # Pipeline de DevSecOps Lab (Oculto en GitHub)
└── .gitignore         # Control estricto de exclusión de artefactos y secretos
```

*(Nota: En el repositorio público de GitHub, varias de estas carpetas son excluidas interactivamente para cumplir el proceso de sanitización).*

---

## 🚀 Requisitos e Instalación

> **NOTA:** Las instrucciones siguientes asumen acceso al laboratorio en GitLab, dado que en GitHub el código puede estar total o parcialmente restringido.

* **Requisitos:** Linux (Kali/Ubuntu) para oyente, Python 3.8+, y/o Visual Studio Code.
* **Componentes:** Netcat para escuchar la conexión reversa.

```bash
# Clonado de repositorio (Asegurarse de tener acceso al Lab)
git clone <URL_DEL_REPOSITORIO>
cd Reverse-Shell

# Configuración inicial y requisitos de compilación de payloads
sudo bash scripts/config.sh
```

---

## ▶️ Uso de Ejemplos en el Laboratorio

> **Advertencia de Seguridad:** Asegúrate de ejecutar esto en máquinas virtuales aisladas controladas.

1. Configura la IP del atacante en los payloads ubicados en `src/shell.py` (Windows) o `src/shell.sh` (Linux).

<p align="center">
  <img src="./Img/config2.png" alt="Configuración de IP">
</p>

2. Localmente (Máquina atacante Linux), ponte a la escucha con Netcat:
```bash
nc -lvnp 4444
```

---

## ⚠️ Declaración Ética y Legal (Disclaimer)

Este proyecto, sus scripts y su arquitectura han sido desarrollados **exclusivamente con fines educativos y de investigación en ciberseguridad** (Red Teaming, Malware Research y DevSecOps). 
Queda estrictamente prohibido el uso de este material para atacar infraestructuras sin el consentimiento expreso y por escrito de sus propietarios. El creador y los colaboradores no se hacen responsables del uso indebido ni de los daños ocasionados por la ejecución de los binarios o código proporcionado.
