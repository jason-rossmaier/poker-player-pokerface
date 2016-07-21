
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
    #pre-flop
        if game_state.round == 0:
            cards = game_state.players[game_state.in_action].hole_cards
            #if we have at least one ace or a pair, we bet the first hand, if not, then fold
            if (cards[0].rank == 'A'
                or cards[1] == 'A'
                or cards[0].rank == cards[1].rank):
                return game_state.current_buy_in + game_state.minimum_raise
            else:
            return 0
            
        else:
            return 100

    def showdown(self, game_state):
        pass

