from main import BMICalculator
class TestBMICalculator:
    def test_laki_laki_165(self):
        assert BMICalculator("laki-laki", 165) == 58.5

    def test_laki_laki_170(self):
        assert BMICalculator("laki-laki", 170) == 63.00

    def test_laki_laki_160(self):
        assert BMICalculator("laki-laki", 160) == 54.00

    def test_laki_laki_155(self):
        assert BMICalculator("laki-laki", 155) == 49.5

    def test_perempuan_165(self):
        assert BMICalculator("perempuan", 165) == 55.25

    def test_perempuan_170(self):
        assert BMICalculator("perempuan", 170) == 59.5

    def test_perempuan_160(self):
        assert BMICalculator("perempuan", 160) == 51.00

    def test_perempuan_155(self):
        assert BMICalculator("perempuan", 155) == 46.75
