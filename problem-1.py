import string

def preprocess_word(word):
    # Remove punctuation and convert to lowercase
    word = word.translate(str.maketrans('', '', string.punctuation)).lower()
    return word

def mapper(line):
    # Tokenize the line into words
    words = line.strip().split()
    
    # Emit each preprocessed word as a key-value pair
    for word in words:
        preprocessed_word = preprocess_word(word)
        if preprocessed_word:
            yield preprocessed_word, 1

def reducer(word, counts):
    # Sum up the counts for each word
    total_count = sum(counts)
    
    # Emit the word with its total count if it's unique
    if total_count == 1:
        yield word, total_count

# Input paragraph directly in the script
input_paragraph = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Donec condimentum elit vel mauris varius, id laoreet tortor placerat.
Nulla scelerisque felis ac risus varius, sit amet luctus elit mattis.
"""

unique_words = set()  # Set to store unique words

# Read input from the paragraph
for line in input_paragraph.splitlines():
    # Apply the Map function and update unique words set
    for word, count in mapper(line):
        unique_words.add(word)

# Sort the unique words in alphabetical order
sorted_words = sorted(unique_words)

# Output the final result
for word in sorted_words:
    print(f'"{word}" 1')




