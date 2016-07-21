from collections import defaultdict

#ranks. Add (rank of cards involved / 13) to these values
#for straights and flushes, (highest card / 13) is added
###########
hand_str_dict = {
    'high card': 0.0,
    'pair' : 1.0,
    'two_pair' : 2.0,
    'three_kind' : 3.0,
    'straight' : 4.0,
    'flush' : 5.0,
    'full_house' : 6.0,
    'four_kind' : 7.0,
    'straight_flush' : 8.0,
}

card_value = dict((str(i), i) for i in xrange(2, 11))
card_value.update(J=11, Q=12, K=13, A=14)


# range 0-1, float. flush defined above, 0.4 is 2 cards of same suit, 0.6 3 cards of same suit
def eval_flush(card_suits):
    num_flush_cards = max(card_suits.items(), key = lambda x: x[1])[1]
    #just having 1 card of a particular suit is baseline and makes no difference
    if (num_flush_cards) == 1: 
        num_flush_cards = 0
    #we have a flush! automatically big points
    if num_flush_cards >= 5:
        return hand_str_dict['flush']

    return float(num_flush_cards) / 5.0

def has_straight_ranks(ranks):
    if len(ranks) < 5:
        return False
    ranks = sorted(ranks)
    def has_straight_4(low_rank):
        return all(i in ranks for i in xrange(low_rank, low_rank + 4))
    for i in xrange(len(ranks) - 4):
        if has_straight_4(ranks[i] + 1):
            return True
    if 14 in ranks: # A, 2, 3, 4, 5
        return has_straight_4(2)
    return False

def has_straight(cards):
    return has_straight_ranks(set(card_value[str(card["rank"])] for card in cards))

def eval_straight(cards):
    return hand_str_dict['straight'] if has_straight(cards) else 0.0

# high card, pair, three of a kind, 4 of a kind
def eval_matching_rank_hands(card_ranks):
    num_matching_ranks = max(card_ranks.items(), key = lambda x: x[1])[1]
    if num_matching_ranks == 4:
        return hand_str_dict['four_kind']
    else:
        return num_matching_ranks

def eval_matching_rank_hands_v2(card_ranks):
    count_by_multiplicities = defaultdict(int)
    for m in card_ranks.itervalues():
        count_by_multiplicities[m] += 1
    if count_by_multiplicities[4]:
        print "HAVE 4 OF A KIND"
        result = hand_str_dict['four_kind']
    elif count_by_multiplicities[3] and count_by_multiplicities[2] or count_by_multiplicities[3] == 2:
        print "HAVE FULL HOUSE"
        result = hand_str_dict['full_house']
    elif count_by_multiplicities[3]:
        print "HAVE 3 OF A KIND"
        result = hand_str_dict['three_kind']
    elif count_by_multiplicities[2] >= 2:
        print "HAVE 2 PAIRS"
        result = hand_str_dict['two_pair']
    elif count_by_multiplicities[2]:
        print "HAVE PAIR"
        result = hand_str_dict['pair']
    else:
        result = hand_str_dict['high card']
    return result

def eval_hand_priv(cards):
    card_ranks = defaultdict(int)
    card_suits = defaultdict(int)
    for card in cards:
        rank = card["rank"]
        card_ranks[rank] += 1
        suit = card["suit"]
        card_suits[suit] += 1
    v1 = eval_matching_rank_hands(card_ranks)
    v2 = eval_matching_rank_hands_v2(card_ranks)
    print "DANIEL'S EVAL_HAND:", v1
    print "DI-AN'S EVAL_HAND:", v2
    return max( v1, eval_flush(card_suits), eval_straight(cards) )

def eval_hand(hole, community):
    if not hole:
        return 0

    if community:
        return eval_hand_priv(hole + community) - eval_hand_priv(community)
    else:
        return eval_hand_priv(hole)

if __name__ == "__main__":
    community = [{"rank":2, "suit":'C'}]
    hole = [{"rank":"J", "suit":'C'},{"rank":"J", "suit":'D'},{"rank":"Q", "suit":'C'},{"rank":2, "suit":'C'}]
    result = eval_hand(hole, community)

    print "hand result:",result

    assert has_straight_ranks([2,3,4,5,6])
    assert has_straight_ranks([2,3,4,5,14])
    assert not has_straight_ranks([2,3,4,5,7,8,9,10])
    print "hand result:",result
