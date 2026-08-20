class Stock:
    """Represents a stock holding."""

    def __init__(self, symbol, quantity, purchase_price):
        self.symbol = symbol.upper()
        self.quantity = quantity
        self.purchase_price = purchase_price

    @property
    def investment_value(self):
        return self.quantity * self.purchase_price


class Portfolio:
    """Manages a collection of stock holdings."""

    def __init__(self):
        self.holdings = {}

    def add_stock(self, symbol, quantity, purchase_price):
        """Add a stock or increase an existing holding."""
        symbol = symbol.upper()

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if purchase_price <= 0:
            raise ValueError("Purchase price must be greater than zero.")

        if symbol in self.holdings:
            stock = self.holdings[symbol]

            total_quantity = stock.quantity + quantity
            total_cost = stock.investment_value + (
                quantity * purchase_price
            )

            stock.quantity = total_quantity
            stock.purchase_price = total_cost / total_quantity

        else:
            self.holdings[symbol] = Stock(
                symbol,
                quantity,
                purchase_price
            )

    def remove_stock(self, symbol, quantity):
        """Remove a specified quantity of a stock."""
        symbol = symbol.upper()

        if symbol not in self.holdings:
            raise ValueError("Stock not found in portfolio.")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        stock = self.holdings[symbol]

        if quantity > stock.quantity:
            raise ValueError("You do not own that many shares.")

        stock.quantity -= quantity

        if stock.quantity == 0:
            del self.holdings[symbol]

    def get_stock(self, symbol):
        """Return a stock holding."""
        return self.holdings.get(symbol.upper())

    def total_investment(self):
        """Calculate total amount invested."""
        return sum(
            stock.investment_value
            for stock in self.holdings.values()
        )

    def portfolio_summary(self):
        """Return a formatted portfolio summary."""
        if not self.holdings:
            return "Portfolio is empty."

        lines = []
        lines.append("\nPortfolio Summary")
        lines.append("-" * 55)

        for stock in self.holdings.values():
            lines.append(
                f"{stock.symbol:<10}"
                f"Quantity: {stock.quantity:<8}"
                f"Avg Price: ₹{stock.purchase_price:.2f}   "
                f"Value: ₹{stock.investment_value:.2f}"
            )

        lines.append("-" * 55)
        lines.append(
            f"Total Investment: ₹{self.total_investment():.2f}"
        )

        return "\n".join(lines)