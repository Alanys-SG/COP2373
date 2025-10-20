# Alanys Suazo
# Assignment: Programming Exercise 7

# The purpose of this assignment is get more practice using regular expressions.
# The code I will be referencing is found section 7.4 in Supercharged Python by Brian Overland & John Bennett.
# This program should be able to receive a paragraph as input, then sort and read through it to tell the user
#   how many sentences were written.

# Importing the needed and wanted features
import re
import time

# This function is used to find the pattern used to identify a sentence and count the input
def sentence_counter(paragraph: str) -> list[str]:
    # This is the patterns used to organize what qualifies as a sentence and what doesn't
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
    # This goes through the text and returns every match of the pattern as a list
    sentences = re.findall(pattern, paragraph.strip(), flags=re.DOTALL | re.MULTILINE)
    return sentences

# This function i for user interaction and is the centerpoint from where the program flows
def main():
    print("Hello and welcome to 'Is it a paragraph?'")
    time.sleep(1.5)
    print("A paragraph usually consists of a collection of 3 to 5 sentences in the form of a block of text.\n"
          "This program will count the number of sentences in your inputted paragraph,\n"
          "and then tell you if it is a paragraph and how many sentences you have written.\n")
    time.sleep(4)
    while True:
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

        # prints each sentence in its own line
        print("\nHere are your sentences:")
        for i, s in enumerate(sentences, 1):
            print(f"{i}. {s}")

        # This counts and tells how many sentences the user entered
        print(f"\nTotal sentences: {len(sentences)}")
        if 7 <= len(sentences):
            print("Did you know that there is such thing as too much? This hurts my brain!")
        elif 3 <= len(sentences) <= 6:
            print("This qualifies as a decent paragraph.")
        elif 0 < len(sentences) < 3:
            print("Just a bit shy of a parapgraph but it is something.")
        else:
            print("Not a single sentence to be found! How did you manage that?")


        # Ask if the user wants to continue
        time.sleep(1.5)
        again = input("\nWould you like to continue? (y/n): ").strip().lower()
        if again != "y":
            time.sleep(1)
            print("\nExiting program.")
            time.sleep(1)
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()