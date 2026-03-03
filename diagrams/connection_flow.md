# Flujo de Conexión (Reverse Shell)

A continuación, se detalla el diagrama de secuencia que explica gráficamente cómo opera este Comando y Control (C2) de manera que se evada el bloqueo de tráfico de entrada comúnmente aplicado por firewalls perimetrales y puertas de enlace NAT.

```mermaid
sequenceDiagram
    participant Attacker as Attacker Machine (C2)
    participant Victim as Victim Machine (Target)

    note over Attacker: Netcat Escuchando (Puerto 4444)
    Victim->>Attacker: Inicia Conexión Reverse Shell
    activate Attacker
    Attacker-->>Victim: [ACK] Sesión Establecida (Túnel)
    Attacker->>Victim: Envía Comando (ej: 'whoami')
    activate Victim
    Victim-->>Attacker: Ejecuta y Retorna STDOUT/STDERR
    deactivate Victim
    deactivate Attacker
```
