tRate = 0.06

def sales_tax(x):
	tax_rate = (x*tRate)
	return round(tax_rate, 2)

def total_after_tax(x, y):
	total_after_tax = (x + y)
	return round(total_after_tax, 2)

