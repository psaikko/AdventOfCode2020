lines = open("input","r").readlines()

p1_cards = []
p2_cards = []

def read_cards(lines, i):
    cards = []
    while i < len(lines) and lines[i] != "\n":
        cards.append(int(lines[i].strip()))
        i += 1
    return cards, i

p1_cards, i = read_cards(lines, 1)
p2_cards, _ = read_cards(lines, i+2)

print(p1_cards)
print(p2_cards)

r = 1
while len(p1_cards) and len(p2_cards):
    print()
    print("-- Round %d --" % r)
    print("Player 1's deck:", ",".join(map(str,p1_cards)))
    print("Player 2's deck:", ",".join(map(str,p2_cards)))
    p1_card, p1_cards = p1_cards[0], p1_cards[1:]
    p2_card, p2_cards = p2_cards[0], p2_cards[1:]
    print("Player 1 plays:", p1_card)
    print("Player 2 plays:", p2_card)
    if p1_card > p2_card:
        print("Player 1 wins the round!")
        p1_cards += [p1_card, p2_card]
    else:
        print("Player 2 wins the round!")
        p2_cards += [p2_card, p1_card]

print()
print("== Post-game results ==")
print("Player 1's deck:", ",".join(map(str,p1_cards)))
print("Player 2's deck:", ",".join(map(str,p2_cards)))

winning_cards = p1_cards if len(p1_cards) else p2_cards

score = 0
for i in range(len(winning_cards)):
    score += winning_cards[i] * (len(winning_cards) - i)
print(score)