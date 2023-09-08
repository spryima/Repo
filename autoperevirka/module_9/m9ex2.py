DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    customer ={1: 23}
    price = price * (1 - customer.get("discount", DEFAULT_DISCOUNT))
    return price
    
        
    