# Lab 42 - Data Hiding with `@property` | Execution Proof

## Run command

```bash
python3 demo.py
```

## Terminal evidence

The screenshots below are the actual terminal outputs supplied for this lab.

### Screenshot 1: Property access, data hiding, discount, and inventory operations

![Lab 42 proof screenshot 1](proof/lab42-proof-1.jpg)

### Screenshot 2: Validation checks and multiple products

![Lab 42 proof screenshot 2](proof/lab42-proof-2.jpg)

### Screenshot 3: Final inventory total and successful completion

![Lab 42 proof screenshot 3](proof/lab42-proof-3.jpg)

## Results captured

- Property-based price access and update worked.
- Direct access to `laptop.__price` was blocked as expected.
- A 15% discount changed $1,350.00 to $1,147.50.
- Inventory was restocked and stock was sold with the remaining quantity updated.
- Invalid prices, quantities, categories, sales, and discounts were rejected.
- Multiple product examples totalled **$43,175.00**.
- The terminal ended with **`Lab demo complete.`**
