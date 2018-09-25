#
# Name: Jonathan Shan
# Student ID:014705700
# Date (last modified): 9/21/18
#
# Lab 0 
# Section 15
# Purpose of Lab: Convert weight on different planets
# 

#w_mars is a float which is converted weight on mars
#w_jupiter is a float which is coverted weight on jupiter

def weight_on_planets():
	weight = int(input("What do you weigh on earth? "))
	w_mars = weight * .38
	w_jupiter = weight * 2.34
	print("\n" + "On Mars you would weigh" , w_mars, "pounds." + "\n" + "On Jupiter you would weigh" , w_jupiter, "pounds.")

if __name__ == '__main__':
   weight_on_planets()