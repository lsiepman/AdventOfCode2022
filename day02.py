# functions

def calc_score(result):
    """Calculates score of a game based on its result

    Args:
        result (str): Result of the game, win, loss, or draw.

    Returns:
        int: score
    """    
    if result == "win":
        return 6
    elif result == "draw":
        return 3
    elif result == "loss":
        return 0
    else:
        raise ValueError("Unknown result type")

def define_result(hand1, hand2):
    """Defines whether a game is won, draw, or lost for hand1

    Args:
        hand1 (str): one of rock, paper, scissors. Result is defined for this hand
        hand2 (str): one of rock, paper, scissors

    Raises:
        ValueError: When an unknown hand is entered

    Returns:
        str: result string, win, draw, or loss
    """    
    if hand1 == hand2:
        return "draw"
    elif hand1 == "rock" and hand2 == "paper":
        return "loss"
    elif hand1 == "rock" and hand2 == "scissors":
        return "win"
    elif hand1 == "paper" and hand2 == "scissors":
        return "loss"
    elif hand1 == "paper" and hand2 == "rock":
        return "win"
    elif hand1 == "scissors" and hand2 == "rock":
        return "loss"
    elif hand1 == "scissors" and hand2 == "paper":
        return "win"
    else:
        raise ValueError("One or more hands are unknown")

def calc_hand(hand):
    """Calculates the score of a handshape

    Args:
        hand (str): one of rock, paper, scissors

    Raises:
        ValueError: If an invalid hand is used

    Returns:
        int: score value
    """    
    if hand == "rock":
        return 1
    elif hand == "paper":
        return 2
    elif hand == "scissors":
        return 3
    else:
        raise ValueError("Invalid hand")

def convert_shape(hand):
    """Convert shape abbreviation into shap

    Args:
        hand (str): One of A, B, C or X, Y, Z

    Returns:
        str: shape, one of rock, paper, scissors
    """    
    if hand in ["X", "A"]:
        return "rock"
    elif hand in ["Y", "B"]:
        return "paper"
    elif hand in ["Z", "C"]:
        return "scissors"
    else:
        return hand

def need_result(instructions):
    """Determine the result needed based on the hand instructions

    Args:
        instructions (str): instructions given, one of X, Y, Z

    Raises:
        ValueError: Invalid instructions

    Returns:
        result: Result needed, one of loss, draw, win
    """    
    if instructions == "X":
        return "loss"
    elif instructions == "Y":
        return "draw"
    elif instructions == "Z":
        return "win"
    else:
        raise ValueError("Invalid instructions")

def pick_hand(opp_hand, result):
    if result == "draw":
        return opp_hand

    if result == "win":
        if opp_hand == "rock":
            return "paper"
        elif opp_hand == "paper":
            return "scissors"
        elif opp_hand == "scissors":
            return "rock"
        else:
            raise ValueError("Invalid combination")
    elif result == "loss":
        if opp_hand == "rock":
            return "scissors"
        elif opp_hand == "paper":
            return "rock"
        elif opp_hand == "scissors":
            return "paper"
        else:
            raise ValueError("Invalid combination")
    else:
        raise ValueError("Invalid combination")

def calc_total_score(data, part):
    game = [(convert_shape(i), convert_shape(j)) for i,j in zip(data["opponent"], data["you"])]
    game_results = sum([calc_score(define_result(j,i)) for i,j in game])
    hand_results = sum(calc_hand(i[1]) for i in game)

    print(f"The answer to part {part} = {game_results + hand_results}")


if __name__ == "__main__":
    # read data
    data = {"opponent": [], "you": []}

    with open("./input/day02.txt") as f:
        for line in f:
            x,y = line.strip().split()
            data["opponent"].append(x)
            data["you"].append(y)

    # part 1
    calc_total_score(data, 1)

    # part 2
    intended_results = [need_result(i) for i in data["you"]]
    dat_opp = [convert_shape(i) for i in data["opponent"]]
    moves = [pick_hand(i,j) for i,j in zip(dat_opp, intended_results)]
    game2_data = {"opponent": data["opponent"], "you": moves}
    calc_total_score(game2_data, 2)