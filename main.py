from two_player_games.games.morris import SixMensMorris  # or any other game
from minimax import Minimax  # or any other game
import random
import time

# Słownik przechowujący wyniki dla każdego z graczy
results = {
    'Player 1': {'wins': 0, 'draws': 0, 'losses': 0},
    'Player 2': {'wins': 0, 'draws': 0, 'losses': 0}
}


def main(gameOption, depth, num_games):
    # Czas rozpoczęcia gry
    start_time = time.time()

    for i in range(num_games):
        # Utworzenie nowej gry
        game = SixMensMorris()
        engine = Minimax(game)

        while not game.is_finished():
            moves = game.get_moves()
            if game.get_current_player() == game.first_player:
                # Gracz 1
                [_, move] = engine.get_best_move(game, depth)
            else:
                if gameOption == 1:
                    # Gracz 2
                    move = random.choice(moves)
                elif gameOption == 2:
                    [_, move] = engine.get_best_move(game, depth)
            game.make_move(move)

        # Ustalenie zwycięzcy lub remisu
        winner = game.get_winner()
        if winner is None:
            print(f'Game {i + 1}: Draw!')
            results['Player 1']['draws'] += 1
            results['Player 2']['draws'] += 1
        else:
            print(f'Game {i + 1}: Winner: Player {winner.char}')
            if winner.char == '1':
                results['Player 1']['wins'] += 1
                results['Player 2']['losses'] += 1
            else:
                results['Player 2']['wins'] += 1
                results['Player 1']['losses'] += 1

    # Czas zakończenia gry
    end_time = time.time()

    # Obliczenie czasu trwania gry
    duration = end_time - start_time

    # Wyświetlenie wyników
    print(f'\nResults:\n{"=" * 20}')
    print(
        f'Player 1: Wins={results["Player 1"]["wins"]}, Draws={results["Player 1"]["draws"]}, Losses={results["Player 1"]["losses"]}')
    print(
        f'Player 2: Wins={results["Player 2"]["wins"]}, Draws={results["Player 2"]["draws"]}, Losses={results["Player 2"]["losses"]}')
    print(f'\nDuration whole game: {duration:.2f} seconds')
    print(f'Duration single game: {duration/num_games:.2f} seconds')

    print(f"\nDepth of searching: {depth}")

if __name__ == "__main__":
    '''
    optionGame: 1 - MiniMax vs Random, 
                2 - MiniMax vs MiniMax
    depth: search depth
    num_games: number of games played
    '''
    main(gameOption=2, depth=2, num_games=100)
