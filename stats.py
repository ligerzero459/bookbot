from string import ascii_lowercase

def count_words(text):
  words = text.split()
  return len(words)

def init_character_dictionary():
  # Initialize a dictionary with lowercase letters as keys and 0 as values
  char_dict = {}
  for char in ascii_lowercase:
    char_dict[char] = 0

  return char_dict

def count_characters(text):
  char_count = init_character_dictionary()

  for char in text.lower():
    if char in char_count:
      char_count[char] += 1

  return char_count

def sort_on(items):
    return items["num"]

def sort_character_count(char_count):
  sorted_char_count = []

  for char, count in char_count.items():
    sorted_char_count.append({
      "char": char,
      "num": count
    })

  sorted_char_count.sort(key=sort_on, reverse=True)
  return sorted_char_count
