n = int(input("Enter any number: "))
print("""Choose one of the options for Base conversion: 
      [ 1 ] Convert to BINARY
      [ 2 ] Convert to OCTAL
      [ 3 ] Convert to HEXADECIMAL""")
option = int(input("Your choice: "))
if option == 1:
    print("The number {} converted to BINARY is {}".format(n, bin(n)[2:]))
elif option == 2:
    print("The number {} converted to OCTAL is {}".format(n, oct(n)[2:]))
elif option == 3:
    print("The number {} converted to HEXADECIMAL is {}".format(n, hex(n)[2:]))
else:
    print("Invalid option!")