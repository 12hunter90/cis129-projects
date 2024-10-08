# Lab 5 The Bottle Return Program
# Joel Martin
# 09/05/2024
# Program tells you how many bottles you
# have collected in a week and how much you have earned for collection

# Declare variables below 
totalBottles = 0
counter = 1 
todayBottles = 0
totalPayout = 0 
keepGoing = "y" 

# Loop to run program again
while keepGoing == "y":
    # Code to set value of variables
    totalBottles = 0
    counter = 1 

    # Collect bottles returned for 7 days
    while counter <= 7:  
        todayBottles = int(input(f"Enter number of bottles returned for day #{counter}: "))
        totalBottles += todayBottles  
        counter += 1  

    # Code to calculate total payout
    PAYOUT_PER_BOTTLE = 0.10
    totalPayout = totalBottles * PAYOUT_PER_BOTTLE

    # Code to print the number of total bottles and total payout
    print(f"\nTotal bottles returned: {totalBottles}")
    print(f"Total payout: ${totalPayout:.2f}")

    # Ask user if they want to continue
    print("Do you want to enter another week’s worth of data?")
    print("(Enter y or n)")
    keepGoing = input() 
