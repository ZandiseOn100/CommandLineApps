def cleans_mobile(value): 
    
     
    """
    Removes all non-numeric characters from mobile number, adds an initial zero if it is missing and returns a cleaned number.
    """

    msg = "Re run an enter a value this time!" 
    value = input("Enter your mobile number: ") 
    if value !="":
        for character in value:
            if len(value) < 9:
                    print("invalid number length") 
                    quit()  
            else:
                if character.isdigit():
                    if value[0] != "0":
                        value = "0" + value                           
                        numeric_filter = filter(str.isdigit, value)
                        clean_number = "".join(numeric_filter)                           
                        return clean_number       
        return msg
print(cleans_mobile(value=0))