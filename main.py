import sys
from stats import count_words, count_characters

def get_book_text(book_path):
  with open(book_path, "r") as f:
    return f.read()

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  path = sys.argv[1]
  print(f"Analyzing book found at {path}...")
  text = get_book_text(path)
  count_words(text)
  count_characters(text)

if __name__ == "__main__":
  main()