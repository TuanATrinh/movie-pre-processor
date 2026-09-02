"""Parse and clean a movie description text file."""

import argparse
import os

import text_parsing_functions as tpf

NAMES = {
    'suan', 'seongkyeong', 'yonsuk', 'seokwoo', 'sanghwa',
    'ingil', 'jonggil', 'yongguk', 'jinhee'
}
REPLACEMENT = 'person'


def clean_file(filepath, stopwords, names, replacement):
    """Read a file line-by-line and return a list of cleaned lines."""
    cleaned_lines = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            cleaned_lines.append(
                tpf.line_cleaning_pipeline(line, stopwords, names, replacement)
            )
    return cleaned_lines


def write_lines(filepath, lines):
    """Write cleaned lines to a text file, one line per item."""
    directory = os.path.dirname(filepath)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))
        if lines:
            file.write('\n')


def main():
    """Parse command-line arguments and process the movie description."""
    parser = argparse.ArgumentParser(
        description='Clean a movie description for text clustering.'
    )
    parser.add_argument('-i', '--input', required=True,
                        help='Path to the input movie description')
    parser.add_argument('-o', '--output', required=True,
                        help='Path to the cleaned output file')
    args = parser.parse_args()

    stopwords = tpf.load_stopwords('data/stopwords.txt')
    cleaned_lines = clean_file(args.input, stopwords, NAMES, REPLACEMENT)
    write_lines(args.output, cleaned_lines)


if __name__ == '__main__':
    main()
