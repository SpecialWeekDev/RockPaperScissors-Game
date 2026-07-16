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

def get_score():
    return score