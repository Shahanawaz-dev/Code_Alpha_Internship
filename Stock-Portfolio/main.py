from portfolio import Portfolio


def get_positive_number(prompt, number_type=float):
    """Get a positive numerical value from the user."""
    while True:
        try:
            value = number_type(input(prompt).strip())

            if value <= 0:
                print("Please enter a value greater than zero.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def add_stock(portfolio):
    """Handle adding a stock to the portfolio."""
    symbol = input("Enter stock symbol: ").strip().upper()

    if not symbol:
        print("Stock symbol cannot be empty.")
        return

    quantity = get_positive_number(
        "Enter quantity: ",
        int
    )

    price = get_positive_number(
        "Enter purchase price: ₹"
    )

    try:
        portfolio.add_stock(symbol, quantity, price)
        print(f"{symbol} added successfully.")

    except ValueError as error:
        print(f"Error: {error}")


def remove_stock(portfolio):
    """Handle removing a stock."""
    symbol = input("Enter stock symbol: ").strip().upper()

    quantity = get_positive_number(
        "Enter quantity to remove: ",
        int
    )

    try:
        portfolio.remove_stock(symbol, quantity)
        print(f"{quantity} shares of {symbol} removed.")

    except ValueError as error:
        print(f"Error: {error}")


def view_portfolio(portfolio):
    """Display portfolio information."""
    print(portfolio.portfolio_summary())


def main():
    """Run the portfolio management application."""
    portfolio = Portfolio()

    print("=" * 55)
    print("           STOCK PORTFOLIO MANAGER")
    print("=" * 55)

    while True:
        print("\nMenu")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. View portfolio")
        print("4. View total investment")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_stock(portfolio)

        elif choice == "2":
            remove_stock(portfolio)

        elif choice == "3":
            view_portfolio(portfolio)

        elif choice == "4":
            total = portfolio.total_investment()
            print(f"Total Investment: ₹{total:.2f}")

        elif choice == "5":
            print("Thank you for using Stock Portfolio Manager!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()