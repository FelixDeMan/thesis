#!/bin/bash
source ../../venv/bin/activate

python predict.py \
    --model gpt-3.5-turbo \
    --prompts data/test.nl.filtered  \
    --n 3 \
    --output outputs/gpt-turbo.out