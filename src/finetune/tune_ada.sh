#!/bin/bash
source ../../venv/bin/activate

# Creating the fine-tune
openai api fine_tunes.create \
    -t data/nl2bash_finetune_train.jsonl \
    -m ada \
    --n_epochs 3 \
    --suffix "ada 3 epochs"

# Syncing with wandb
openai wandb sync

# To get completion
# openai api completions.create -m ada:ft-personal:ada-3-epochs-2023-04-18-09-43-53 -p <YOUR_PROMPT>
