from main import TicketPlayground


class TestTicketPlayground:
    def test_TicketPlayground_age_less_than_5(self):
        assert TicketPlayground(85, 4) == -1

    def test_TicketPlayground_age_more_than_12(self):
        assert TicketPlayground(140, 13) == 100000

    def test_TicketPlayground_age_between_5_and_7_height_more_than_120(self):
        assert TicketPlayground(121, 7) == 15000

    def test_TicketPlayground_age_between_5_and_7_height_more_than_135(self):
        assert TicketPlayground(136, 7) == 25000

    def test_TicketPlayground_age_between_5_and_7_height_more_than_150(self):
        assert TicketPlayground(151, 6) == 40000

    def test_TicketPlayground_age_between_5_and_7_height_more_than_160(self):
        assert TicketPlayground(161, 7) == 60000

    def test_TicketPlayground_age_between_8_and_9_height_more_than_120(self):
        assert TicketPlayground(121, 9) == 25000

    def test_TicketPlayground_age_between_8_and_9_height_more_than_135(self):
        assert TicketPlayground(136, 9) == 25000

    def test_TicketPlayground_age_between_8_and_9_height_more_than_150(self):
        assert TicketPlayground(151, 9) == 40000

    def test_TicketPlayground_age_between_8_and_9_height_more_than_160(self):
        assert TicketPlayground(161, 9) == 60000

    def test_TicketPlayground_age_between_10_and_11_height_more_than_120(self):
        assert TicketPlayground(121, 11) == 40000

    def test_TicketPlayground_age_between_10_and_11_height_more_than_135(self):
        assert TicketPlayground(136, 11) == 40000

    def test_TicketPlayground_age_between_10_and_11_height_more_than_150(self):
        assert TicketPlayground(151, 11) == 40000

    def test_TicketPlayground_age_between_10_and_11_height_more_than_160(self):
        assert TicketPlayground(161, 11) == 60000

    def test_TicketPlayground_age_equal_12_height_more_than_120(self):
        assert TicketPlayground(121, 12) == 60000

    def test_TicketPlayground_age_equal_12_height_more_than_135(self):
        assert TicketPlayground(136, 12) == 60000

    def test_TicketPlayground_age_equal_12_height_more_than_150(self):
        assert TicketPlayground(151, 12) == 60000

    def test_TicketPlayground_age_equal_12_height_more_than_160(self):
        assert TicketPlayground(161, 12) == 60000
