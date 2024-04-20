def load(path):
    kv_pairs = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            pair = line.strip().split("=", 1)

            if len(pair) != 2:
                pair.append("")

            kv_pairs.append(pair)
    return dict(kv_pairs)
