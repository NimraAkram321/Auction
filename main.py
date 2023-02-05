import os
#HINT: You can call clear() to clear the output in the console
from art import logo
print(logo);

list={}
def add_list(name,bid):
  
  list[name]=bid;

print("Welcome to the screate auction program");
run=True;
while run:
  name=input("what is your name?: ");
  bid=int(input("what's your bid?: $"))
  add_list(name,bid)
  condition=input("Are there anyother bidders? Type 'yes' or 'no'\n")
  if condition=="no":
    
    run=False;
  else:
    os.system('cls')
    
highest_bid=0
winner=""
for key in list:
    bid_amount=list[key]
    if bid_amount>highest_bid:
      highest_bid=bid_amount;
      winner=key
      
print(f"\n==================================================\nThe winner is {winner} with the highest bid of {highest_bid}.\n==================================================\n\n")      