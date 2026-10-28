"""
improved_code.py
Refactored shopping cart billing system using clean architecture principles and AI assistance.
Author: Golu Kumar
University: JECRC University, Jaipur
"""

from dataclasses import dataclass
from typing import List

# Business rule constants
STANDARD_TAX_RATE = 0.18
DISCOUNT_TIERS = (
    (50000.0, 0.15),
    (20000.0, 0.10),
    (5000.0, 0.05),
)

@dataclass(frozen=True)
class Item:
    name: str
    unit_price: float
    quantity: int

    @property
    def subtotal(self) -> float:
        return round(self.unit_price * self.quantity, 2)


@dataclass(frozen=True)
class InvoiceLine:
    item: Item
    subtotal: float
    discount_amount: float
    taxable_amount: float
    tax_amount: float
    line_total: float


class BillingCalculator:
    """Encapsulates pricing, tiered discounts, and tax computation."""

    @staticmethod
    def calculate_discount(subtotal: float) -> float:
        """Determines tiered discount based on item volume."""
        for threshold, rate in DISCOUNT_TIERS:
            if subtotal > threshold:
                return round(subtotal * rate, 2)
        return 0.0

    @classmethod
    def process_item(cls, item: Item) -> InvoiceLine:
        """Computes discounts, taxes, and final payable amount for a single cart item."""
        subtotal = item.subtotal
        discount = cls.calculate_discount(subtotal)
        taxable = subtotal - discount
        tax = round(taxable * STANDARD_TAX_RATE, 2)
        total = round(taxable + tax, 2)

        return InvoiceLine(
            item=item,
            subtotal=subtotal,
            discount_amount=discount,
            taxable_amount=taxable,
            tax_amount=tax,
            line_total=total
        )

    @classmethod
    def generate_invoice(cls, items: List[Item]) -> None:
        """Prints a formatted invoice summary table."""
        print("=" * 80)
        print(f"{'Item Name':<16} {'Price':>10} {'Qty':>5} {'Subtotal':>10} {'Discount':>10} {'Tax(18%)':>10} {'Total':>12}")
        print("-" * 80)

        grand_total = 0.0
        for item in items:
            line = cls.process_item(item)
            grand_total += line.line_total
            print(
                f"{line.item.name:<16} "
                f"₹{line.item.unit_price:>9.2f} "
                f"{line.item.quantity:>5} "
                f"₹{line.subtotal:>9.2f} "
                f"₹{line.discount_amount:>9.2f} "
                f"₹{line.tax_amount:>9.2f} "
                f"₹{line.line_total:>11.2f}"
            )

        print("=" * 80)
        print(f"{'GRAND TOTAL PAYABLE:':<64} ₹{grand_total:>12.2f}")
        print("=" * 80)


def main():
    cart = [
        Item(name="Laptop", unit_price=55000.0, quantity=2),
        Item(name="Mouse", unit_price=600.0, quantity=5),
        Item(name="Keyboard", unit_price=1500.0, quantity=3),
        Item(name="Monitor", unit_price=12000.0, quantity=1),
    ]

    BillingCalculator.generate_invoice(cart)


if __name__ == "__main__":
    main()
