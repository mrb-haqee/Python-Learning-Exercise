from main import resistorValue

class TestresistorValue:
    def test_resistorValue_not_null(self):
        assert resistorValue('brown', 'black', 'red', 'gold') is not None
        assert resistorValue('red', 'red', 'red', 'gold') is not None
        assert resistorValue('yellow', 'violet', 'green', 'silver') is not None

    def test_resistorValue_brown_black_red_gold(self):
        assert resistorValue('brown', 'black', 'red', 'gold') == '1000 ohm ±5%'

    def test_resistorValue_red_red_red_gold(self):
        assert resistorValue('red', 'red', 'red', 'gold') == '2200 ohm ±5%'

    def test_resistorValue_yellow_violet_green_silver(self):
        assert resistorValue('yellow', 'violet', 'green', 'silver') == '4700000 ohm ±10%'

    def test_resistorValue_yellow_green_green_silver(self):
        assert resistorValue('yellow', 'green', 'green', 'silver') == '4500000 ohm ±10%'

    def test_resistorValue_blue_green_violet_gold(self):
        assert resistorValue('blue', 'green', 'violet', 'gold') == '650000000 ohm ±5%'
