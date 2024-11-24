import random
from RPS import player

# This function simulates a match between two players
def play(player1, player2, num_games, verbose=False):
    score1 = 0
    score2 = 0

    for i in range(num_games):
        prev_play1 = ""
        prev_play2 = ""
        move1 = player1(prev_play2)  # Player 1's move
        move2 = player2(prev_play1)  # Player 2's move

        # Determine the winner of the round
        if move1 == "R" and move2 == "S" or \
           move1 == "P" and move2 == "R" or \
           move1 == "S" and move2 == "P":
            score1 += 1
        elif move1 == move2:
            continue
        else:
            score2 += 1

        prev_play1 = move1
        prev_play2 = move2

        if verbose:
            print(f"Game {i+1}: Player 1 played {move1}, Player 2 played {move2}")

    print(f"Final Score: Player 1 - {score1}, Player 2 - {score2}")
    return score1, score2

# Test the bot by playing 1000 games and displaying detailed results
if __name__ == "__main__":
    play(player, player, 1000, verbose=True)
