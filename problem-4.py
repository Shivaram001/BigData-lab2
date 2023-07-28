import re
import string

def preprocess_word(word):
    # Remove punctuation and convert to lowercase
    word = word.translate(str.maketrans('', '', string.punctuation)).lower()
    return word

def mapper(document_id, text):
    # Tokenize the text into words using the regular expression [\w']+
    words = re.findall(r"[\w']+", text.lower())

    # Emit each word and its corresponding document ID
    for word in words:
        word = preprocess_word(word)
        if word:
            yield word, document_id

def reducer(word, document_ids):
    # Convert the document IDs to a sorted comma-separated string
    sorted_document_ids = sorted(set(document_ids))
    document_list = ", ".join(sorted_document_ids)

    # Emit the word and its list of document IDs
    yield word, document_list

# Example input text with three documents
input_text = {
    "Document 1": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Document 2": "Donec condimentum elit vel mauris varius, id laoreet tortor placerat.",
    "Document 3": "Nulla scelerisque felis ac risus varius, sit amet luctus elit mattis."
}

# Create an empty dictionary to store the intermediate results (inverted index)
inverted_index = {}

# Map phase: Process each document in the input text
for document_id, text in input_text.items():
    # Call the Mapper function for each document and process the results
    for word, document in mapper(document_id, text):
        # Append the document to the existing documents for the word in the dictionary
        inverted_index.setdefault(word, []).append(document)

# Reduce phase: Process the intermediate results and get the final inverted index
final_inverted_index = {}
for word, document_ids in inverted_index.items():
    # Call the Reducer function for each word and its list of documents
    for word, documents in reducer(word, document_ids):
        # Store the final inverted index in the dictionary
        final_inverted_index[word] = documents

# Sort the final inverted index by keys in alphabetical order
sorted_inverted_index = dict(sorted(final_inverted_index.items()))

# Print the final output in alphabetical order
for word, documents in sorted_inverted_index.items():
    print(f'"{word}" {documents}')