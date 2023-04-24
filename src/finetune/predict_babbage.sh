#!/bin/bash
source ../../venv/bin/activate

python predict.py \
    --model babbage \
    --prompts data/test.nl.filtered  \
    --n 3 \
    --output outputs/babbage.out