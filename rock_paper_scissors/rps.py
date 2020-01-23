#!/usr/bin/python

import sys

def rock_paper_scissors(n, cache = None):
  options = [['rock'], ['paper'], ['scissors']]
  combos = []
  
  if n == 0:
    return [[]]
  if n == 1:
    return options
  elif cache and cache[n] > 1:
    return cache[n]
  else:
    if not cache:
      cache = {i: 0 for i in range(n - 1)}
    cache[n] = rock_paper_scissors(n-1, cache)
    return cache[n]

  
  # arr = rock_paper_scissors(n - 1)
  # for sub in arr:
  #   for throw in options:
  #     new_throw = sub + throw
  #     combos.append(new_throw)
  # return combos




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')