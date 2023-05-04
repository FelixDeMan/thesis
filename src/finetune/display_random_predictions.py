# This script can be used to display some of the test prompts, expected outputs, and model outputs.
import random

random.seed(1288)


def main():
    # Reading prompts and gold standard
    with open("data/test.nl.filtered", "r") as f:
        prompts = f.readlines()
    with open("data/test.cm.filtered", "r") as f:
        expected_outputs = f.readlines()

    # Reading model outputs
    with open("outputs/ada.out", "r") as f:
        ada_outputs = f.readlines()
        ada_outputs = [line.split("|||")[0] for line in ada_outputs]
    with open("outputs/babbage.out", "r") as f:
        babbage_outputs = f.readlines()
        babbage_outputs = [line.split("|||")[0] for line in babbage_outputs]
    with open("outputs/curie.out", "r") as f:
        curie_outputs = f.readlines()
        curie_outputs = [line.split("|||")[0] for line in curie_outputs]
    with open("outputs/gpt-turbo.out", "r") as f:
        gpt_turbo_outputs = f.readlines()
        gpt_turbo_outputs = [line.split("|||")[0] for line in gpt_turbo_outputs]

    # Randomly selecting 10 prompts
    random_indices = random.sample(range(len(prompts)), 20)

    # Displaying the prompts, expected outputs, and model outputs
    for i in random_indices:
        print("Prompt          : ", prompts[i].strip())
        print("Expected output : ", expected_outputs[i].strip())
        print("Ada             : ", ada_outputs[i].strip())
        print("Babbage         : ", babbage_outputs[i].strip())
        print("Curie           : ", curie_outputs[i].strip())
        print("GPT-Turbo       : ", gpt_turbo_outputs[i].strip())
        print("\n")


if __name__ == "__main__":
    main()
