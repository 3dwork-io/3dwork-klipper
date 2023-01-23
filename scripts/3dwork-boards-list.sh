#!/bin/bash

# Store the names of all folders in the current directory
boards=$(ls /home/pi/printer_data/config/3dwork/boards/ -d */)

# Write the names to a text file
echo "$boards" > boards_list.txt

# Print the contents of the text file
cat boards_list.txt
