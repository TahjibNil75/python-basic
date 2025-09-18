seat_type = input("Enter seat type (economy/business/first/sleeper): ").strip().lower()

match seat_type:
    case "economy":
        print("Economy - Chepest option, basic amenities.")
    case "business":
        print("Business - More space, better service.")
    case "first":
        print("First - Luxury experience, top-notch service.")
    case "sleeper":
        print("Sleeper - Comfortable sleeping arrangements.")   
    case _:
        print("Invalid seat type. Please choose economy, business, first, or sleeper.")