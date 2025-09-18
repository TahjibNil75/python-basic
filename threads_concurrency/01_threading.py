import threading
import time

def take_orders():
    for i in range(5):
        print(f"Taking order {i + 1}")
        time.sleep(1)  # Simulate time taken to take an order


def process_payments():
    for i in range(5):
        print(f"Processing payment {i + 1}")
        time.sleep(2)  # Simulate time taken to process a payment


def brew_coffe():
    for i in range(5):
        print(f"Brewing coffee {i + 1}")
        time.sleep(3)

## Create Threads
order_thread = threading.Thread(target=take_orders)
payment_thread = threading.Thread(target=process_payments)
brew_thread = threading.Thread(target=brew_coffe)


## Start Threads
order_thread.start()
payment_thread.start()
brew_thread.start()

## Wait for all threads to complete
order_thread.join()
payment_thread.join()
brew_thread.join()

print("All tasks completed.")