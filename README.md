# Movie Description Pre-Processing Project

This project will help you practice essential Python skills by building a text pre-processing pipeline for movie descriptions. You'll create a command-line application that reads movie descriptions from text files, cleans and processes the text, and writes the results to new files.

## Learning Objectives

By completing this project, you will demonstrate your ability to:

* Create a console application executable from the Terminal
* Choose appropriate data structures (lists, dictionaries, sets) for different tasks
* Read from and write to files using Python's file I/O operations
* Properly import and use functions from helper scripts
* Understand and utilize the `if __name__ == "__main__":` pattern
* Work with Python string methods for text processing
* Load and work with external data files

## Project Overview

You'll build a text processing pipeline that:
1. Reads a movie description from a text file
2. Converts all text to lowercase
3. Removes punctuation
4. Filters out common words (stopwords)
5. Replaces character names with a placeholder
6. Writes the cleaned text to a new file

## Getting Started

See the detailed [assignment instructions](assignment.md) for step-by-step guidance through the project.

## Project Structure

```
movie-pre-processor/
├── data/                   # Input data files
│   ├── train_to_busan_description.txt
│   └── stopwords.txt
├── src/                    # Your Python scripts
│   ├── explore_data.py
│   ├── text_parsing_functions.py
│   └── description_parser.py (you'll create this)
├── parsed/                 # Output directory (created when you run the script)
└── images/                 # Reference images
```

## Minimum Requirements

Complete Parts 1-7 of the assignment:
- Explore the data
- Implement all text parsing functions
- Create the main `description_parser.py` script
- Successfully process the movie description file

## Stretch Goals

- Implement command-line argument parsing (Part 8)
- Add error handling for missing files
- Process multiple files in a loop
- Add additional text transformations
