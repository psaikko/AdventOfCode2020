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

n_games = 0
def play(p1_cards, p2_cards):
    global n_games 

    n_games += 1
    gid = n_games
    print("\n=== Game %d ===" % gid)

    state_cache = set()
    r = 1
    while len(p1_cards) and len(p2_cards):
        print()
        print("-- Round %d (Game %d)--" % (r, gid))
        print("Player 1's deck:", ",".join(map(str,p1_cards)))
        print("Player 2's deck:", ",".join(map(str,p2_cards)))

        s = str(p1_cards)+str(p2_cards)
        if s in state_cache:
            print("Player 1 wins to prevent an infinite loop")
            return 1
        state_cache.add(s)

        p1_card, p1_cards = p1_cards[0], p1_cards[1:]
        p2_card, p2_cards = p2_cards[0], p2_cards[1:]
        print("Player 1 plays:", p1_card)
        print("Player 2 plays:", p2_card)

        winner = 0
        if len(p1_cards) >= p1_card and len(p2_cards) >= p2_card:
            print("Playing a sub-game to determine the winner...")
            winner = play(p1_cards[:p1_card], p2_cards[:p2_card])
            print("\n...anyway, back to game %d." % gid)
        elif p1_card > p2_card:
            winner = 1
        else:
            winner = 2

        if winner == 1:
            print("Player 1 wins round %d of game %d!" % (r, gid))
            p1_cards += [p1_card, p2_card]
        elif winner == 2:
            print("Player 2 wins round %d of game %d!" % (r, gid))
            p2_cards += [p2_card, p1_card]
        else:
            print("?!")
            exit(1)

        r += 1
    
    winner = 1 if len(p1_cards) else 2
    print("The winner of game %g is player %d" % (gid, winner))

    if gid == 1:
        print()
        print("== Post-game results ==")
        print("Player 1's deck:", ",".join(map(str,p1_cards)))
        print("Player 2's deck:", ",".join(map(str,p2_cards)))

        winning_cards = p1_cards if len(p1_cards) else p2_cards

        score = 0
        for i in range(len(winning_cards)):
            score += winning_cards[i] * (len(winning_cards) - i)
        print(score)
        exit(0)

    return winner

play(p1_cards, p2_cards)