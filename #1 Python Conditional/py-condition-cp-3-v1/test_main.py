from main import GetPredicate


class TestGetPredicate:
    def test_for_average_score_100(self):
        assert GetPredicate(100, 100, 100, 100) == "Sempurna"

    def test_for_average_score_more_than_90(self):
        assert GetPredicate(90, 90, 90, 90) == "Sangat Baik"
        assert GetPredicate(92, 92, 95, 100) == "Sangat Baik"

    def test_for_average_score_more_than_80_and_less_90(self):
        assert GetPredicate(80, 80, 80, 80) == "Baik"
        assert GetPredicate(82, 85, 95, 80) == "Baik"

    def test_for_average_score_more_than_70_and_less_80(self):
        assert GetPredicate(75, 75, 75, 75) == "Cukup"
        assert GetPredicate(70, 70, 70, 90) == "Cukup"

    def test_for_average_score_more_than_60_and_less_70(self):
        assert GetPredicate(60, 65, 65, 65) == "Kurang"
        assert GetPredicate(60, 60, 60, 75) == "Kurang"

    def test_for_average_score_less_60(self):
        assert GetPredicate(50, 50, 50, 50) == "Sangat kurang"
        assert GetPredicate(50, 50, 50, 60) == "Sangat kurang"
