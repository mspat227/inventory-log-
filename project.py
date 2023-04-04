'''
Vehicle spare parts inventory log
Final project for Havard's CS50P
Mayura Pathirana
Sri lanka
'''
#importing libraries
from tabulate import tabulate
from datetime import date, time, datetime
import csv
import sys
import os

def main():
    #creating the file
    file = "spare_parts_log.csv"
 
    #get the correct user input
    while True:
        try:
            #call the menu function
            menu()
            #get the user input and prompt the user for correct input, strip() to remove white spaces
            user_input: int = int(input("Select Operation: ").strip()) 
            if user_input == 1:
                register(file)
            elif user_input == 2:
                delete(file)
            elif user_input == 3:
                search(file)
            elif user_input == 4:
                view_log(file)
            elif user_input == 5:
                sys.exit(0)
            else:
                print("Sorry, Wrong Operation")
        except ValueError:
            print("Sorry, Wrong Operation")

#menu function
def menu():
    #creating table function with tabulate lib
    table = [["[1]", "Register Items"], ["[2]", "Delete Items"], ["[3]", "Search Items"], ["[4]", "Log"], ["[5]","Quit Programme"]]
    print(tabulate(table, headers=["🚗", "Vehicle Spare Parts Log"], tablefmt="rst"))

#creating save to CSV lib
def register(CSV_filename):
    #check if the file already exist, if not create file and add heading 
    if os.path.exists(CSV_filename) == False:
        with open(CSV_filename, 'a', newline='') as csvfile:
            fieldnames = ['Date', 'Time', 'Item Number', 'Item Name', 'Item Manufacturer', 'Specifications','Quantity', 'Item Cost', 'Selling Price' ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    #getting today date and time with datetime lib
    today_date = date.today()

    y = datetime.now()
    time = y.strftime("%H:%M:%S")
    
    #open list to append item_numbers in
    numbers = []

    #appending item nmbers into numbers list
    try:
        with open(CSV_filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                numbers.append(row['Item Number'])
    except KeyError:
        pass

    #get the input for item number and check if its already in the csv using numbers list/ check if the item number is infact a number
    while True:
        item_number = input("Item Number: ").strip()
        if item_number in numbers:
            print("Item is already Added")
        if item_number.isdigit() == False:
            print("Not Valid")
        else:
            item_number = item_number
            break
    #get the name, manufacturer and specs as user input   
    item_name = input("Item Name: ").strip().title()
    item_manufacture = input("Item Manufacturer: ").strip().title()
    item_specs = input("Specifications: ").strip().title()
    
    #get the quantity from the user
    while True:
        item_quantity = input("Item Quantity: ").strip()
        if item_quantity.isdigit() == False:
            print("Not Valid!")
        else:
            item_quantity = item_quantity
            break

    #getting the cost from user and check if input is only numbers
    while True:
        item_cost = input("Item Cost: ").strip()
        if item_cost.isdigit() == False:
            print("Not Valid!")
        else:
            item_cost = item_cost
            break
    
    #getting the selling price from the user and check if the input is valid number
    while True:
        selling_price = input("Selling Price: ").strip()
        if selling_price.isdigit() == False:
            print("Not Valid")
        else:
            selling_price = selling_price
            break

    #append and save all the variables into the CSV using dictwriter 
    with open(CSV_filename, 'a', newline='') as csvfile:
        fieldnames = ['Date', 'Time', 'Item Number', 'Item Name', 'Item Manufacturer', 'Specifications','Quantity', 'Item Cost', 'Selling Price' ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'Date': today_date, 'Time': time, 'Item Number': item_number, 'Item Name': item_name, 'Item Manufacturer': item_manufacture, 'Specifications': item_specs, 'Quantity': item_quantity, 'Item Cost': f"{item_cost} LKR", 'Selling Price': f"{selling_price} LKR" })
    
    print(f"Item {item_number} has been saved successfully!")
  
#creating delete record function
def delete(CSV_filename):
    #creating a list to append items in csv
    lines = []

    #creating a list to apppend item numbers in csv
    numbers = []

    #open and append the item numbers from csv file
    with open(CSV_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            numbers.append(row['Item Number'])

    #get the user input which number to delete and check if the number is in the csv  
    while True:
        item_number= input("Please enter the item number to be deleted: ")
        if item_number not in numbers:
            print("Item number invalid")
        else:
            item_number = item_number
            break

    #open and append the item rows to list and remove the row user need  delete
    with open(CSV_filename, 'r') as readFile:

        reader = csv.reader(readFile)

        for row in reader:

            lines.append(row)

            for field in row:

                if field == item_number:

                    lines.remove(row)

    #rewrite the rows in to the csv file after remove the row
    with open(CSV_filename, 'w', newline='') as writeFile:

        writer = csv.writer(writeFile)

        writer.writerows(lines)
    
    #print the operation is successful
    print(f"Entry {item_number} has been deleted successfully!")

#creating search items function
def search(CSV_filename):
    #creating a list to append items in csv
    lines = []

    #creating a list to apppend item numbers in csv
    numbers = []

    #open and append the item numbers from csv file
    with open(CSV_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            numbers.append(row['Item Number'])

    #get the user input which number to search and check if the number is in the csv  
    while True:
        item_number= input("Please enter the item number to be viewed: ")
        if item_number not in numbers:
            print("Item number invalid")
        else:
            item_number = item_number
            break
    #open and read the csv file and when item number match the print the item
    with open(CSV_filename, 'r') as readFile:

        reader = csv.reader(readFile)

        for row in reader:

            lines.append(row)

            for field in row:

                if field == item_number:
                    print(f'Date:               {row[0]}')
                    print(f'Time:               {row[1]}')
                    print(f'Item Number:        {row[2]}')
                    print(f'Item Name:          {row[3]}')
                    print(f'Item Manufacturer:  {row[4]}')
                    print(f'specifications:     {row[5]}')
                    print(f'Quantity:           {row[6]}')
                    print(f'Item Cost:          {row[7]}')
                    print(f'Selling Price:      {row[8]}')

#creating reports function
def view_log(CSV_filename):

    #creating the listr to append the csv  
    lines  = []

    with open(CSV_filename, 'r') as readFile:

        reader = csv.reader(readFile)

        for row in reader:

            lines.append(row)


    print(tabulate(lines, tablefmt="grid"))


if __name__=="__main__":
    main()
