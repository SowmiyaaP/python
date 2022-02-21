from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bids = {}
bidding_over = False
def highest_bid(bidding_record):
  highest = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record
    if bid_amount>highest:
      highest = bid_amount
      winner = bidder
  print("the winner is {winner} with the bid {highest}.")    



while not bidding_over:
  user = input("Enter your name:")
  bid=int(input("Enter your bid amount:"))
  bids[user] = bid
  option = input("Is there an another participant? yes/no:")
  if option == "no":
    bidding_over = True
  elif option == "yes" :
   clear()
   