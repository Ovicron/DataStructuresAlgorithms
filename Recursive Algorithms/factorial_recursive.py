
def factorial(n):
  if n <= 2:
    return n
  else:
    n = n * factorial(n-1)
  return n

print(factorial(5))
