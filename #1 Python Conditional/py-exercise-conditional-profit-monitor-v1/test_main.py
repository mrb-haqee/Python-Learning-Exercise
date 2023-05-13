from main import profitMonitor


class TestprofitMonitor:
    def test_not_null(self):
        assert profitMonitor(100, 50) is not None

    def test_profit_increase(self):
        assert profitMonitor(100, 50) == 'Profit naik sebanyak 50 point'
        assert profitMonitor(200, 100) == 'Profit naik sebanyak 100 point'

    def test_profit_decrease(self):
        assert profitMonitor(50, 100) == 'Profit turun sebanyak 50 point'
        assert profitMonitor(100, 200) == 'Profit turun sebanyak 100 point'

    def test_profit_stabil(self):
        assert profitMonitor(100, 100) == 'Profit stabil'
        assert profitMonitor(200, 200) == 'Profit stabil'
