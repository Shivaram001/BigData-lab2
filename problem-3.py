import re

def mapper(text):
    # Split the text into lines
    lines = text.splitlines()

    # Iterate through lines
    for line in lines:
        # Split the line into words using the regular expression [\w']+
        words = re.findall(r"[\w']+", line.lower())
        num_words = len(words)

        # Emit each word bigram in the line as a key-value pair
        for i in range(num_words - 1):
            bigram = f"{words[i]},{words[i + 1]}"
            yield bigram, 1

def reducer(bigram, counts):
    # Calculate the total count for each bigram
    total_count = sum(counts)

    # Emit the bigram with its total count
    yield bigram, total_count

# Example input text
input_text = """
a man a plan a canal panama there was a plan to build a canal in panama in panama a canal
was built
"""

# Create an empty dictionary to store the intermediate results
bigram_counts = {}

# Map phase: Process each line of the input text
for line in input_text.splitlines():
    # Call the Mapper function for each line and process the results
    for bigram, count in mapper(line):
        # Append the count for the bigram to the existing counts in the dictionary
        bigram_counts.setdefault(bigram, []).append(count)

# Reduce phase: Process the intermediate results and get the final bigram counts
final_bigram_counts = {}
for bigram, counts in bigram_counts.items():
    # Call the Reducer function for each bigram and its counts
    for bigram, count in reducer(bigram, counts):
        # Store the final bigram count in the dictionary
        final_bigram_counts[bigram] = count

# Print the final output in the required format
for bigram, count in final_bigram_counts.items():
    print(f'"{bigram}" {count}')