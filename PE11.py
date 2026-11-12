import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        ranks = [
            "Ace", "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "Jack", "Queen", "King"
        ]

        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

        self.cards = [
            Card(rank, suit)
            for suit in suits
            for rank in ranks
        ]

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


def display_hand(hand):
    for number, card in enumerate(hand, start=1):
        print(f"{number}. {card}")


def get_replacement_choices():
    while True:
        entry = input(
            "\nEnter the numbers of the cards you want to replace "
            "(1-5, separated by commas), or press Enter to keep all cards: "
        ).strip()

        if entry == "":
            return []

        try:
            choices = [int(value.strip()) for value in entry.split(",")]
        except ValueError:
            print("Please enter numbers like 1, 3, 5.")
            continue

        if (
            not choices
            or any(number < 1 or number > 5 for number in choices)
            or len(set(choices)) != len(choices)
        ):
            print("Enter each card number from 1 to 5 only once.")
            continue

        return choices


def play_poker_draw():
    deck = Deck()

    hand = [deck.deal_card() for _ in range(5)]

    print("Welcome to Five-Card Draw Poker!")

    print("\nYour starting hand:")
    display_hand(hand)

    replacements = get_replacement_choices()

    for number in replacements:
        hand[number - 1] = deck.deal_card()

    print("\nYour final hand:")
    display_hand(hand)

    print("\nYou received", len(replacements), "new card(s).")
    print("Thanks for playing!")


if __name__ == "__main__":
    play_poker_draw()