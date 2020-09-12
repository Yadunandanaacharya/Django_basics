def oh_my_god(func):
    
    def wrapper_function():
        #code before function
        print("*Oh!, my God*")
        func()
    return wrapper_function
def good(func1):
    def wrapper2_function():
        func1()
        print('Ok,then good and fine')
    return wrapper2_function


@oh_my_god
def quetsion():
    print('What did you do?')


@good
def answer():
    print('I have not done anything')




quetsion()
answer()