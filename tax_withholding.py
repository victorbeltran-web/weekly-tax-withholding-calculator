"""
Weekly Tax Withholding Calculator
----------------------------------
Calculates the tax withheld from a customer's weekly income based on the
following bracket guidelines, then reports the average weekly income and
average weekly tax withholding across all customers entered in a session.

    Income < $500                       -> 10% tax rate
    $500  <= Income < $1500             -> 15% tax rate
    $1500 <= Income < $2500             -> 20% tax rate
    Income >= $2500                     -> 30% tax rate

Author: Computer (Perplexity)
"""


def calculate_tax(weekly_income: float) -> float:
    """Return the tax rate (as a decimal) that applies to a weekly income."""
    if weekly_income < 500:
        return 0.10
    elif weekly_income < 1500:
        return 0.15
    elif weekly_income < 2500:
        return 0.20
    else:
        return 0.30


def get_weekly_income() -> float:
    """Prompt the user for a weekly income value, validating the input."""
    while True:
        raw_value = input("Enter weekly income for customer (or -1 to stop): $")
        try:
            income = float(raw_value)
        except ValueError:
            print("Error: please enter a valid number.\n")
            continue

        if income == -1:
            return income

        if income < 0:
            print("Error: income cannot be negative. Please try again.\n")
            continue

        return income


def main():
    print("=" * 50)
    print("   WEEKLY TAX WITHHOLDING CALCULATOR")
    print("=" * 50)

    customer_count = 0
    total_income = 0.0
    total_tax = 0.0

    while True:
        weekly_income = get_weekly_income()

        if weekly_income == -1:
            break

        rate = calculate_tax(weekly_income)
        tax_withheld = weekly_income * rate

        print(f"  -> Tax rate applied : {rate * 100:.0f}%")
        print(f"  -> Tax withheld     : ${tax_withheld:,.2f}\n")

        total_income += weekly_income
        total_tax += tax_withheld
        customer_count += 1

    print("-" * 50)
    if customer_count > 0:
        average_income = total_income / customer_count
        average_tax = total_tax / customer_count

        print("SUMMARY")
        print(f"Customers processed          : {customer_count}")
        print(f"Total weekly income          : ${total_income:,.2f}")
        print(f"Total tax withheld           : ${total_tax:,.2f}")
        print(f"Average weekly income        : ${average_income:,.2f}")
        print(f"Average weekly tax withholding: ${average_tax:,.2f}")
    else:
        print("No customer data was entered.")
    print("-" * 50)


if __name__ == "__main__":
    main()
