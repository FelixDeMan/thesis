import tiktoken


def get_file_contents(file_names):
    contents = ""
    for file in file_names:
        with open("../finetune/data/" + file, "r") as f:
            file_contents = f.read()
            contents += "\n" + file_contents
    return contents


def calculate_cost(n_tokens, model_cost):
    return round(n_tokens / 1000 * model_cost, 2)


def main():
    files = [
        "train.cm.filtered",
        "train.nl.filtered",
        "dev.cm.filtered",
        "dev.nl.filtered",
    ]
    contents = get_file_contents(files)

    model_costs = {"ada": 0.0004, "babbage": 0.0006, "curie": 0.0030, "davinci": 0.0300}
    model_encodings = {
        model: tiktoken.encoding_for_model(model) for model in model_costs
    }

    n_tokens_per_model = {}
    for model, encoding in model_encodings.items():
        tokens = encoding.encode(contents)
        n_tokens = len(tokens)
        n_tokens_per_model[model] = n_tokens

    costs = {
        model: calculate_cost(n_tokens, model_costs[model])
        for model, n_tokens in n_tokens_per_model.items()
    }

    total = 0
    for model, cost in costs.items():
        total += cost
        print(f"{model:21}: ${cost:.2f}")

    print(f"\n{'Total cost':21}: ${total:.2f}")
    print(f"{'Total cost (3 Epochs)':21}: ${total * 3:.2f}")


if __name__ == "__main__":
    main()
