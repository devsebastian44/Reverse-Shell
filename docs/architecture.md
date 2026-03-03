# Arquitectura del Reverse Shell

El diseño de esta herramienta sigue una estrategia estándar de Comando y Control (C2) simplificada para demostración académica.

## Componentes

1. **Payload (Víctima):**
   - El código fuente reside en la carpeta `src/`.
   - Existen dos variantes: `shell.py` (diseñado para máquinas Windows) y `shell.sh` (diseñando para ataques a sistemas Unix/Linux).
   - El objetivo del payload es evadir la detección inicial de consola (`hide_console_window` en Win32) y redirigir silenciosamente el `stdin`/`stdout`/`stderr` de una terminal local hacia un socket remoto.

2. **Listener (Atacante):**
   - El puerto por defecto establecido en los payloads es `4444`.
   - Se utiliza generalmente `netcat` (`nc -lvnp 4444`) como socket primario para interactuar con la shell.

## Flujo de Conexión (diagrams/connection_flow.md)

Una Reverse Shell se diferencia de una Bind Shell en que es la **víctima** quien inicia proactivamente la conexión hacia el **atacante**. Esto sortea muchas de las barreras de Firewalls tradicionales (NAT), ya que el tráfico de salida (Egress) raramente se bloquea con la misma intensidad que el tráfico entrante (Ingress).

## Consideraciones DevSecOps

Para protección profesional, los payloads (en la carpeta `src/`) junto con toda la infraestructura de configuración de tests se almacenan y ejecutan exclusivamente desde el repositorio privado (**GitLab**). 

Al liberar en el portafolio de **GitHub**, el script de publicación omite estas carpetas para evitar flags automáticas o el uso malintencionado por terceros.
