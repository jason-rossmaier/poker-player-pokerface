from collections import defaultdict

#ranks. Add (rank of cards involved / 13) to these values
#for straights and flushes, (highest card / 13) is added
###########
hand_str_dict = {
    'high card': 0,
    'pair' : 1,
    'two_pair' : 2,
    'three_kind' : 3,
    'straight' : 4,
    'flush' : 5,
    'full_house' : 6,
    'four_kind' : 7,
    'straight_flush' : 8,
}

# 0: very low, 1: have a flush
def eval_flush_potential(hand_suits):
    pass
    #for card in hand_suits:
        #if card["suit"]

def eval_hand_priv(cards):
    result = 0.0
    
    card_ranks = defaultdict(int)
    card_suits = defaultdict(int)

    for card in cards:
        rank = card["rank"]
        card_ranks[rank] += 1
        suit = card["suit"]
        card_suits[suit] += 1
        
    return max(card_ranks.items(), key = lambda x: x[1])[1]

def eval_hand(hole, community):
    return ( eval_hand_priv(hole) + eval_hand_priv(community) ) - eval_hand_priv(community)

if __name__ == "__main__":
    community = [{"rank":2, "suit":'C'}]
    hole = [{"rank":11, "suit":'S'},{"rank":2, "suit":'D'}]
    result = eval_hand(hole, community)
    print result