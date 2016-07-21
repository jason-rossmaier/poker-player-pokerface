import sys
sys.stdout = sys.stderr

print "PYTHON VERSION", sys.version

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
        round = game_state["round"]

        #pull out the other players
        other_players = []
        for player in players if player["status"] == "active" and player is not our_player:
            other_players.copy(player)
        
        #other_players + 1
        n_playing = len(other_players) + 1

        #pre-flop
        if len(community_cards) == 0:
            cards = our_player["hole_cards"]
            #if we have at least one ace or a pair, we bet the first hand, if not, then fold
            if (cards[0]["rank"] == 'A'
                    or cards[1]["rank"] == 'A'
                    or cards[0]["rank"] == cards[1]["rank"]):
                this_bet = min_bet + minimum_raise
            else:
                this_bet = 0
        #if we are post flop and have a larger chip stack, put them all in
        else if n_playing == 2 and other_players[0]["stack"] < our_player["stack"]:
            this_bet = other_players[0]["stack"]
        else:
            this_bet = 100
        print "******** ROUND", round, "BET_INDEX", bet_index, "BET", this_bet, "STACK", our_player["stack"], "N_PLAYING", n_playing
        return this_bet

    def showdown(self, game_state):
        pass
