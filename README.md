# Blind-Auction
A simple terminal-based blind auction game built using Python. 
This program simulates an auction where users can place secret bids. 
At the end of the auction, the highest bidder is announced.

steps:
1.Accept Multiple User Bids
Prompts each user to enter their name and bid amount one at a time.

2.Maintain Bid Privacy
Simulates screen clearing using multiple \n characters to keep bids hidden from other users.

3.Store Bids Securely
Uses a Python dictionary ({name: bid}) to keep track of all submitted bids.

4.Determine the Winner
After all bids are entered, the program identifies the highest bidder and displays their name and bid.

Technologies & Python Libraries Used:
-print(), input() – for user interaction
-if/else, while loops – for flow control
-dictionary – for storing user bids

Custom ASCII Art:
-from art import logo – displays a styled logo at the beginning
-Optional: You can create your own art.py or use an ASCII generator
