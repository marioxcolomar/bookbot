import sys

from stats import (
    chars_dict_to_sorted_list,
    get_chars_dict,
    get_num_words,
)


def get_book_text(book_path: str):
    with open(book_path, "r") as f:
        return f.read()


def print_report(
    path: str, num_words: int, char_count_list: list[tuple[str, int]]
) -> None:
    print("============ BOOKBOT ============")
    print(f"Looking into book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count ------")
    for char, count in char_count_list:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    text = get_book_text(path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    char_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(path, num_words, char_sorted_list)


if __name__ == "__main__":
    main()
