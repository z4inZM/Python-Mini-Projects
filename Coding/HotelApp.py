dict_menu = {
    "Pasta":300 ,
    "Burger":200 ,
    "Coffee":120 ,
    "Shake":100 ,
    "Pizza":500 
    }

print("WELCOME TO OUR PYTHON CAFE")
print("Pasta Rs:300\nBurger Rs:200\nCoffee Rs:120\nShake Rs:100\nPizza Rs:500" )

order_total = 0

item_1 = input("Please Enter your 1st item to Order = ")
if item_1 in dict_menu:
    order_total += dict_menu[item_1]
    print(f"your item  {item_1} has been added to your cart ")

else:
    print("Enter Correct Order")

another_item_confirmation = input("Do You want another Item? (Y/N)")
if another_item_confirmation == "Y":
  item_2 =input("Please Enter your 2nd item to Order = ")
  if item_2 in dict_menu:
    order_total += dict_menu[item_2]
    print(f"your item  {item_2} has been added to your cart")
    
    print(f"\n \t \t Total amount of your Order is {order_total}")
    print("\n \t \t THANKS FOR USING OUR SERVICES")
  else:
    print(f"your is not available")
elif another_item_confirmation == "N":
  print(f"\n \t \t Total amount of your Order is {order_total}")
  print("\n \t \t THANKS FOR USING OUR SERVICES")
  


