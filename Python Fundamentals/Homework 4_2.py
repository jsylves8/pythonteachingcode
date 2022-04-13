

def loop_enter():
    while True:

        input_user = input("Please enter a number: ")

        if input_user.isdigit():

            print(f"Your number is {input_user}.")
            break

        elif input_user.isalpha():

            print(f"This is a letter, please enter a number!")

        else:
            print(f"Please enter a number!")

#loop_enter()

def for_fact():

    num = input("Please enter a number for factorial calculation: ")

    if num.isdigit():

        num = int(num)

        fact = 1

        for i in range(1, num + 1):

            fact = fact * i

        return fact

    elif num.isalpha():
        print("This is a letter, please enter a number. Run program again!")
    else:
        print("Please enter a number. Run the program again!")

#print(for_fact())


def while_fact():

    num = 1

    while True:

        num_fact = input("Please enter a number for factorial calculation: ")

        if num_fact.isdigit():

            while int(num_fact) >= 1:

                num = num * int(num_fact)

                num_fact = int(num_fact) - 1

            return(num)
        
        

        elif num_fact.isalpha():

            print(f"Please enter a number, not a letter!")
            
        else:

            print(f"Please enter a number!")
            
        

#print(f"The factorial total is {while_fact()}.")
    

###############################################################################################################################


def loop_enter_txt():     
    while True:         
        input_user = input("Tell us about yourself: ")          
        print(f"My name is {input_user}")          
        with open ("my_info.txt","w") as file:             
            file.write(f"{input_user}")             
            file.close()             
            pass                  
        with open ("my_info.txt", 'r') as file:             
            var = file.read()             
            print(var)             
            file.close()             
            pass          

            while True:

                input_user2 = input("Tell me some more information: ")

                if input_user2.lower() == "quit":
                    with open ("my_info.txt", 'r') as file:
                        file.read 
                        var2 = file.read
                        print(var2)
                        file.close()
                    break

                elif input_user2.isalpha():

                    with open ("my_info.txt","a") as file:             
                        file.write(f"{input_user2}")             
                        file.close()
                        
        break 
    

    extra_credit_ans = (f'This is the first letter of my name \"{input_user[0].upper()}\"')
    return extra_credit_ans

loop_enter_txt()

