from main import GetTicketPrice


class TestGetTicketPrice:
    def test_for_when_total_price_ticket_is_less_than_100(self):
        assert GetTicketPrice(1, 1, 1, 20) == 60.0
        assert GetTicketPrice(0, 0, 5, 1) == 50.0
        assert GetTicketPrice(1, 0, 6, 15) == 90.0

    def test_for_when_total_price_ticket_is_more_than_or_equal_to_100(self):
        assert GetTicketPrice(4, 0, 0, 13) == 102.0
        assert GetTicketPrice(3, 3, 3, 20) == 144.0
        assert GetTicketPrice(4, 4, 4, 20) == 192.0

    def test_for_even_days(self):
        assert GetTicketPrice(4, 0, 0, 20) == 108.0
        assert GetTicketPrice(3, 3, 3, 22) == 144.0
        assert GetTicketPrice(4, 4, 4, 22) == 192.0
