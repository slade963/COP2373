
"""
Sentence Counter Program
This program accepts a paragraph, displays each individual sentence,
and counts the total number of sentences.
"""

import re


def split_sentences(paragraph):
    """Find and return individual sentences in the paragraph."""

    # Match sentences beginning with a capital letter or a number.
    # The look-ahead checks for a space followed by a capital letter
    # or number, or the end of the paragraph.
    pattern = r'[A-Z0-9].*?[.!?](?=\s+[A-Z0-9]|$)'

    # Find all sentences without consuming the next sentence's first character.
    matches = re.findall(pattern, paragraph, flags=re.DOTALL)

    # Remove extra spaces from each sentence.
    sentences = [sentence.strip() for sentence in matches]

    return sentences


def display_sentences(sentences):
    """Display each sentence and the total sentence count."""

    # Display each sentence with its number.
    for number, sentence in enumerate(sentences, start=1):
        print(f"{number}. {sentence}")

    # Display the total number of sentences.
    print(f"\nSentence count: {len(sentences)}")


def main():
    """Get paragraph input and run the sentence counter."""

    # Ask the user to enter a paragraph.
    paragraph = input("Enter a paragraph: ").strip()

    # Check whether the user entered anything.
    if not paragraph:
        print("No paragraph entered. Please run the program again.")
        return

    # Separate the paragraph into individual sentences.
    sentences = split_sentences(paragraph)

    # Display the sentences and their total count.
    display_sentences(sentences)


# Run the main function when the program starts.
if __name__ == "__main__":
    main()
