#1. Class to Create & Manage all the menus for available products
class Product_Options_Menu: #<--Parent Class For Product Options Menu
    pass
class New_Releases(Product_Options_Menu): #<-- Sub-Calss for new releases
    pass
class Mens_Products (Product_Options_Menu): #<-- Sub-Class for Men's Products Menu
    pass
class Womens_Products(Product_Options_Menu): #<-- Sub-Class for Women's Products Menu
    pass
class Kids_Producs(Product_Options_Menu): #<-- Sub-Class for Kid's Products Menu
    pass
class On_Sale(Product_Options_Menu): #<-- Sub-Class for "Products On Sale" Menu
    pass
#2. While Statement to Mange Input & Navigation of these options
userState = False
while not(userState):
    userInput = input("\nPlease Choose an Option: ")
    if userInput == "1":
        print("\nOption 1 Operational\n") #<-- test for user input 1
    elif userInput == "2":
        print("\nOption 2 Operational\n")
    elif userInput == "5":
        userState = True

    