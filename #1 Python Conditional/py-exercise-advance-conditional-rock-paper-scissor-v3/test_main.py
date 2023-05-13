from main import rockPaperScissor


class TestrockPaperScissor:
    def test_Player_1_using_rock_Player(self):
        assert rockPaperScissor('rock', 'rock') == 'Draw!'
        assert rockPaperScissor('rock', 'paper') == 'Player 2 Won!'
        assert rockPaperScissor('rock', 'scissor') == 'Player 1 Won!'

    def test_Player_1_using_paper(self):
        assert rockPaperScissor('paper', 'rock') == 'Player 1 Won!'
        assert rockPaperScissor('paper', 'paper') == 'Draw!'
        assert rockPaperScissor('paper', 'scissor') == 'Player 2 Won!'

    def test_Player_1_using_scissor(self):
        assert rockPaperScissor('scissor', 'rock') == 'Player 2 Won!'
        assert rockPaperScissor('scissor', 'paper') == 'Player 1 Won!'
        assert rockPaperScissor('scissor', 'scissor') == 'Draw!'
