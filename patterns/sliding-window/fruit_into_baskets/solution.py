from collections import defaultdict

def total_fruit(fruits):
  total, l, r  = 0, 0, 0
  basket = defaultdict(int)
  
  while r < len(fruits):
    fruit_type = fruits[r]

    while len(basket) == 2 and fruit_type not in basket:
      left_fruit_type = fruits[l]
      basket[left_fruit_type] -= 1
      l += 1
      if basket[left_fruit_type] == 0:
        del basket[left_fruit_type]

    basket[fruit_type] += 1
    total = max(total, r - l + 1)
    r += 1
  
  return total
