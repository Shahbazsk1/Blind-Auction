# Blind-Auction
A simple terminal-based blind auction game built using Python. 
This program simulates an auction where users can place secret bids. 
At the end of the auction, the highest bidder is announced.

steps:
<br>1.Accept Multiple User Bids
<br>Prompts each user to enter their name and bid amount one at a time.
<br>2.Maintain Bid Privacy
<br>Simulates screen clearing using multiple \n characters to keep bids hidden from other users.
<br>3.Store Bids Securely
<br>Uses a Python dictionary ({name: bid}) to keep track of all submitted bids.
<br>4.Determine the Winner
<br>After all bids are entered, the program identifies the highest bidder and displays their name and bid.

Technologies & Python Libraries Used:
<br>-print(), input() – for user interaction
<br>-if/else, while loops – for flow control
<br>-dictionary – for storing user bids

Custom ASCII Art:
<br>-from art import logo – displays a styled logo at the beginning
<br>-Optional: You can create your own art.py or use an ASCII generator
