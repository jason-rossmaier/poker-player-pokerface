from collections import defaultdict

#ranks. Add (rank of cards involved / 13) to these values
#for straights and flushes, (highest card / 13) is added
###########
hand_str_dict = {
    'high card': 0,
    'pair' = 1,
    'two_pair' = 2,
    'three_kind' = 3,
    'straight' = 4,
    'flush' = 5,
    'full_house' = 6,
    'four_kind' = 7,
    'straight_flush' = 8,
}

def eval_hand(hole, community):
    result = 0.0
    hand_ranks = defaultdict(int)
    hand_suits = defaultdict(int)

    for card in hole:
        rank = card["rank"]
        hand_ranks[rank] += 1
        suit = card["suit"]
        hand_suits[suit] += 1

    for card in community:
        rank = card["rank"]
        hand_ranks[rank] += 1
        suit = card["suit"]
        hand_suits[suit] += 1

    for card in hand_ranks
        

if __name__ == "__main__":

    result = eval_hand([{"rank":11, "suit":'S'},{"rank":2, "suit":'D'}], [{"rank":2, "suit":'D'}])
    print result