# [ ] create function, call and test 
def cheese_order(max_order=100.0, min_order=0.5, price_per_unit=7.99, order_amount=None):

    try:
        max_order = float(max_order)
        min_order = float(min_order)
        price_per_unit = float(price_per_unit)
        order_amount = float(order_amount)
    except ValueError:
        print("Invalid input. Please enter numeric values")
        return 


    user_name = "Brandon Watts"


    if order_amount > max_order:
        print(f"{user_name}, enter cheese order weight (numeric value): {order_amount}")
        print(f"{order_amount} is more than currently available stock")
    elif order_amount < min_order:
        print(f"{user_name}, enter cheese order weight (numeric value): {order_amount}")
        print(f"{order_amount} is below minimum order amount")
    else:
        total_price = order_amount * price_per_unit
        print(f"{user_name}, enter cheese order weight (numeric value): {order_amount}")
        print(f"{order_amount} costs ${total_price:.2f}")


order_weight_input = input("Enter cheese order weight (numeric value): ")


cheese_order(order_amount=order_weight_input)