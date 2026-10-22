# Lab 42 - Data Hiding with `@property` | Execution Proof

## Run command

```bash
python3 demo.py
```

## Actual terminal screenshots

The image below combines the three terminal screenshots supplied for Lab 42.

![Lab 42 terminal proof screenshots](proof/lab42-proof-images.jpg)

## Results captured

- Property-based price access and update worked.
- Direct access to `laptop.__price` was blocked as expected.
- A 15% discount changed $1,350.00 to $1,147.50.
- Inventory was restocked and stock was sold with the remaining quantity updated.
- Invalid prices, quantities, categories, sales, and discounts were rejected.
- Multiple product examples totalled **$43,175.00**.
- The terminal ended with **`Lab demo complete.`**
