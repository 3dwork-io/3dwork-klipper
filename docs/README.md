# 3Dwork Klipper Wizard

## Configuración

### mkdocs.yml

```yaml
site_name: 3Dwork Klipper Wizard
site_description: El asistente más fácil para configurar Klipper
theme:
  name: material
  language: es
```

## Estructura de Documentación

La documentación está organizada para funcionar con GitHub Pages usando MkDocs Material:

```
docs/
├── index.md        # Página principal
├── instalacion.md # Guía de instalación
├── web-wizard.md  # Cómo usar el Web Wizard
├── cli-wizard.md  # Cómo usar el CLI
├── placas.md       # Placas soportadas
└── mkdocs.yml     # Configuración
```

## Generar la Documentación

```bash
pip install mkdocs-material
cd docs
mkdocs serve
```

## Publicar en GitHub Pages

```bash
mkdocs gh-deploy
```

!!! note "Nota"
    Esta documentación está diseñada para usar GitHub Actions y publicarse automáticamente en GitHub Pages.