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

# range 0-1, float. 1 is flush, 0.4 is 2 cards of same suit
def eval_flush(cards):
    card_suits = defaultdict(int)
    for card in cards:
        suit = card["suit"]
        card_suits[suit] += 1
        
    num_flush_cards = max(card_suits.items(), key = lambda x: x[1])[1]
    if (num_flush_cards) == 1: #just having 1 card of a particular suit is baseline and makes no difference
        num_flush_cards = 0
    return float(num_flush_cards) / 5.0

def eval_hand_priv(cards):
    result = 0.0
    
    card_ranks = defaultdict(int)
    for card in cards:
        rank = card["rank"]
        card_ranks[rank] += 1

    result += ( max(card_ranks.items(), key = lambda x: x[1])[1] + eval_flush(cards) )
    return result

def eval_hand(hole, community):
    if not hole:
        return 0

    if community:
        return eval_hand_priv(hole + community) - eval_hand_priv(community)
    else:
        return eval_hand_priv(hole)

if __name__ == "__main__":
    community = [{"rank":2, "suit":'C'}]
    hole = [{"rank":11, "suit":'C'},{"rank":2, "suit":'D'}]
    result = eval_hand(hole, community)
    
    print "hand result:",result
    print "flush cards: ", eval_flush(hole + community)