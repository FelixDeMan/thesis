import openai
import os
import subprocess
import ast
import shlex
import sys

def main():
    try:
        OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        openai.api_key = OPENAI_API_KEY
    except Exception as e:
        print('Error while authenticating with OpenAI, set OPENAI_API_KEY environment variable.')
    
    if len(sys.argv) != 1:
        request = " ".join(sys.argv[1:])
    else:
        request = input('Request: ')
    

    prompt = f"""# Bash (MacOS)
# <BEGIN>Show all files in current directory that are larger than 40 mb.<END>
["ls -l | awk '$5 > 40000000'"]

# Bash (MacOS)
# <BEGIN>Create a directory called textfiles, and move all text files in current directory in there<END>
["mkdir textfiles", "mv *.txt textfiles"]

# Bash (MacOS)
# <BEGIN>{request}<END>"""
    completions = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=256,
        n=1,
        stop=['#'],
        temperature=0,
    )

    model_output = completions['choices'][0]['text'].strip('\n')
    command_list = ast.literal_eval(model_output)

    print('Proposed solution:')
    for i, command in enumerate(command_list, start=1):
        print(f"\t{i}. >>> {command}")

    choice = input('Execute? [y/n]: ')

    if choice.lower() == 'y':
        for command in command_list:
            subprocess.run(shlex.split(command))

if __name__ == '__main__':
    main()
