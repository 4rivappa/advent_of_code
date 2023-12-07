
class Hand:
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    def __init__(self, cards, bid):
        self.cards = cards
        self.type = self.classify_hand(cards)
        self.bid = bid
    
    def __lt__(self, other):
        if self.type < other.type:
            return True
        elif self.type > other.type:
            return False
        else:
            return self.compare_equal_types(self.cards, other.cards)
    
    def compare_equal_types(self, first, second):
        for it in range(len(first)):
            first_letter = first[it]
            second_letter = second[it]
            if self.card_values.index(first_letter) < self.card_values.index(second_letter):
                return True
            elif self.card_values.index(first_letter) > self.card_values.index(second_letter):
                return False
        return True

    def classify_hand(self, string: str) -> int:
        letters = dict()
        for letter in string:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        hand_type = 0
        if len(letters) == 5:
            hand_type = 1 # high-card
        elif len(letters) == 4:
            hand_type = 2 # one-pair
        elif len(letters) == 3:
            values = list(letters.values())
            values.sort()
            if values[-1] == 3:
                hand_type = 4 # three-of-a-kind
            elif values[-1] == 2:
                hand_type = 3 # two-pair
        elif len(letters) == 2:
            values = list(letters.values())
            values.sort()
            if values[-1] == 4:
                hand_type = 6 # four-of-a-kind
            elif values[-1] == 3:
                hand_type = 5 # full-house
        elif len(letters) == 1:
            hand_type = 7 # five-of-a-kind
        return hand_type

def main() -> None:
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    hands = []
    for line in lines:
        elems = line.strip().split(" ")
        hands.append(Hand(elems[0], int(elems[1])))
    
    hands.sort()

    return_amount = 0
    for index in range(len(hands)):
        return_amount += hands[index].bid * (index + 1)
    print(return_amount)

if __name__ == "__main__":
    main()