dict_book={}

while True:
  print("WELCOME TO YOUR PHONEBOOK")
  print("\nChoices")
  print("1- ADD NEW CONTACT\n2- SEARCH CONTACT\n3- DELETE CONTACT\n4- MODIFY CONTACT DETAILS\n5- View All Contacts\n0- Exit")
  choice = int(input("Enter your Choice = "))
  if choice==1 :
    print("Add Contact")
    name = input("Enter Name : ")
    number = input("Enter number : ")
    dict_book[name] = number
    print(f"Contact {name} Added Successfully")
  elif choice==2:
    print("Search Contact")
    name = input("Enter Name to Search : ")
    if name in dict_book:
     print(f"Your Contact {name} is Available is {dict_book[name]}") 
    else:
      print("Contact doesnot present")
  elif choice==3:
    print("Delete Contact")
    name = input("Enter Name to Delete : ")
    if name in dict_book:
     del dict_book[name]
    else:
      print("name is not available")
  elif choice==4:
    print("Modify your Contact Details")
    name=input("Enter Name to Modify")
    if name in dict_book:
       print("Updating Contact {name}")
       up=input("Enter 'N' t update name and 'P' for Ph#")
       if up== 'N':
        up_name=input("Enter New Name for this contact")
        dict_book[name]=up_name
        print("Updted Succesfully")
       elif up=='P':
        up_num =input("Enter New Number to Update")
        dict_book[number]=up_num
        print("Updted Succesfully")
    else:
      print("Contact is not available")
  elif choice==5:
    print("All Contacts Contact")
    if dict_book:
     for name,number in dict_book.items():
      print(f"Contact Name :{name}\t\t Ph# :{number}")
    else:
      print("No contact Found")
  elif choice==0:
    print("GOOD BYE")
    break
  else:
    print("Invalid Input Try again")