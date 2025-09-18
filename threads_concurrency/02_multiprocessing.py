from multiprocessing import process

import time

def brew_coffe(name):
    print(f"Process {name}: Starting to brew coffee")
    time.sleep(3)
    print(f"Process {name}: Finished brewing coffee")


if __name__ == "__main__":
    coffe_makers = [
        process(target=brew_coffe, args=(f"CoffeMaker-{i+1}",)) 
        for i in range(3)
    ]

    for p in coffe_makers:
        p.start()

    for p in coffe_makers:
        p.join()

    print("All coffee brewed.")

