# import tiktoken


# def get_file_contents(file_names):
#     contents = ""
#     for file in file_names:
#         with open("src/finetune/data/" + file, "r") as f:
#             file_contents = f.read()
#             contents += "\n" + file_contents
#     return contents


# def calculate_cost(n_tokens, model_costs):
#     return {model: n_tokens / 1000 * cost for model, cost in model_costs.items()}


# def main():
#     files = [
#         "train.cm.filtered",
#         "train.nl.filtered",
#         "dev.cm.filtered",
#         "dev.nl.filtered",
#     ]
#     contents = get_file_contents(files)

#     encoding = tiktoken.get_encoding("r50k_base")
#     tokens = encoding.encode(contents)
#     n_tokens = len(tokens)

#     model_costs = {"ada": 0.0004, "babbage": 0.0006, "davinci": 0.0300, "curie": 0.0030}
#     costs = calculate_cost(n_tokens, model_costs)

#     total = 0
#     for model, cost in costs.items():
#         total += cost
#         print(f"{model}: ${round(cost, 3)}")

#     print(f"\nTotal cost: ${round(total, 3)}")


# if __name__ == "__main__":
#     main()

import tiktoken


def get_file_contents(file_names):
    contents = ""
    for file in file_names:
        with open("src/finetune/data/" + file, "r") as f:
            file_contents = f.read()
            contents += "\n" + file_contents
    return contents


def calculate_cost(n_tokens, model_cost):
    return n_tokens / 1000 * model_cost


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
        print(f"{model:8}: $ {cost:6.3f}")

    print(f"\n{'Total cost':8}: $ {total:6.3f}")


if __name__ == "__main__":
    main()
