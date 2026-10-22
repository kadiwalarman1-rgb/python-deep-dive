# Lab 42 - Execution Proof

## Run command

```bash
python3 demo.py
```

## Observed results

The terminal run completed and displayed `Lab demo complete.`

### Property and data hiding
- Product: Gaming Laptop
- Initial price: $1,200.00
- Reading the price through the property worked.
- Direct access to `laptop.__price` was blocked as expected.
- Name-mangled attribute demonstration showed $1,200.00.
- Updated price: $1,350.00
- Price after 15% discount: $1,147.50

### Inventory and OOP behavior
- Gaming Laptop: price $1,500.00, initial quantity 25.
- Total inventory value: $37,500.00.
- Restocked 20 units, bringing quantity to 45.
- Sold 15 units, revenue $22,500.00, remaining quantity 30.
- Updated inventory value: $45,000.00.

### Validation checks
All displayed validation checks passed:
- Negative price rejected.
- Text price rejected.
- Excessive price rejected.
- Negative quantity rejected.
- Fractional quantity rejected.
- Invalid category rejected.
- Selling more than available stock rejected.
- Invalid discount rejected.

### Multiple products
The demo printed information for:
- Smartphone: $800.00, quantity 50, inventory value $40,000.00.
- T-Shirt: $25.00, quantity 100, inventory value $2,500.00.
- Python Book: $45.00, quantity 15, inventory value $675.00.

**Total inventory value:** $43,175.00.

## Evidence note

These details are transcribed from the terminal screenshots provided for Lab 42. The screenshots themselves have not been uploaded as image files in this repository yet.
