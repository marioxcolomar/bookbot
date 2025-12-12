def count_words(text):
  num_words = len(text.split())
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")

def sort_characters(characters):
  return characters[1]

def count_characters(text):
  characters = {}
  for char in text:
    char = char.lower()
    if char.isalpha():
      characters[char] = characters.get(char, 0) + 1
  print("--------- Character Count -------")
  list_of_characters = list(characters.items())
  list_of_characters.sort(reverse=True, key=sort_characters)

  for char, count in list_of_characters:
    print(f"{char}: {count}")