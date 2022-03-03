while True:
    print("------------------------------------")
    number1 = input("First number: ")
    number2 = input("Second number: ")

    while True:
        if number1.isdigit():
            break
        else:
            print("------------------------------------")
            number1 = input("First number (only numbers pls): ")
        

    while True:
        if number2.isdigit():
            break
        else:
            print("------------------------------------")
            number2 = input("Second number (only numbers pls): ")

    print("------------------------------------")
    calculation = input("What type of calculation do you wanna do? (+,-,/,*): ")

    calculations = ["-", "+", "*", "/"]

    print("------------------------------------")
    while True:
        if calculation not in calculations:
            calculation = input("type (-.+,*,/)")
        if calculation in calculations:
            break
    try:
        if calculation == "-":
            print(int(number1)-int(number2))
        if calculation == "+":
            print(int(number1)+int(number2))
        if calculation == "*":
            print(int(number1)*int(number2))
        if calculation == "/":
            print(int(number1)/int(number2))
    except:
        print("Something went wrong")
    
      
    response = input("Do you wanna calculate something else?: ")
    response.lower()
    if response != "yes":
        print("Okay bye bye")
        break