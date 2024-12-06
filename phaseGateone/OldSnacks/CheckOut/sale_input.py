class SaleInput:
    def __init__(self):
        self.customer = ""
        self.product = []
        self.unit = []
        self.price = []
        self.cashier = ""
    
    def set_customer(self, customer):
        self.customer = customer
    
    def get_customer(self):
        return self.customer
    
    def set_product(self, product_name):
        self.product.append(product_name)
    
    def get_product(self, index):
        return self.product[index]
    
    def set_unit(self, unit_quantity):
        self.unit.append(unit_quantity)
    
    def get_unit(self, index):
        return self.unit[index]
    
    def set_price(self, price_per_unit):
        self.price.append(price_per_unit)
    
    def get_price(self, index):
        return self.price[index]
    
    def set_cashier(self, cashier_name):
        self.cashier = cashier_name
    
    def get_cashier(self):
        return self.cashier