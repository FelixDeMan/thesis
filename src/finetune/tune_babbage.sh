#!/bin/bash
source ../../venv/bin/activate

# Creating the fine-tune
openai api fine_tunes.create \
    -t data/nl2bash_finetune_train.jsonl \
    -m babbage \
    --n_epochs 3 \
    --suffix "babbage 3 epochs"

# Syncing with wandb
openai wandb sync

# To get completion
# openai api completions.create -m #babbage:ft-personal:babbage-3-epochs-2023-04-18-11-00-05 -p <YOUR_PROMPT>

