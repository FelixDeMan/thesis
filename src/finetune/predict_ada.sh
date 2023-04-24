#!/bin/bash
source ../../venv/bin/activate

python predict.py \
    --model ada \
    --prompts data/test.nl.filtered  \
    --n 3 \
    --output outputs/ada.out