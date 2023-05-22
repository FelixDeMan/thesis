import questionary
import pandas as pd
from datetime import datetime
import os


FILE_NAME = "results.csv"

questions = [
    {"type": "text", "msg": "Name and last name:", "column_name": "name"},
    {
        "type": "text",
        "msg": "How many years of experience do you have with Unix shell languages (Bash, zsh, etc.) (provide a whole number):",
        "column_name": "exp_years",
    },
    {
        "type": "select",
        "msg": "Rate your proficiency in Unix shell languages (Bash, zsh, etc.): 1 (Beginner) - 5 (Expert)",
        "choices": ["1", "2", "3", "4", "5"],
        "column_name": "proficiency",
    },
    {
        "type": "select",
        "msg": "roger was easy to use: 1 (Strongly disagree) - 5 (Strongly agree)",
        "choices": ["1", "2", "3", "4", "5"],
        "column_name": "easy_use",
    },
    {
        "type": "select",
        "msg": "roger understood me well: 1 (Strongly disagree) - 5 (Strongly agree)",
        "choices": ["1", "2", "3", "4", "5"],
        "column_name": "understood",
    },
    {
        "type": "select",
        "msg": "rogers answers were useful: 1 (Strongly disagree) - 5 (Strongly agree) ",
        "choices": ["1", "2", "3", "4", "5"],
        "column_name": "answers_useful",
    },
    {
        "type": "select",
        "msg": "roger asked me for additional information when needed: 1 (Strongly disagree) - 5 (Strongly agree) ",
        "choices": ["1", "2", "3", "4", "5"],
        "column_name": "additional_info",
    },
    {
        "type": "select",
        "msg": "roger was able to explain its own output when asked: 1 (Strongly disagree) - 5 (Strongly agree) ",
        "choices": [
            "1",
            "2",
            "3",
            "4",
            "5",
            "I did not ask roger to explain its output during the study",
        ],
        "column_name": "explain_output",
    },
    {
        "type": "select",
        "msg": "roger coped well with any mistakes I made when prompting it: 1 (Strongly disagree) - 5 (Strongly agree) ",
        "choices": [
            "1",
            "2",
            "3",
            "4",
            "5",
            "I did not make any mistakes (typos, semantic errors) while prompting roger",
        ],
        "column_name": "robustness",
    },
    {
        "type": "select",
        "msg": "roger is an improvement to my workflow: 1 (Strongly disagree) - 5 (Strongly agree) ",
        "choices": ["1", "2", "3", "4", "5"],
        "column_name": "workflow_improvement",
    },
    {
        "type": "select",
        "msg": "roger generates useful shell commands: 1 (Strongly disagree) - 5 (Strongly agree)",
        "choices": ["1", "2", "3", "4", "5"],
        "column_name": "generation_useful",
    },
    {
        "type": "select",
        "msg": "Using roger improved my efficiency while using the terminal: 1 (Strongly disagree) - 5 (Strongly agree)",
        "choices": ["1", "2", "3", "4", "5"],
        "column_name": "efficiency",
    },
    {
        "type": "select",
        "msg": "roger's response time was satisfactory: 1 (Strongly disagree) - 5 (Strongly agree)",
        "choices": ["1", "2", "3", "4", "5"],
        "column_name": "response_time",
    },
    {
        "type": "select",
        "msg": "I felt more confident with my terminal skills with roger's assistance: 1 (Strongly disagree) - 5 (Strongly agree)",
        "choices": ["1", "2", "3", "4", "5"],
        "column_name": "confidence",
    },
    {
        "type": "select",
        "msg": "I would continue using roger for future terminal tasks: 1 (Strongly disagree) - 5 (Strongly agree)",
        "choices": ["1", "2", "3", "4", "5"],
        "column_name": "continue_using",
    },
    {
        "type": "confirm",
        "msg": "roger's command suggestions taught me new commands",
        "column_name": "learned_commands",
    },
    {
        "type": "confirm",
        "msg": "I ran at least one command generated by roger that I did not fully understand",
        "column_name": "uncertain_command",
    },
    {
        "type": "text",
        "msg": "What do you think could be improved about roger? Do you have any criticisms?",
        "column_name": "improvement_comments",
    },
]

responses = {}

for question in questions:
    question_type = question["type"]
    msg = question["msg"]

    if question_type == "text":
        response = questionary.text(msg).ask()
    elif question_type == "select":
        response = questionary.select(msg, choices=question["choices"]).ask()
    elif question_type == "rawselect":
        response = questionary.rawselect(msg, choices=question["choices"]).ask()
    elif question_type == "confirm":
        response = questionary.confirm(msg, auto_enter=False).ask()

    responses[question["column_name"]] = response

responses["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create a DataFrame and save/append the result
df = pd.DataFrame(responses, index=[0])

if os.path.exists(FILE_NAME):
    df.to_csv(FILE_NAME, mode="a", header=False, index=False)
else:
    df.to_csv(FILE_NAME, mode="a", index=False)
