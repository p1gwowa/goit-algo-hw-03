import random

min = int(input("Please enter minimal possible number in lottery: "))       # Asking user to input parametrs for lottery
max = int(input("Please enter maximal possible number in lottery: "))
quantity = int(input("Please enter quantity of winning numbers: "))


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:          # Function definition
    if min >= 1 and max <= 1000 and min < quantity < max:                   # Condtion for generation of lottery ticket
        lottery_list  = list(range(int(min), int(max+1)))                   # List creation for inputed bounds
        lottery_ticket = random.sample(lottery_list, int(quantity))         # Generation of list with unique random numbers 
        lottery_ticket.sort()                                               # Sorting of generated list
        return lottery_ticket                                               # Returning of the result if criteria was met
    else:                                                                   # Condition if criteria wasn't met
        lottery_ticket = []                                                 # Creation of empty list
        return lottery_ticket                                               # Returning of the result if criteria wasn't met

result = get_numbers_ticket(min, max, quantity)                             # Getting of the result

print(result)
print(type(result))
