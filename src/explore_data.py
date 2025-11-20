"""
Data exploration script for movie description text file.

This script helps you understand the structure and content of the
movie description data before building the text processing pipeline.
"""

def explore_file(filepath):
    """
    Reads and displays statistics about a text file.

    Parameters
    ----------
    filepath : str
        Path to the text file to explore
    """
    print(f"\n{'='*60}")
    print(f"Exploring: {filepath}")
    print(f"{'='*60}\n")

    # Read the entire file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')

    # Display basic statistics
    print(f"Total characters: {len(content)}")
    print(f"Total lines: {len(lines)}")
    print(f"Total words: {len(content.split())}")

    # Display first 5 lines
    print(f"\n{'='*60}")
    print("First 5 lines:")
    print(f"{'='*60}")
    for i, line in enumerate(lines[:5], 1):
        print(f"{i}: {line}")

    # Display sample of words
    words = content.split()
    print(f"\n{'='*60}")
    print("First 20 words:")
    print(f"{'='*60}")
    print(" ".join(words[:20]))

    # Character type examples
    print(f"\n{'='*60}")
    print("Character types found in first line:")
    print(f"{'='*60}")
    first_line = lines[0] if lines else ""
    has_uppercase = any(c.isupper() for c in first_line)
    has_lowercase = any(c.islower() for c in first_line)
    has_punctuation = any(c in '.,!?;:\'"()-' for c in first_line)
    has_numbers = any(c.isdigit() for c in first_line)

    print(f"Has uppercase letters: {has_uppercase}")
    print(f"Has lowercase letters: {has_lowercase}")
    print(f"Has punctuation: {has_punctuation}")
    print(f"Has numbers: {has_numbers}")

    # Common words preview (simple frequency)
    print(f"\n{'='*60}")
    print("Sample of unique words (first 10):")
    print(f"{'='*60}")
    unique_words = list(set(words))[:10]
    for word in unique_words:
        print(f"  - {word}")

    print(f"\n{'='*60}")
    print("What will your text processing pipeline need to do?")
    print(f"{'='*60}")
    print("1. Convert uppercase to lowercase")
    print("2. Remove punctuation")
    print("3. Remove common words (stopwords like 'the', 'a', 'and')")
    print("4. Replace character names with 'person'")
    print("5. Write the cleaned text to a new file")
    print()


if __name__ == '__main__':
    # Path to the movie description file
    filepath = 'data/train_to_busan_description.txt'

    print("\nWelcome to the Movie Description Data Explorer!")
    print("This script will help you understand the data you'll be processing.\n")

    try:
        explore_file(filepath)

        print("\nNext Steps:")
        print("-----------")
        print("1. Review the text structure and content above")
        print("2. Think about how you'll transform this text")
        print("3. Start building functions in text_parsing_functions.py")
        print("4. Test each function as you write it")
        print()

    except FileNotFoundError:
        print(f"\nError: Could not find file '{filepath}'")
        print("Make sure you're running this script from the project root directory.")
        print()
