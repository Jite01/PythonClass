from datetime import datetime
from sale_input import SaleInput  
class InvoiceReceipt:
    def __init__(self):
        self.my_invoice = SaleInput()
        self.discount = 0
        self.sub_total = 0
        self.actual_discount = 0
        self.vat = 0
        self.total = 0
        self.amount_paid = 0
        self.balance = 0

    def sales_desk_insert(self):
        add_to_invoice_action = "yes"
        
        while add_to_invoice_action.lower() != "no":
            product_name = input("What did the user buy? ")
            self.my_invoice.set_product(product_name)

            unit_quantity = float(input("How many pieces? "))
            self.my_invoice.set_unit(unit_quantity)

            price_per_unit = float(input("How much per unit? "))
            self.my_invoice.set_price(price_per_unit)

            add_to_invoice_action = input("Add more Items? ")

    def invoice_input(self):
        customer_name = input("What is the customer's Name? ")
        self.my_invoice.set_customer(customer_name)

        self.sales_desk_insert()

        cashier_name = input("What is your name? ")
        self.my_invoice.set_cashier(cashier_name)

        self.discount = float(input("How much discount will he get? "))

    def display_invoice(self):
        current_time = datetime.now().strftime("%d-%b-%y %I:%M:%S %p")

        print("""
SEMICOLON STORES
MAIN BRANCH
LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.
TEL: 03293828343
DATE: {}
""".format(current_time))

        print(f"Cashier:  {self.my_invoice.get_cashier()}")
        print(f"Customer Name: {self.my_invoice.get_customer()}")

        print("=" * 68)
        print(f"{'ITEM':<15} {'QTY':<10} {'PRICE':<15} {'TOTAL(NGN)':<15}")
        print("-" * 68)

        self.sub_total = 0
        for i in range(len(self.my_invoice.product)):
            item_total = self.my_invoice.get_unit(i) * self.my_invoice.get_price(i)
            self.sub_total += item_total
            
            print(f"{self.my_invoice.get_product(i):<15} {self.my_invoice.get_unit(i):<10.2f} {self.my_invoice.get_price(i):<15.2f} {item_total:<15.2f}")

        self.actual_discount = (self.discount * self.sub_total) / 100
        self.vat = (17.5 * self.sub_total) / 100
        self.total = self.sub_total - self.actual_discount + self.vat

        print("-" * 68)
        print(f"{'Sub Total:':<15} {'':<10} {'':<15} {self.sub_total:<15.2f}")
        print(f"{'Discount:':<15} {'':<10} {'':<15} {self.actual_discount:<15.2f}")
        print(f"{'VAT @ 17.5%:':<15} {'':<10} {'':<15} {self.vat:<15.2f}")
        print("=" * 68)
        print(f"{'Bill Total:':<15} {'':<10} {'':<15} {self.total:<15.2f}")
        print("=" * 68)
        print(f"THIS IS NOT A RECEIPT. KINDLY PAY {self.total:.2f}")
        print("=" * 68)

    def display_invoice_receipt(self):
        self.amount_paid = float(input("How much did the customer give to you? "))

        current_time = datetime.now().strftime("%d-%b-%y %I:%M:%S %p")

        print("""
SEMICOLON STORES
MAIN BRANCH
LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.
TEL: 03293828343
DATE: {}
""".format(current_time))

        print(f"Cashier:  {self.my_invoice.get_cashier()}")
        print(f"Customer Name: {self.my_invoice.get_customer()}")

        print("=" * 68)
        print(f"{'ITEM':<15} {'QTY':<10} {'PRICE':<15} {'TOTAL(NGN)':<15}")
        print("-" * 68)

        for i in range(len(self.my_invoice.product)):
            item_total = self.my_invoice.get_unit(i) * self.my_invoice.get_price(i)
            print(f"{self.my_invoice.get_product(i):<15} {self.my_invoice.get_unit(i):<10.2f} {self.my_invoice.get_price(i):<15.2f} {item_total:<15.2f}")

        self.balance = self.amount_paid - self.total

        print("-" * 68)
        print(f"{'Sub Total:':<15} {'':<10} {'':<15} {self.sub_total:<15.2f}")
        print(f"{'Discount:':<15} {'':<10} {'':<15} {self.actual_discount:<15.2f}")
        print(f"{'VAT @ 17.5%:':<15} {'':<10} {'':<15} {self.vat:<15.2f}")
        print("=" * 68)
        print(f"{'Bill Total:':<15} {'':<10} {'':<15} {self.total:<15.2f}")
        print(f"{'Amount Paid:':<15} {'':<10} {'':<15} {self.amount_paid:<15.2f}")
        print(f"{'Balance:':<15} {'':<10} {'':<15} {self.balance:<15.2f}")
        print("=" * 68)
        print("             THANK YOU FOR YOUR PATRONAGE             ")
        print("=" * 68)

def main():
    invoice_receipt = InvoiceReceipt()
    invoice_receipt.invoice_input()
    invoice_receipt.display_invoice()
    invoice_receipt.display_invoice_receipt()

if __name__ == "__main__":
    main()