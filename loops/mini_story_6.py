users = [
    {"id": 1, "total": 100, "coupon_code": "SJKE30"},
    {"id": 2, "total": 150, "coupon_code": "SAYU60"},
    {"id": 3, "total": 80, "coupon_code": "NMVE10"},
]

discounts = {
    "SJKE30": (0.2, 0),
    "SAYU60": (0.5, 0),
    "NMVE10": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon_code"], (0, 0))
    discounts_amount = user["total"] * percent + fixed
    print(f"{user['id']} paid {user['total']} and got discount for next visit of taka {discounts_amount}.")
