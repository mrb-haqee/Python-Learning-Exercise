from main import mineralMining


class TestmineralMining:
    def test_invalid_mineral_name(self):
        assert mineralMining('rock', 10, 70, 40) == 'Invalid mineral name'
        assert mineralMining('diamond', 10, 70, 40) == 'Invalid mineral name'

    def test_mineral_mining_profit(self):
        assert mineralMining('silver', 33, 200, 30) == 'Mineral mining profit 168'
        assert mineralMining('gold', 50, 400, 150) == 'Mineral mining profit 516.6666666666667'
        assert mineralMining('titanium', 20, 350,150) == 'Mineral mining profit 40.90909090909091'
