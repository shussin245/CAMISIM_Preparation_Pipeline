#!/bin/bash

DOCKER_CONTAINER="cami/camisim:1.3.0"
INPUT_DIR="/Users/sarahussin/CAMISIM"
OUTPUT_DIR="/Users/sarahussin/CAMISIM_Output"

for CONFIG_FILE in "$INPUT_DIR"/Ini_Files/config_*.ini; do
	FILENAME=$(basename "$CONFIG_FILE")
	docker run -v "$INPUT_DIR:/input:rw" -v "$OUTPUT_DIR:/output:rw" "$DOCKER_CONTAINER" metagenomesimulation.py "/input/Ini_Files/$FILENAME"
done
