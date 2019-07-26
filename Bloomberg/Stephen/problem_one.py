def shuffle_deck(deck):
    new_deck = []

    while deck:
        index = math.randint(len(deck))
        new_deck.append(deck.pop(index))

    return new_deck


def shuffle_deck(deck):
    for _ in range(len(deck)):
        index1 = math.randint(len(deck))
        index2 = math.randint(len(deck))
        deck[index1], deck[index2] = deck[index2], deck[index1]

    return deck
