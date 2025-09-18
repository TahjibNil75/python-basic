player_attributes = dict(
    type="forward",
    position="LW",
    number="10"
)
print(f"Details: {player_attributes}")



accessories = {}
accessories["gloves"] = "red"
accessories["ball"] = "blue"
accessories["shoes"] = "black"
print(f"Accessories: {accessories}")

print(f"player ball: {accessories['ball']}")
del accessories["gloves"]
print(f"Updated Accessories: {accessories}")


accessories_order = {
    "type":"Ball",
    "color":"white",
    "size":"5",
    "brand":"Nike",
}

# print(f"order details (keys): {accessories_order.keys()}")
# print(f"order details (values): {accessories_order.values()}")
# print(f"order details (items): {accessories_order.items()}")

last_item = accessories_order.popitem()
print(f"Last item removed: {last_item}")
print(f"Updated order details: {accessories_order}")


extra_accessories = {"socks": "white", "headband": "black"}
accessories_order.update(extra_accessories)
print(f"Updated order details after adding extra accessories: {accessories_order}")

ball_size = accessories_order.get("size")
print(f"Ball size: {ball_size}")

brand_name = accessories_order.get("brand", "Unknown Brand")
print(f"Brand name: {brand_name}")