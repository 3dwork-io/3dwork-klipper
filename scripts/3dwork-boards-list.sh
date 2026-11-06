#!/bin/bash

# Lista las placas disponibles en boards/ como JSON (para el wizard/moonraker).
BOARDS_DIR="${1:-/home/pi/printer_data/config/3dwork-klipper/boards}"
OUT="${2:-/tmp/boards.json}"

json='{"boards":['
first=1
for board in "$BOARDS_DIR"/*/; do
  [ -d "$board" ] || continue
  name=$(basename "$board")
  if [ "$first" -eq 1 ]; then first=0; else json+=','; fi
  json+="\"$name\""
done
json+=']}'

echo "$json" > "$OUT"
cat "$OUT"
