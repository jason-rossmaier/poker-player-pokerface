import sys
from collections import defaultdict
sys.stdout = sys.stderr

print "PYTHON VERSION", sys.version

def eval_hand(cards):
    result = 0.0
    card_ranks = defaultdict(int)

    for card in cards:
        rank = card["rank"]
        card_ranks[rank] += 1

    return max(card_ranks.items(), key = lambda x: x[1])[1]
    
class Player:
    VERSION = "Default Python folding player"
    
    def betRequest(self, game_state):
        in_action = game_state["in_action"]
        current_buy_in = game_state["current_buy_in"]
        pot = game_state["pot"]
        minimum_raise = game_state["minimum_raise"]
        players = game_state["players"]
        our_player = players[in_action]
        min_bet = current_buy_in - our_player["bet"]
        bet_index = game_state["bet_index"]
        community_cards = game_state["community_cards"]
        my_cards = our_player["hole_cards"]
        round = game_state["round"]

        hand_score = 0

        if len(community_cards):
            hand_value = eval_hand(my_cards + community_cards)
            community_value = eval_hand(community_cards)
            hand_score = hand_value - community_value
        else:
            hand_score = eval_hand(my_cards)

        #pull out the other players
        other_players = [player for player in players if player["status"] == "active" and player is not our_player]

        #other_players + 1
        n_playing = len(other_players) + 1

        #pre-flop
        if len(community_cards) == 0:
            cards = our_player["hole_cards"]
            #if we have at least one ace or a pair, we bet the first hand, if not, then fold
            if (cards[0]["rank"] == 'A'
                    or cards[1]["rank"] == 'A'
                    or cards[0]["rank"] == cards[1]["rank"]):
                this_bet = 500 # min_bet + minimum_raise
            elif current_buy_in <= 50:
                this_bet = min_bet
            else:
                this_bet = 0
        #if we are post flop and have a larger chip stack, put them all in
        elif hand_score > 0:
            if n_playing == 2 and other_players[0]["stack"] < our_player["stack"]:
                this_bet = other_players[0]["stack"]
            else:
                this_bet = max(min_bet, int(our_player["stack"]) / 2)  
        else:
            this_bet = minimum_raise
        print "******** ROUND", round, "BET_INDEX", bet_index, "BET", this_bet, "STACK", our_player["stack"], "N_PLAYING", n_playing, "Hand Rating", hand_score
        return this_bet

    def showdown(self, game_state):
        pass

if __name__ == "__main__":
    import json
    game_state = json.loads('''
{
    "tournament_id":"550d1d68cd7bd10003000003",
    "game_id":"550da1cb2d909006e90004b1",
    "round":0,
    "bet_index":0,
    "small_blind": 10,
    "current_buy_in": 320,
    "pot": 400,
    "minimum_raise": 240,
    "dealer": 1,
    "orbits": 7,
    "in_action": 1,
    "players": [
        {
            "id": 0,
            "name": "Albert",
            "status": "active",
            "version": "Default random player",
            "stack": 1010,
            "bet": 320
        },
        {
            "id": 1,
            "name": "Bob",
            "status": "active",
            "version": "Default random player",
            "stack": 1590,
            "bet": 80,
            "hole_cards": [
                {
                    "rank": "6",
                    "suit": "hearts"
                },
                {
                    "rank": "K",
                    "suit": "spades"
                }
            ]
        },
        {
            "id": 2,
            "name": "Chuck",
            "status": "out",
            "version": "Default random player",
            "stack": 0,
            "bet": 0
        }
    ],
    "community_cards": [
        {
            "rank": "4",
            "suit": "spades"
        },
        {
            "rank": "A",
            "suit": "hearts"
        },
        {
            "rank": "6",
            "suit": "clubs"
        }
    ]
}''')
    player = Player()
    print player.betRequest(game_state)
