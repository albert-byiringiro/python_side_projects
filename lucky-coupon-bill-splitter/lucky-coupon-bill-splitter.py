import random

def split_bill_with_coupon(orders, seed):
    if not orders:
        return {}
    
    totals = {}
    
    for name, prices in orders.items():
        subtotal = 0
        for item in prices:
            try:
                value = int(item);
                if value >= 0:
                    subtotal += value
            except (ValueError, TypeError):
                continue
        totals[name] = subtotal
    
    random.seed(seed)
    lucky_winner = random.choice(list(totals.keys()))
    
    totals[lucky_winner] = max(0, totals[lucky_winner] - 300)
    
    return totals


orders = {
    "Ava": [500, "250", "bad"],
    "Ben": [300, 200],
}

print(split_bill_with_coupon(orders, 2))
