#!/usr/bin/python

import sys


def making_change(amount, denominations):
	# denominations = [50, 25, 10, 5, 1]
	# set how to find combinations
	combos = [0] * (amount + 1)
	# set base
	if amount <= -1:
		return 0
	combos[0] = 1
	#double for loop to go through and match up denominations
	for coin in denominations:
		for j in range(coin, amount + 1):
			combos[j] += combos[j - coin]
	#return the total amount of combinations to make the provided amount
	return combos[amount]
  


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")