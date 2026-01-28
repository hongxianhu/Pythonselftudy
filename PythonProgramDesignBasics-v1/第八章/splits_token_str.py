def display_tokens(data, delimiter):
    tokens = data.split(delimiter)
    return tokens


def average_core(os_csv: str) -> list[float]:
    csv_file = open(os_csv, "r")
    lines = csv_file.readlines()
    csv_file.close()

    averages = []
    for line in lines:
        tokens = display_tokens(line, ",")

        total = 0
        for token in tokens:
            totle += token

        average = total / len(tokens)
        averages.append(average)
    return averages

