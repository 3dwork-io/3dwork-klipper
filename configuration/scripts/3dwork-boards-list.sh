#!/bin/bash

# Store the names of all folders in the /boards directory
folders=$(ls -d /home/pi/printer_data/config/3dwork-klipper/boards/*/)

# Create a JSON object with the folder names
json_data='{"boards":['
for boards in $boards; do
  json_data+='"'$boards'",'
done
json_data=${json_data%,}
json_data+=']}'

# Write the JSON object to a file
echo $json_data > boards_list.json