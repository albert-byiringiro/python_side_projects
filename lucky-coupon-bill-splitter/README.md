# Lucky Coupon Bill Splitter

**Complete the `split_bill_with_coupon` function**.

You are building a small bill-splitting helper for a group meal.

The function should:

1. Go through the `orders` dictionary.
2. Add up each person's item prices.
3. Some prices may be strings like `"250"` instead of integers.
4. If a price cannot be turned into an integer, ignore it.
5. If a price is negative, ignore it.
6. Use `random.seed(seed)` and then pick **one random person** from the dictionary keys.
7. Give that person a `300` cent discount.
8. A person's final total should never go below `0`.
9. Return a dictionary mapping each person to their final total in cents.

Use loops to process the dictionary and each person's list of prices.

## Notes

- The `random` module lets you pick a random value. In this challenge, the seed makes the result predictable for testing.
- Use `try`/`except` when converting prices with `int(...)`.
- If `orders` is empty, return an empty dictionary.

## Example

```py
orders = {
    "Ava": [500, "250", "bad"],
    "Ben": [300, 200],
}

print(split_bill_with_coupon(orders, 1))
```

One possible result is:

```py
{"Ava": 450, "Ben": 500}
```

Explanation:

- Ava's valid prices are `500` and `250` -> subtotal `750`
- Ben's subtotal is `500`
- With this seed, Ava is chosen for the `300` cent discount
- Ava's final total becomes `450`