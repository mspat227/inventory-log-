# Inventory Log for vehicale spare parts
#### Video Demo:  
#### Description:

## Main Idea:

#### What is inventory log:
- Inventory logs are used to help track inventory when it is requested and fulfilled in your site's requests. It also tracks: who used the inventory. the         quantity fulfilled. the total inventory cost.

- A system that helps a shop owner to insert inventory log. Specially a vehicle spare parts shop owner

- the programme allows user to register items into system

- the programme allows the user to delete records

- the programme alows the user to see the log of the data he insert

- the programme allows the user to search the data he added

## Methodes and Mocules used:

- tabulate
- datetime
- csv
- sys
- os

## Functions:

## Main Function;

- first the programme stats to run after the CLI command you will starts to see the menu apperas. Main will call the menu function first

- then the programme will ask the user input as per the menu and user can choose which function to create

- comand will be cheked through Try and Except block for ValueErrors might done by the user

- if user give a wrong input the user will be prompt untill a correct inpput to be added

- to promt the user for above used While loop and inside Try and Except block


## Menu Function:

- menu function will invoke by the main function once main function invoked by the user through CLI command

- main functions main task is to creat the menu for the user to choose in CLI

- to create the table in CLI used module Tabulate (pip install tabulate)

- <print(tabulate(table, headers=["🚗", "Vehicle Spare Parts Log"], tablefmt="rst"))>

## Register Function:
- register function helps the user to insert new items into the programme. def rgister()

- first function will check there is any csv file opened, if not then the function will open a csv file and add the heading.

- then the function will append the items in the list using Dictreader to two lists. one to cheak the item number that user will be adding already exist. and then to just open a file.
- then function will get the excst time and date of the registering is done with help of datetime module
- function will ask the user tto input Item Number and it must be a intiger and it should not be used before, if so the programme will prompt the user untill a valid data is being added

- then the programme will ask the Item name / Item Sepecs and item manufacturerer respectively. All will be titled when saved to CSV

- programme will next ask the user to input Item Quantity/ Item price and Item Cost respectivly

- all input for above must be ints and if not programme will prompt the user

- to promt the user for above used While loop and inside Try and Except block

- once user add all details , saved the data to varibales will be write to CSV using DictWriter with help of CSV module

## Delete Function:

- creating a list to append items in csv

- creating a list to apppend item numbers in csv

- open and append the item numbers from csv file

- get the user input which number to delete and check if the number is in the csv

- open and append the item rows to list and remove the row user need to delete

- rewrite the rows in to the csv file after remove the row

- print the operation is successfull

## Search Function
- creating a list to append items in csv

- creating a list to apppend item numbers in csv

- open and append the item numbers from csv file

- get the user input which number to search and check if the number is in the csv

- used while and TRY Except to promt the user for output

- open and read the csv file and when item number match the print the item


## View Log Function
- once user choose log from main menu the programme will invoke View_log function

- used a list to read the csv file row by row

- print the list using tabulate function as a table
