import text_parsing_functions as tpf

def read_lines_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = []

        for line in f:
            lines.append(line)

    return lines

def clean_lines(lines, stopwords, names, replacement):
    cleaned_lines = []

    for line in lines:
        cleaned_line = tpf.line_cleaning_pipeline(
            line,
            stopwords,
            names,
            replacement
        )

    cleaned_lines.append(cleaned_line)

    return cleaned_lines

def write_lines_to_file(lines, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

if __name__ == '__main__':
    # Load stopwords from file
    stopwords = tpf.load_stopwords('data/stopwords.txt')

    # Character names that should be replaced with 'person'
    replacement = 'person'
    names = {
      'suan',
      'seongkyeong',
      'yonsuk',
      'seokwoo',
      'ingil',
      'yonghuk',
      'jinhee'
    }

    lines = read_lines_from_file('data/train_to_busan_description.txt')

    cleaned_lines = clean_lines(
        lines,
        stopwords,
        names,
        replacement
    )

    write_lines_to_file(
        cleaned_lines,
        'parsed/train_to_busan.txt'
    )

    # Test the pipeline with a sample line
    line_text = (
      "pregnant wife Seong-kyeong, "
      "a high school baseball team, "
      "rich-yet-egotistical"
    )
    cleaned_text = tpf.line_cleaning_pipeline(
        line_text,
        stopwords,
        names,
        replacement
        )

    print(cleaned_text)