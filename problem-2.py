import string

# List of stopwords
stopwords = {"the", "and", "of", "a", "to", "in", "is", "it"}

def preprocess_word(word):
    # Remove punctuation and convert to lowercase
    word = word.translate(str.maketrans('', '', string.punctuation)).lower()
    return word

def mapper(line):
    # Tokenize the line into words
    words = line.strip().split()

    # Emit each preprocessed word as a key-value pair if it's not a stopword
    for word in words:
        preprocessed_word = preprocess_word(word)
        if preprocessed_word and preprocessed_word not in stopwords:
            yield preprocessed_word, 1

def reducer(word, counts):
    # Sum up the counts for each word
    total_count = sum(counts)

    # Emit the word with its total count
    yield word, total_count

def wordcount_with_stopwords(input_paragraph):
    word_counts = {}
    # Read input from the paragraph
    for line in input_paragraph.splitlines():
        # Apply the Map function and update unique words dictionary
        for word, count in mapper(line):
            if word not in word_counts:
                word_counts[word] = 0
            word_counts[word] += count

    # Sort the word counts in ascending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[0])

    # Output the final result
    for word, count in sorted_word_counts:
        print(f'"{word}" {count}')


# Input paragraph directly in the script
input_paragraph = """
    This is a sample input text. It contains some common words such as the, and, of, a, and to.
    These stopwords should be removed in the output.
    """
wordcount_with_stopwords(input_paragraph)