import json


def read_file(file_path):
    with open(file_path, "r") as f:
        content = f.readlines()
    return [x.strip("\n") for x in content]


def read_data(include_dev=False):
    train_nl = read_file("data/train.nl.filtered")
    train_cm = read_file("data/train.cm.filtered")

    if include_dev:
        dev_nl = read_file("data/dev.nl.filtered")
        dev_cm = read_file("data/dev.cm.filtered")
        train_nl += dev_nl
        train_cm += dev_cm

    test_nl = read_file("data/test.nl.filtered")
    test_cm = read_file("data/test.cm.filtered")

    return (train_nl, train_cm), (test_nl, test_cm)


def create_finetune_data(
    nls, cms, path="nl2bash_finetune.jsonl", separator="\n\n###\n\n", stop="||##||"
):
    with open(path, "w") as f:
        for nl, cm in zip(nls, cms):
            # write a line in this format: {"prompt": "nl|seprator", "completion": " cm|stop"}
            f.write(
                json.dumps(
                    {
                        "prompt": f"{nl}{separator}",
                        "completion": f" {cm}{stop}",
                    }
                )
                + "\n"
            )


def main():
    # Make sure the function works
    (train_nl, train_cm), (test_nl, test_cm) = read_data(include_dev=False)
    assert len(train_nl) == len(train_cm)
    assert len(test_nl) == len(test_cm)

    # Make sure the function still works with dev data
    (train_nl, train_cm), (test_nl, test_cm) = read_data(include_dev=True)
    assert len(train_nl) == len(train_cm)
    assert len(test_nl) == len(test_cm)

    create_finetune_data(train_nl, train_cm, path="data/nl2bash_finetune_train.jsonl")


if __name__ == "__main__":
    main()
