
#______________________Class - Product Menus_____________________________
#1. Class to Create & Manage all the menus for available products
class Product_Options_Menu: #<--Parent Class For Product Options Menu
    pass
    def __init__(self, categories = []): #<-- Method1.0 - Constructor
        self.productCat = categories #<-- Creates empty list to hold categories

    def populate_primary_cat(self):#Method1.1 - fills the list with the websites primary categories
        self.productCat.append("Main Categories: ")
        main_cat = ["1. Men |", " 2. Women |", " 3. Kids |", " 4. On Sale |", " 5. New Releases "]
        self.productCat.extend(main_cat)
        return self.productCat

    def turn_into_one_column(self): #Method 1.2 - Turns a given list of options into a horizontal
        print(*self.productCat, sep='\n') # <-- Prints list as a SINGLE vertical column

    def turn_into_one_row(self): #Method 1.3 - Removes the commas and brackets, turning list into a neater list
        self.productCat = ' '.join(map(str, self.productCat)) #<-- turns list into SINGLE horizontal row
        return self.productCat

class New_Releases(Product_Options_Menu): #<-- Sub-Class for New releases
    pass
class Mens_Products (Product_Options_Menu): #<-- Sub-Class for Men's Products Menu
    pass
class Womens_Products(Product_Options_Menu): #<-- Sub-Class for Women's Products Menu
    pass
class Kids_Producs(Product_Options_Menu): #<-- Sub-Class for Kid's Products Menu
    pass
class On_Sale(Product_Options_Menu): #<-- Sub-Class for "Products On Sale" Menu
    pass

#____________________________Shoe Store Main__________________________________-

#2. While Statement to Manage Input & Navigation of these options
userState = False
while not(userState):

    primary = Product_Options_Menu()
    primary.populate_primary_cat()
    primary.turn_into_one_row()
    print("\n===============================================================\n")
    print(primary.productCat)
    print("\n===============================================================\n")


    userInput = input("\nPlease Choose an Option: ")

    if userInput == "1": #<-- Mens Category
        print("\nOption 1 Operational\n") #<-- test for user input 1
        #primary.turn_into_one_row()
        #primary.turn_into_one_column()
        #print(primary.productCat) #<-- test for un-modified product category
        #print(' '.join(map(str, primary.productCat)))
    elif userInput == "2": #<-- Womens Category
        print("\nOption 2 Operational\n")
    elif userInput == "3": #<-- Kid's Category
        print("\nOption 2 Operational\n")
    elif userInput == "4": #<-- On-Sale Category
        print("\nOption 2 Operational\n")
    elif userInput == "5": #<-- New Release Category
        print("\nOption 2 Operational\n")
    elif userInput == "6": #<-- Terminates the program
        userState = True

    