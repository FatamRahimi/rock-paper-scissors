import random

# This function decides the next move for the bot based on the previous play
def player(prev_play, opponent_history=[]):
    # If it's the first game, the bot picks a random move
    if prev_play == "":
        return random.choice(["R", "P", "S"])

    # Store the opponent's previous moves
    opponent_history.append(prev_play)
    
    # Simple strategy to counter the opponent's last move
    if prev_play == "R":
        return "P"  # "P" beats "R"
    elif prev_play == "P":
        return "S"  # "S" beats "P"
    elif prev_play == "S":
        return "R"  # "R" beats "S"
    
    # If something goes wrong, the bot picks a random move
    return random.choice(["R", "P", "S"])
