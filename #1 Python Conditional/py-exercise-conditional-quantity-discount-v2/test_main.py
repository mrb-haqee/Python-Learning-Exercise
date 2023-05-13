from main import quantityDiscount


class TestquantityDiscount:
    def test_quantityDiscount_not_null(self):
        assert quantityDiscount(1, 100) is not None
        assert quantityDiscount(3, 100) is not None
        assert quantityDiscount(5, 100) is not None
        assert quantityDiscount(10, 100) is not None
        assert quantityDiscount(15, 3) is not None

    def test_quantityDiscount_quantity_less_than_5(self):
        assert quantityDiscount(1, 100) == 111
        assert quantityDiscount(3, 100) == 333

    def test_quantityDiscount_quantity_more_than_5_and_less_than_10(self):
        assert quantityDiscount(5, 100) == 471.75
        assert quantityDiscount(6, 100) == 566.1
        assert quantityDiscount(9, 100) == 849.15

    def test_quantityDiscount_quantity_more_than_10(self):
        assert quantityDiscount(10, 100) == 888
        assert quantityDiscount(15, 3) == 39.96
