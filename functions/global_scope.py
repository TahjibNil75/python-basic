coffe_type = "Espresso"  # Global scope

def serve_coffe():
    def kitchen():
        global coffe_type
        coffe_type = "Latte"
    kitchen()

serve_coffe
print(f"Order updated to: ", coffe_type )