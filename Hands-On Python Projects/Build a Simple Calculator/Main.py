while True:
    try :
        x = int(input("Enter a 1st Number:-"))
        y = int(input("Enter a 2nd Number:-"))
        print('''Enter a type of operation you want to do:-
Addition = '+' 
Subtraction = '-'
Multiplication = '*'
Division = '/'
Floor Division = '//'
Modulus (gives remainder) = '%'
Exponent = '**' ''')
        o = input("Enter a Operation:-")

        match o :
            case "+" :
                print("======================================")
                print(f"Addition of {x} & {y} is :-{x+y}")
                print("======================================")
            case "-" :
                print(f"Subtration of {x} & {y} is :-{x-y}")
                print("======================================")
            case "/" :
                print("======================================")
                print(f"division of {x} & {y} is :-{x/y}")
                print("======================================")
            case "*" :
                print("======================================")
                print(f"Multiplication of {x} & {y} is :-{x*y}")
                print("======================================")
            case "//" :
                print("======================================")
                print(f"Floor Division of {x} & {y} is :-{x//y}")
                print("======================================")
            case "%" :
                print("==================================================")
                print(f"Modulus (gives remainder) of {x} & {y} is :-{x%y}")
                print("===================================================")
            case "**" :
                print("======================================")
                print(f"Exponent of {x} & {y} is :-{x**y}")
                print("======================================")   
                                  
        print("Do you want to calculate again? (yes/no):")
        again = str(input())
        if again.lower() == "no":
            break
        else:
            pass
    except Exception as e :
        print("Enter a invalid identity ",e)
