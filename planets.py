def weight_on_planets():
	weight = float(input("What do you weigh on earth? "))
	w_mars = weight * .38
	w_jupiter = weight * 2.34
	print("\n" + "On Mars you would weigh" , w_mars, "pounds." + "\n" + "On Jupiter you would weigh" , w_jupiter, "pounds.")

if __name__ == '__main__':
   weight_on_planets()