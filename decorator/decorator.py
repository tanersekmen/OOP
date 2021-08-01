def decorator_with_argument(function):
    def wrapper_accepting_argument(arg1, arg2):
        print("My arguments are : {0}, {1}".format(arg1, arg2))
        function(arg1, arg2)

    return wrapper_accepting_argument

@decorator_with_argument
def cities(city1, city2):
    print('Cities I love are {0} and {1}.'.format(city1, city2))

cities('Rome', 'Izmir')


# OUTPUT

##My arguments are : Rome, Izmir
##Cities I love are Rome and Izmir.