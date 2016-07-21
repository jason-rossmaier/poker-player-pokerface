import sys
sys.stdout = sys.stderr

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
        round = game_state["round"]

        #pre-flop
        if game_state["round"] == 0:
            cards = our_player["hole_cards"]
            #if we have at least one ace or a pair, we bet the first hand, if not, then fold
            if (cards[0]["rank"] == 'A'
                    or cards[1] == 'A'
                    or cards[0]["rank"] == cards[1]["rank"]):
                this_bet = min_bet + minimum_raise
            else:
                this_bet = 0
        else:
            this_bet = 100
        print "******** ROUND", round, "BET", this_bet
        return this_bet

    def showdown(self, game_state):
        pass
