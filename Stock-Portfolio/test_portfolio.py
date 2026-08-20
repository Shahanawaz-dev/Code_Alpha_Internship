import pytest

from portfolio import Portfolio, Stock


def test_stock_creation():
    stock = Stock("tcs", 10, 3500)

    assert stock.symbol == "TCS"
    assert stock.quantity == 10
    assert stock.purchase_price == 3500
    assert stock.investment_value == 35000


def test_add_stock():
    portfolio = Portfolio()

    portfolio.add_stock("TCS", 10, 3500)

    stock = portfolio.get_stock("TCS")

    assert stock.quantity == 10
    assert stock.purchase_price == 3500


def test_add_existing_stock():
    portfolio = Portfolio()

    portfolio.add_stock("TCS", 10, 3000)
    portfolio.add_stock("TCS", 10, 4000)

    stock = portfolio.get_stock("TCS")

    assert stock.quantity == 20
    assert stock.purchase_price == 3500


def test_remove_stock():
    portfolio = Portfolio()

    portfolio.add_stock("TCS", 10, 3500)
    portfolio.remove_stock("TCS", 4)

    stock = portfolio.get_stock("TCS")

    assert stock.quantity == 6


def test_remove_all_stock():
    portfolio = Portfolio()

    portfolio.add_stock("TCS", 10, 3500)
    portfolio.remove_stock("TCS", 10)

    assert portfolio.get_stock("TCS") is None


def test_total_investment():
    portfolio = Portfolio()

    portfolio.add_stock("TCS", 10, 3500)
    portfolio.add_stock("INFY", 5, 1500)

    assert portfolio.total_investment() == 42500


def test_invalid_quantity():
    portfolio = Portfolio()

    with pytest.raises(ValueError):
        portfolio.add_stock("TCS", 0, 3500)


def test_invalid_price():
    portfolio = Portfolio()

    with pytest.raises(ValueError):
        portfolio.add_stock("TCS", 10, -100)


def test_remove_more_than_owned():
    portfolio = Portfolio()

    portfolio.add_stock("TCS", 5, 3500)

    with pytest.raises(ValueError):
        portfolio.remove_stock("TCS", 10)