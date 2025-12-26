from stats import count_words, count_characters, sort_character_count

def get_book_text(path):
  with open(path) as file:
    book_data = file.read()
    return book_data

def main():
  book_path = "books/frankenstein.txt"
  book_text = get_book_text(book_path)
  total_words = count_words(book_text)
  char_counts = count_characters(book_text)
  sorted_char_counts = sort_character_count(char_counts)
  print_report(book_path, total_words, sorted_char_counts)

def print_report(path, total_words, char_counts):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}")
  print("----------- Word Count ----------")
  print(f"Found {total_words} total words")
  print("--------- Character Count -------")
  for item in char_counts:
    print(f"{item['char']}: {item['num']}")


main()
