############### Code helpers in python ###############
# This class is creating new Exception by hand


class CostomizedException(Exception):

    def __init__(self, arg, msg="The costom text Exception about") -> None:
        self.arg = arg
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self) -> str:
        return f"{self.msg} <{self.arg}> argument."

    # Using the returned Expetion with our costom text
    # def __str__(self) -> str:
    #    return super().__str__() + "My custom Exception text"


# This function rasing the Exception
def use_Exception(): 
    raise CostomizedException("Hello world!")

if __name__ == "__main__":
    use_Exception()
