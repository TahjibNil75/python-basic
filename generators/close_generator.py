def local_coffe():
    yield "Local Coffee 1"
    yield "Local Coffee 2"

def imported_coffe():
    yield "Imported Coffee 1"
    yield "Imported Coffee 2"


def full_menu():
    yield from local_coffe()
    yield from imported_coffe()

for coffe in full_menu():
    print(coffe)


def coffe_shop():
    try:
        while True:
            order = yield "waiting for coffee"

    except:
        print(f"Stall is closed")


shop = coffe_shop()
print(next(shop))
shop.close  ### gracefull close the generator which also cleans up the memory 