# Alanys Suazo
# Assignment: Programming Exercise 7

# The purpose of this assignment is get more practice using regular expressions.
# The code I will be referencing is found section 7.4 in Supercharged Python by Brian Overland & John Bennett.
# This program should be able to receive a paragraph as input, then sort and read through it to tell the user
#   how many sentences were written.

import re
import time

def sentence_counter(paragraph: str) -> list[str]:
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    sentences = re.findall(pattern, paragraph.strip(), flags=re.DOTALL | re.MULTILINE)
    return sentences

def main():
    print("Hello and welcome to 'Is it a paragraph?'")
    print("A paragraph usually consists of a collection of 3 to 5 sentences in the form of a block of text.\n"
          "This program will count the number of sentences in your inputted paragraph,\n"
          "and then tell you if it is a paragraph and how many sentences you have written.\n")

    print("Paste your paragraph below. Press Enter twice (blank line) when finished:\n")

    # Collect multiple lines until a blank line is entered
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    user_paragraph = " ".join(lines)
    sentences = sentence_counter(user_paragraph)

    print("\nHere are your sentences:")
    for i, s in enumerate(sentences, 1):
        print(f"{i}. {s}")

    print(f"\nTotal sentences: {len(sentences)}")
    if 3 <= len(sentences) <= 5:
        print("This qualifies as a paragraph.")
    else:
        print("This does not qualify as a standard paragraph.")

if __name__ == "__main__":
    main()