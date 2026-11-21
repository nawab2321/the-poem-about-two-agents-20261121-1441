from pathlib import Path


POEM = (
    "I said straight across.\n"
    "The rover braked for an egg\n"
    "the color of the road.\n"
    "I took my thumb off override.\n\n"
    "It swung its lamp up the scree.\n"
    "I put my whole weight\n"
    "where it laid its light."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
