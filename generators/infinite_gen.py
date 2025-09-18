def coffe_refill():
    count = 1

    while True:
        yield f"Refill #{count}"
        count += 1

User1 = coffe_refill()

for _ in range(5):
    print(next(User1))

user2 = coffe_refill()
for _ in range(3):
    print(next(user2))    
