# Prompt the user to input two numbers (num1 and num2)
num1 = float(input(&quot;Enter the first number (num1): &quot;))
num2 = float(input(&quot;Enter the first number (num2): &quot;))

# Calculate multiplication
multiplication = num1 * num2

# Ensure non-zero division
if num2 != 0:
division = num1 / num2
else:
division = &quot;Undefined (division by zero)&quot;

# Print results
print(&quot;Multiplication:&quot;, multiplication)
print(&quot;Division:&quot;, division)
