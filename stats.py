def sort_on(characters: tuple[str, int]) -> int:
    return characters[1]


def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_chars_dict(text: str) -> dict[str, int]:
    chars: dict[str, int] = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def chars_dict_to_sorted_list(dict: dict[str, int]) -> list[tuple[str, int]]:
    res: list[tuple[str, int]] = []

    for key, char in dict.items():
        res.append((key, char))

    sort = sorted(res, key=sort_on, reverse=True)
    return sort
