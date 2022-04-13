def loop_enter_txt():     
    while True:         
        input_user = input("Tell us about yourself: ")          
        print(f"My name is {input_user}")          
        with open ("my_info.txt","w") as file:             
            file.write(f"{input_user}")             
            file.close             
            pass                  
        with open ("my_info.txt", 'r') as file:             
            var = file.read()             
            print(var)             
            file.close()             
            pass          

            while True:

                input_user2 = input("Tell me some moere information: ")

                if input_user2.lower() == "quit":

                    print(input_user2)
                    file.close
                    break
                elif input_user2.isalpha():

                    with open ("my_info.txt","a") as file:             
                        file.write(f"{input_user2}")             
                        file.close()
                        break
        break 
    
loop_enter_txt()