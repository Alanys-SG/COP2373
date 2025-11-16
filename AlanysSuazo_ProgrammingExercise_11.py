# Alanys Suazo
# Assignment: Programming Exercise 11

# The purpose of this assignment is to create a game program using the deck object. The program should deal
#    a poker hand of 5 cards, after which it wil prompt the user to enter a series of numbersthat selects cards
#    from the hands to be replaced, and print the results of the new hand. I will be using the sample code provided
#    in section 11.6 of the SuperCharged Python reference book being used in this course as the base for my program
#    where the Unicode for the pictograms of the suits are used.

import random

class Deck:
    def __init__(self, n_decks = 1):
        self.card_list = [num +suit
            for suit in '\u2665\u2666\u2663\u2660'
            for num in 'A23456789TJQK'
            for deck in range(n_decks)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)
