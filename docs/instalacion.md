# 🚀 Instalación

## Requisitos Previos

- Raspberry Pi (o cualquier ordenador con Linux)
- Python 3.8 o superior
- Git
- Conexión a internet

## Opción 1: Un Comando (Recomendado)

Conecta a tu Raspberry por SSH y ejecuta:

```bash
bash <(curl -s https://raw.githubusercontent.com/3dwork-io/3dwork-klipper/dev/install.sh)
```

Esto installará automáticamente:
- El repositorio 3dwork-klipper
- El wizard y todas sus dependencias

## Opción 2: Instalación Manual

```bash
# Conectar por SSH
ssh pi@192.168.X.X

# Ir al directorio de configuración
cd ~/printer_data/config

# Clonar el repositorio
git clone -b dev https://github.com/3dwork-io/3dwork-klipper.git
```

## Instalar Flask (para Web Wizard)

```bash
pip3 install flask
```

## Verificar la Instalación

```bash
# Probar CLI
python3 ~/printer_data/config/3dwork-klipper/wizard/cli.py

# O web
python3 ~/printer_data/config/3dwork-klipper/wizard/web/app.py
```

## Actualizar el Wizard

```bash
cd ~/printer_data/config/3dwork-klipper
git pull origin dev
```

!!! warning "Rama dev"
    Esta documentación corresponde a la rama `dev` que está en desarrollo activo. Para uso estable, usa la rama `master`.