#!/bin/bash
source ../../venv/bin/activate

# Creating the fine-tune
openai api fine_tunes.create \
    -t data/nl2bash_finetune_train.jsonl \
    -m curie \
    --n_epochs 3 \
    --suffix "curie 3 epochs"

# Syncing with wandb
openai wandb sync

# To get completion
# openai api completions.create -m curie:ft-personal:curie-3-epochs-2023-04-18-11-41-28 -p <YOUR_PROMPT>

