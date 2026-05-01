# Arquitectura del Reverse Shell

El diseño de esta herramienta sigue una estrategia estándar de Comando y Control (C2) simplificada para demostración académica.

## Componentes

1. **Payload (Víctima):**
   - El código fuente reside en la carpeta `src/`.
   - El código principal reside en `src/reverse_shell.py`. Este payload es multiplataforma y está diseñado para establecer conexiones inversas desde sistemas Windows o Linux.
   - El objetivo del payload es evadir la detección inicial de consola (`hide_console_window` en Win32) y redirigir silenciosamente el `stdin`/`stdout`/`stderr` de una terminal local hacia un socket remoto.

2. **Listener (Atacante):**
   - El puerto por defecto establecido en los payloads es `4444`.
   - Se utiliza generalmente `netcat` (`nc -lvnp 4444`) como socket primario para interactuar con la shell.

## Flujo de Conexión (diagrams/connection_flow.mermaid)

Una Reverse Shell se diferencia de una Bind Shell en que es la **víctima** quien inicia proactivamente la conexión hacia el **atacante**. Esto sortea muchas de las barreras de Firewalls tradicionales (NAT), ya que el tráfico de salida (Egress) raramente se bloquea con la misma intensidad que el tráfico entrante (Ingress).

## Consideraciones de Seguridad

Para protección profesional, los payloads y toda la infraestructura de configuración se gestionan siguiendo principios de DevSecOps, utilizando análisis estático (SAST) y pruebas automatizadas para garantizar la integridad del código antes de su despliegue.
