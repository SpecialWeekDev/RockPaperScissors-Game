score = {
    "wins": 0,
    "losses": 0,
    "ties": 0
}

def update_score(result):
    if result == "You win!":
        score["wins"] += 1
    elif result == "Computer win!":
        score["losses"] += 1
    else:
        score["ties"] += 1

def get_win():
    return score["wins"]

def get_loss():
    return score["losses"]

def get_tie():
    return score["ties"]

def get_score():
    return score