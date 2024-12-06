import java.util.ArrayList;

public class SaleInput {
	private String customer;
	public  ArrayList<String> product = new ArrayList <>();
	public ArrayList<Double> unit = new ArrayList <>();
	public ArrayList<Double> price = new ArrayList <>();
	public String cashier = " ";

	public void setCustomer (String customer ) {
	this.customer = customer;
	}
	
	public String getCustomer () {
	return customer;
	}

	public void setProduct (String productName) {
	product.add(productName);
	}

	public String getProduct (int index) {
	return product.get(index);
	}

	public void setUnit (double unitQuantity) {
	unit.add(unitQuantity);
	}

	public double getUnit (int index) {
	return unit.get(index);
	}

	public void setPrice (double pricePerUnit) {
	price.add(pricePerUnit);
	}

	public double getPrice (int index ) {
	return price.get(index);
	}

	public void setCashier (String cashierName) {
	this.cashier = cashierName;
	}

	public String getCashier () {
	return cashier;
	}

		}

	
