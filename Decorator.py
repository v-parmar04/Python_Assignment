def discount_decorator(func):

    def wrapper(base_price):
        price = func(base_price)
        print("This is discount decorator")       
        discount_amount = price * 10 / 100
        discount_price = price - discount_amount
        print(discount_price)
        return discount_price
    
    return wrapper

def tax_decorator(func):

    def wrapper(base_price):
        price = func(base_price)
        print("This is tax decorator")       
        discount_amount = price * 18 / 100
        final_price_after_tax = price - discount_amount
        return final_price_after_tax
    
    return wrapper

@tax_decorator
@discount_decorator
def calcualte_flight_price(base_price):
    
    print("Base Price = ", base_price)
    return base_price

print(calcualte_flight_price(5000))
