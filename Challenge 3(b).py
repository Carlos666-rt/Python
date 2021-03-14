import textwrap

s = input('Enter a string: ')
w = int(input("Enter the width for the paragraph: ").strip())
print("Result:")
print(textwrap.fill(s, w))
