from two_player_games.games.morris import SixMensMorris
import random
import copy


class Minimax:
    def __init__(self, played_game):
        self.played_game = played_game
        self.maximizing_player = played_game.get_players()[0]

    def get_best_move(self, game, depth, alpha=float('-inf'), beta=float('inf')):
        if depth == 0 or game.is_finished():
            return self.heuristics(game.state, self.maximizing_player), None
        if game.get_current_player() == self.maximizing_player:
            best_score = float('-inf')
            best_moves = []
            for move in game.get_moves():
                game_copy = copy.deepcopy(game)
                game_copy.make_move(move)
                score, _ = self.get_best_move(game_copy, depth - 1, alpha, beta)
                if score > best_score:
                    best_score = score
                    best_moves = [move]
                elif score == best_score:
                    best_moves.append(move)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            best_move = random.choice(best_moves)
            return best_score, best_move
        else:
            best_score = float('inf')
            best_moves = []
            for move in game.get_moves():
                game_copy = copy.deepcopy(game)
                game_copy.make_move(move)
                score, _ = self.get_best_move(game_copy, depth - 1, alpha, beta)
                if score < best_score:
                    best_score = score
                    best_moves = [move]
                elif score == best_score:
                    best_moves.append(move)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            best_move = random.choice(best_moves)
            return best_score, best_move

    @staticmethod
    def heuristics(state, player):
        # Ocena ilości pionów na planszy
        num_player_pawns = 0
        num_opponent_pawns = 0
        for row in state.grid:
            if row is None:
                continue
            if row.char == player.char:
                num_player_pawns += 1
            else:
                num_opponent_pawns += 1

        # Liczba młynów
        num_mills = 0
        for mill in state.possible_morrises:
            if state.grid[mill[0]] is None or state.grid[mill[1]] is None or state.grid[mill[2]] is None:
                continue
            if state.grid[mill[0]].char == state.grid[mill[1]].char == state.grid[mill[2]].char == player.char:
                num_mills += 1

        # Ocena stanu gry na podstawie ilości pionów i młynów
        score = 0.5*(num_player_pawns - num_opponent_pawns) + 2*num_mills

        return score



