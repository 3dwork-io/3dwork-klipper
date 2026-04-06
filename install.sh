#!/bin/bash
#
# 3Dwork Klipper Installer
# One-liner: bash <(curl -s https://raw.githubusercontent.com/3dwork-io/3dwork-klipper/dev/install.sh)
#

set -e

VERSION="1.0.0-dev"
INSTALL_DIR="${HOME}/3dwork-klipper-wizard"
KLIPPER_CONFIG_DIR="${HOME}/printer_data/config"

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[OK]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

banner() {
    echo -e "${GREEN}"
    echo "╔═══════════════════════════════════════════════════════════╗"
    echo "║          3DWORK KLIPPER WIZARD v${VERSION}                      ║"
    echo "║           Asistente de configuración Klipper               ║"
    echo "╚═══════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

check_dependencies() {
    log_info "Verificando dependencias..."
    
    # Verificar git
    if ! command -v git &> /dev/null; then
        log_error "git no está instalado"
        exit 1
    fi
    
    # Verificar Python
    if ! command -v python3 &> /dev/null; then
        log_error "python3 no está instalado"
        exit 1
    fi
    
    log_success "Dependencias verificadas"
}

create_directories() {
    log_info "Creando directorios..."
    
    mkdir -p "${INSTALL_DIR}"
    mkdir -p "${KLIPPER_CONFIG_DIR}/3dwork-klipper"
    
    log_success "Directorios creados"
}

clone_repository() {
    log_info "Clonando repositorio 3dwork-klipper..."
    
    cd "${KLIPPER_CONFIG_DIR}"
    
    if [ -d "3dwork-klipper" ]; then
        log_warn "3dwork-klipper ya existe, actualizando..."
        cd 3dwork-klipper
        git fetch origin
        git checkout dev
        git pull origin dev
    else
        git clone -b dev https://github.com/3dwork-io/3dwork-klipper.git
    fi
    
    log_success "Repositorio clonado"
}

install_wizard() {
    log_info "Instalando wizard..."
    
    # Copiar wizard
    cp -r "${KLIPPER_CONFIG_DIR}/3dwork-klipper/wizard" "${INSTALL_DIR}/" 2>/dev/null || true
    
    # Hacer ejecutable
    chmod +x "${INSTALL_DIR}/wizard/cli.py" 2>/dev/null || true
    
    # Crear alias en .bashrc
    alias_line="alias 3dwork-klipper='python3 ${INSTALL_DIR}/wizard/cli.py'"
    
    if ! grep -q "3dwork-klipper" "${HOME}/.bashrc" 2>/dev/null; then
        echo "" >> "${HOME}/.bashrc"
        echo "# 3Dwork Klipper Wizard" >> "${HOME}/.bashrc"
        echo "${alias_line}" >> "${HOME}/.bashrc"
    fi
    
    log_success "Wizard instalado"
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
    echo "  INSTALACIÓN COMPLETADA"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
    echo ""
    echo "Para usar el wizard, ejecuta:"
    echo "  source ~/.bashrc"
    echo "  3dwork-klipper"
    echo ""
    echo "O directamente:"
    echo "  python3 ${INSTALL_DIR}/wizard/cli.py"
    echo ""
}

main() {
    banner
    check_dependencies
    create_directories
    clone_repository
    install_wizard
}

main "$@"