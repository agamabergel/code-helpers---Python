############### Code helpers in python ###############
# This function uses all types of catching an Exception

def catch_Exception() -> None:

    try:
        int(input("Enter an Integer: "))
    
    except Exception:
        print("Text inputed insted of an Integer")

    else:
        print("Well that's an Integer")

    finally:
        print("You definitely inputed something")
    

    
    
