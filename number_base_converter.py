# Welcome message
print("🎉 Welcome to the Number Converter! 🎉")
print("Here, you can transform numbers into different bases!")
print("Choose a number and an option to see the magic happen! ✨")
print("Ready to get started? Let's go! 🚀\n")

while True:
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

    # Ask if the user wants to continue
    continue_choice = input("Do you want to convert another number? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        print("Thank you for using the Number Converter! Goodbye! 🎉")
        break
      
