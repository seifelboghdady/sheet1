x, p = map(float, input().split())
original = p / (1 - x * .01)
# Print the original price formatted to 2 decimal places (e.g., 100.00 instead of 100.0)
print(f'{original:.2f}')