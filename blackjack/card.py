class Card:
    def __init__(self, value=1, suit="hearts"):
        self.value = value
        self.suit = suit

    def __str__(self):
        cardNumber = ""
        suit = self.suit.capitalize()

        if self.value == 1:
            cardNumber = "Ace"
        elif self.value == 11:
            cardNumber = "Jack"
        elif self.value == 12:
            cardNumber = "Queen"
        elif self.value == 13:
            cardNumber = "King"
        else:
            cardNumber = string(self.value)

        return f"{cardNumber} of {suit}"
