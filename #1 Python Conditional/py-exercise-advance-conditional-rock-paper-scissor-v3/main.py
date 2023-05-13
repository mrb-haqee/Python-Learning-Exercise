def rockPaperScissor(player1: str, player2: str) -> str:
    match player1:
        case "rock":
            match player2:
                case "rock":
                    return "Draw!"
                case "paper":
                    return "Player 2 Won!"
                case "scissor":
                    return "Player 1 Won!"
        case "paper":
            match player2:
                case "rock":
                    return "Player 1 Won!"
                case "paper":
                    return "Draw!"
                case "scissor":
                    return "Player 2 Won!"
        case "scissor":
            match player2:
                case "rock":
                    return "Player 2 Won!"
                case "paper":
                    return "Player 1 Won!"
                case "scissor":
                    return "Draw!"
    # return ""  # TODO: replace this


if __name__ == "__main__":
    print(rockPaperScissor("scissor", "paper"))  # "Player 1 Won!"
    print(rockPaperScissor("rock", "paper"))  # "Player 2 Won!"
    print(rockPaperScissor("paper", "paper"))  # "Draw!"
    print(rockPaperScissor("rock", "rock"))  # "Draw!"
