import java.util.Scanner;

public class InvoiceReciept  {
	private static SaleInput myInvoice = new SaleInput();
	static Scanner scanner = new Scanner(System.in);
	static String addToInvoiceAction = " ";

	static int discount = 0;
	static double subTotal = 0;
	static double actualDiscount;
	static double vat;
	static double total;
	static double amountPaid;
	static double balance;

	public static void main(String[] args){
	invoiceInput();
	displayInvoice();
	displayInvoiceReciept();

	}

		public static void salesDeskInsert(){

		for(; !addToInvoiceAction.equalsIgnoreCase("no"); addToInvoiceAction = scanner.nextLine()) {
 
		System.out.println("What did the user buy?");
		String productName = scanner.nextLine();
		myInvoice.setProduct(productName);


		System.out.println("How many pieces?");
		int unitQuantity = scanner.nextInt();
		myInvoice.setUnit(unitQuantity);

	
		System.out.println("How much per unit?");
		int pricePerUnit = scanner.nextInt();
		myInvoice.setPrice(pricePerUnit);
		
	
		System.out.println("Add more Items?");
		addToInvoiceAction = scanner.nextLine();
			}
		}
		
		public static void invoiceInput() {

		System.out.println("What is the customer's Name");
		String customerName = scanner.nextLine();
		myInvoice.setCustomer(customerName);
	
		salesDeskInsert();

		System.out.println("What is your name");
		String cashierName = scanner.nextLine();	
		myInvoice.setCashier(cashierName);

		System.out.println("How much discount will he get");
		discount = scanner.nextInt();

			}


	

		public static void displayInvoice() {
		System.out.print("""
		SEMICOLON STORES
		MAIN BRANCH
		LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.
		TEL: 03293828343
		DATE: 18-Dec-22 8:48:11 pm
		""");
	 	System.out.printf("Cashier:  %s%n", myInvoice.getCashier());
		System.out.printf("Customer Name: %s%n", myInvoice.getCustomer());

		System.out.print("""
	====================================================================
		""");
								
	System.out.printf("%-15s %-10s %-15s %-15s%n", "ITEM", "QTY", "PRICE", "TOTAL(NGN)");
	System.out.println("--------------------------------------------------------------------");

	for (int i = 0; i < myInvoice.product.size(); i++) {
	
		subTotal += (myInvoice.getPrice(i) *  myInvoice.getUnit(i));
    		System.out.printf("%-15s %-10.2f %-15.2f %-15.2f%n",
                      myInvoice.getProduct(i),
                      myInvoice.getUnit(i),
                      myInvoice.getPrice(i),
                      myInvoice.getUnit(i) * myInvoice.getPrice(i));

		 actualDiscount = (discount * subTotal) / 100;
    		 vat = (17.5 * subTotal) / 100;
    		total = subTotal - actualDiscount + vat;
			}

	System.out.println("--------------------------------------------------------------------");
	System.out.printf("%-15s %-10s %-15s %-15.2f%n", "Sub Total:", "", "", subTotal);
	System.out.printf("%-15s %-10s %-15s %-15.2f%n", "Discount:", "", "", actualDiscount);
	System.out.printf("%-15s %-10s %-15s %-15.2f%n", "VAT @ 17.5%:", "", "", vat);
	System.out.println("====================================================================");
	System.out.printf("%-15s %-10s %-15s %-15.2f%n", "Bill Total:", "", "", total);    	System.out.println("====================================================================");
    	System.out.printf("THIS IS NOT AN RECEIPT. KINDLY PAY %.2f%n", total);
	System.out.println("==================================================================== ");
				}
	

	
	public static void displayInvoiceReciept() {

		System.out.print("How much did the customer give to you?");
		amountPaid = scanner.nextInt();

		System.out.print("""
		SEMICOLON STORES
		MAIN BRANCH
		LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.
		TEL: 03293828343
		DATE: 18-Dec-22 8:48:11 pm
		""");
	 	System.out.printf("Cashier:  %s%n", myInvoice.getCashier());
		System.out.printf("Customer Name: %s%n", myInvoice.getCustomer());

		System.out.print("""
	====================================================================
		""");
								
	System.out.printf("%-15s %-10s %-15s %-15s%n", "ITEM", "QTY", "PRICE", "TOTAL(NGN)");
	System.out.println("--------------------------------------------------------------------");

	for (int i = 0; i < myInvoice.product.size(); i++) {
	
    		System.out.printf("%-15s %-10.2f %-15.2f %-15.2f%n",
                      myInvoice.getProduct(i),
                      myInvoice.getUnit(i),
                      myInvoice.getPrice(i),
                      myInvoice.getUnit(i) * myInvoice.getPrice(i));
			balance = amountPaid - total;
			}

	System.out.println("--------------------------------------------------------------------");
	System.out.printf("%-15s %-10s %-15s %-15.2f%n", "Sub Total:", "", "", subTotal);
	System.out.printf("%-15s %-10s %-15s %-15.2f%n", "Discount:", "", "", actualDiscount);
	System.out.printf("%-15s %-10s %-15s %-15.2f%n", "VAT @ 17.5%:", "", "", vat);
	System.out.println("====================================================================");
	System.out.printf("%-15s %-10s %-15s %-15.2f%n", "Bill Total:", "", "", total);
	System.out.printf("%-15s %-10s %-15s %-15.2f%n", "Amount Paid:", "", "", amountPaid); 
	System.out.printf("%-15s %-10s %-15s %-15.2f%n", "Balance:", "", "", balance); 
    	System.out.println("====================================================================");
    	System.out.println("             "+"THANK YOU FOR YOUR PATRONAGE"+"             ");
	System.out.println("==================================================================== ");
				}
			}
		
		
	




			 