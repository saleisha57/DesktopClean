#Starting work on a simulation for running a marketing company (Sales)

Products = {'item1':15, 'item2':10}
Hour = 0
store_hr = True
store_op = input("Do you want to go to the store? (Yes or No): ")

while store_op == "yes" or store_op == "Yes":
	print("Store Name is now open. \nThe items for sale are: ")

	for prod in Products:
		print(prod)

	while store_hr == True:
		print("Store is open")
		Hour += 1
		if Hour == 8:
			store_hr = False
			print("Store is closed")
	store_op = input("Do you want to come back tomorrow? (Yes or No): ")
	Hour = 0
	store_hr = True