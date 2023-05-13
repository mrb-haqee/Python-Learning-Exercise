from main import hollyKnight


class TesthollyKnight:
    def test_hollyKnight_win(self):
        assert hollyKnight('Lancelot', 30, 20) == 'Holly Knight Lancelot memenangkan pertempuran dengan mudah!'
        assert hollyKnight('Gareth', 100, 10) == 'Holly Knight Gareth memenangkan pertempuran dengan mudah!'

    def test_hollyKnight_win_hard(self):
        assert hollyKnight('Gallahad', 10, 10) == 'Beruntung Holly knight Gallahad berhasil mengalahkan 10 undead!'
        assert hollyKnight('Lancelot', 60, 60) == 'Beruntung Holly knight Lancelot berhasil mengalahkan 60 undead!'

    def test_hollyKnight_defeat(self):
        assert hollyKnight('Gareth', 30, 50) == 'Holly knight Gareth mengalahkan 30 undead, namun sayang holly knight Gareth gugur di medan perang!'
        assert hollyKnight('Percival', 99, 100) == 'Holly knight Percival mengalahkan 99 undead, namun sayang holly knight Percival gugur di medan perang!'
