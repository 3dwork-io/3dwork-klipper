# Layout `configuration/` (nuevo, en migración)

Este árbol reorganiza el repo (todo bajo `configuration/`) y añade configs de
impresora que no estaban en la raíz (v-core-*, tamaños de cama 200-500...).

Estado: **commitado como WIP para no perder el trabajo**, todavía NO es el
layout activo. Lo activo sigue siendo el de la raíz (`macros/`, `boards/`,
`z-probe/`...), que es lo que incluyen los templates, la udev, los scripts y
el wizard. Antes de cambiar el orden de instalación hay que migrar todas esas
referencias (ver ticket 3DWO-468).

Los fixes de la revisión de nov-2026 se aplicaron aquí y en la raíz, así que
los dos árboles están al día en lo arreglado.
