import openai
import os
import argparse


# Getting top n completions from a finetuned model
# returns a list of strings
def get_top_n_completions(model, prompt, n=1, separator="\n\n###\n\n", stop="||##||"):
    response = openai.Completion.create(
        prompt=prompt + separator,
        model=model,
        max_tokens=250,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=[stop],
        n=n,
    )
    return [completion["text"].strip() for completion in response["choices"]]


def main():
    # Authenticating with openai
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Parse command line arguments
    parser = argparse.ArgumentParser()

    # Name of the model, can be ada, curie, or babbage, required, defaults to ada
    parser.add_argument("--model", type=str, required=True)

    # Number of completions per innstance
    parser.add_argument("--n", type=int, default=3)

    # Path to the file containing the prompts, defaults to data/test.nl.filtered
    parser.add_argument("--prompts", type=str, default="data/test.nl.filtered")

    # Get arguments
    args = parser.parse_args()

    # Set model name
    if args.model == "ada":
        model = "ada:ft-personal:ada-3-epochs-2023-04-18-09-43-53"
    elif args.model == "babbage":
        model = "babbage:ft-personal:babbage-3-epochs-2023-04-18-11-00-05"


if __name__ == "__main__":
    main()
