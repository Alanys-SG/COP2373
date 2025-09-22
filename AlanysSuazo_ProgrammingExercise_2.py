# Alanys Suazo-Gracia
# Assignment: Programming Exercise 2

# The purpose of this assignment is to create a program that scans user input as a string
#   after which that sting will be scanned for key phrases seen and used in scam emails. It should return the
#   number of substrings and set an accumulator which will tell the user the likeliness of an email being a scam.

# because I want to practice with display
import time


#was having issues with the functions not scanning the message correctly so i am making something to adjust the message
# to strip the characters that were interfering
def clean_message(message):
    # Convert to lowercase
    message = message.lower()

    # Remove common punctuation manually
    for char in ['.', ',', '!', '?', ':', ';', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '*', '/', '\\']:
        message = message.replace(char, '')

    # Collapse multiple spaces
    message = ' '.join(message.split())

    return message



#setting up the calculator
def spam_sorter(message, keywords):
    spam_score = 0
    matched = []

    message = clean_message(message)  # Clean before scanning

    for word in keywords:
        word_lower = word.lower()
        if word_lower in message:
            count = message.count(word_lower)
            spam_score += count
            matched.append((word, count))

    return spam_score, matched



def scam_score_counter(score):
    if score == 0:
        return "...its not really spam."
    elif 1 <= score <= 3 :
        return "Low chances of spam, but be careful"
    elif 4 <= score <= 6:
        return "Medium chances of spam, send it to the junk pile!"
    else:
        return ("""Yeah its definitely spam! What did you even give me here!?
        
               "I feel like you knew this was spam and just wanted to see what I would do...""")

def main():
    # makes a list of strings/substrings to search for in an email
    keywords = [
        # these strings are related to the promotional area of the spam
        "earn money", "make money fast", "cash bonus", "million dollars", "get paid",
        "lowest price", "save big", "no credit check", "double your income", "investment opportunity",
        "free trial", "limited time offer", "exclusive deal", "click here", "buy now",
        "order today", "special promotion", "risk-free", "100% free", "no obligation",

        # strings focused on the manipulative language that is commonly used spam
        "act now", "congratulations", "you’ve been selected", "urgent response needed",
        "this won’t last", "winner", "guarantee", "call now", "unsecured debt", "work from home",

        # and because the dangerous emails can be considered spam too, I included high-risk security and phishing terms
        "alert", "attention", "suspicious activity", "account suspended", "security notice",
        "verify your account", "unusual login", "immediate action required",
        "your account is in danger", "password expired"
    ]
    print ("SPAM DETECTOR v1.0")
    time.sleep(3)

    # making a while loop for the user so that program can be run multiple times
    while True:

        # enter message here
        message = input("Enter your email message:\n").strip().lower()
        score, matched_keywords = spam_sorter(message, keywords)
        rating = scam_score_counter(score)

                # display
        print ('\nScanning Message...')
        time.sleep(5)
        print("\n--- Spam Analysis ---")
        time.sleep(2)
        print(f"Spam Score: {score}")
        time.sleep(2)
        print(f"Likelihood: {rating}")
        time.sleep(2)
        if matched_keywords:
            print("Matched Keywords:")
            for word, count in matched_keywords:
                print(f" - '{word}' ({count} time{'s' if count > 1 else ''})")
        else:
            print("No spam keywords detected.")
            time.sleep(2)
            print ('Congrats!')

        again = input("\nWould you like to check another message? (yes/no): ").strip().lower()
        if again not in ["yes","y"]:
            print("\nThanks for using SPAM DETECTOR v1.0. Stay safe out there!")
            break

if __name__ == "__main__":
    main()


