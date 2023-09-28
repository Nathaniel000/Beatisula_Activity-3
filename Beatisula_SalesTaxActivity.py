
purchaseamount = float(input("Enter the purchase amount: ₱"))

salestax_rate = 0.06
salestax = purchaseamount * salestax_rate

sales_tax = "Sales tax: ₱" + str(round(salestax, 2))

print(sales_tax)
