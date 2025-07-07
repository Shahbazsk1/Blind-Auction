from unicodedata import bidirectional

import art
print(art.logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def find_highest_bidder(bidder_dictionary):
    winner = ""
    highest_bid = 0

    max(bidder_dictionary)

    for bidder in bidder_dictionary:
        bid_amount = bidder_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner Is {winner} With A bid of ₹{highest_bid}.")

bids = {}
should_continue = True

while should_continue:
    name = input("What is your name: ")
    price = int(input("What's your Bid:  ₹ "))
    bids[name] = price
    should_continue = input("Are Their Any Bidders? Type 'Yes' or 'No'.\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" *5)
