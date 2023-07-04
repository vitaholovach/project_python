def max_min(data):
  a = data[0]
  b = data[0]
  for num in data:
    if num > a:
      a = num
    elif num < b:
        b = num
  return a, b

print(max_min([1, 120, 1032, 14, 0, 4, 77, 100]))
