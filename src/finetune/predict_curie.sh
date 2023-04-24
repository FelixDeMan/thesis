#!/bin/bash
source ../../venv/bin/activate

python predict.py \
    --model curie \
    --prompts data/test.nl.filtered  \
    --n 3 \
    --output outputs/curie.out