def discount_price(discount):
    discount = 1 - discount
    
    
    def calcucation(p):
        return p * discount

    return calcucation

cost_05 =   discount_price(0.05)

price = 100

print(cost_05(price))
    