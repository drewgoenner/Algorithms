#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  options = ['rock', 'paper', 'scissors']
  all_combos = []

  def pair_options(pairs_left, total):
  	if pairs_left == 0:
  		all_combos.append(total)
  		return

  	for i in range(0, len(options)):
  		pair_options(pairs_left -1, total + [options[i]])

  	pair_options(n, [])
  	return all_combos


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')