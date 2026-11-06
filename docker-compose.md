# 3Dwork Klipper Wizard - Entorno de Testing con Docker

Este docker-compose levanta un entorno completo de Klipper para testing del wizard:
- Klipper + Moonraker (simulado)
- Mainsail (interfaz web)
- Webcam dummy (stream simulado)

## Archivos necesarios

### docker-compose.yml

```yaml
version: '3.8'

services:
  # Klipper Virtual Printer (simulado)
  klipper:
    image: ghcr.io/mainsail-crew/virtual-klipper-printer:latest
    container_name: 3dwork-klipper
    ports:
      - "7125:7125"    # Moonraker API
      - "8110:8110"    # Webcam stream
    volumes:
      - ./klipper_config:/home/klipper/klipper_config
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:7125/server/info"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Mainsail Web UI
  mainsail:
    image: ghcr.io/mainsail-crew/mainsail:latest
    container_name: 3dwork-mainsail
    ports:
      - "80:80"        # Mainsail web
    volumes:
      - ./mainsail_config:/data
    environment:
      - KLIPPER_HOST=klipper
      - KLIPPER_PORT=7125
    restart: unless-stopped
    depends_on:
      - klipper

networks:
  default:
    name: 3dwork-klipper-net
```

## Instrucciones de instalación

### 1. Crear directorio para el entorno

```bash
mkdir -p ~/3dwork-klipper-test
cd ~/3dwork-klipper-test
```

### 2. Crear el archivo docker-compose.yml

Guarda el contenido de arriba como `docker-compose.yml`

### 3. Crear directorios de configuración

```bash
mkdir -p klipper_config mainsail_config
```

### 4. Iniciar los contenedores

```bash
docker compose up -d
```

### 5. Verificar que todo funciona

```bash
# Ver estado de contenedores
docker ps

# Ver logs de Klipper
docker logs 3dwork-klipper

# Ver logs de Mainsail
docker logs 3dwork-mainsail
```

## Acceso a los servicios

| Servicio | URL | Descripción |
|----------|-----|-------------|
| **Mainsail** | http://localhost:80 | Interfaz web de Klipper |
| **Moonraker API** | http://localhost:7125 | API REST de Klipper |
| **Webcam Stream** | http://localhost:8110/?action=stream | Stream simulado |

## Configuración del Wizard

Para conectar el 3Dwork Klipper Wizard:

1. **Moonraker URL**: `http://localhost:7125`
2. **WebSocket**: `ws://localhost:7125/websocket`

## Comandos útiles

```bash
# Reiniciar Klipper
docker restart 3dwork-klipper

# Ver logs en tiempo real
docker logs -f 3dwork-klipper

# Detener el entorno
docker compose down

# Eliminar todo (cuidado, borra datos)
docker compose down -v
```

## Notas

- El printer virtual simula una impresora real con todos los endpoints de API
- La webcam dummy always returns una imagen estática
- Moonraker está pre-configurado para aceptar conexiones de Mainsail
- No es una impresora real, pero permite testear toda la API de Klipper

## Para desarrollo del wizard

Para testear el wizard contra este entorno:

```python
# Ejemplo de conexión desde Python
import moonraker

klipper = moonraker.connect(
    host="localhost",
    port=7125
)

# Obtener estado del printer
status = klipper.get_printer_status()
print(status)
```
