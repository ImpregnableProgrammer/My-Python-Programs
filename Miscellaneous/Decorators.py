#########################################################################################################################
######################### Full answer about Decorators with more info here: #############################################
#### http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python#answer-739665 ####
#########################################################################################################################

firsts = ['1st', '1', 'First', 'One', 'The first one', 'first one']
seconds = ['2nd', '2', 'Second', 'Two', 'The second one', 'second one']
thirds = ['3rd', '3', 'Third', 'Three', 'The third one', 'third one']
fourths = ['4th', '4', 'Fourth', 'Four', 'The fourth one', 'fourth one']
fifths = ['5th', '5', 'Fifth', 'Five', 'The fifth one', 'fourth one']
sixths = ['6th', '6', 'Sixth', 'Six', 'The fifth one', 'fourth one']
sevenths = ['7th', '7', 'Seventh', 'Seven', 'The seventh one', 'seventh one']
alls = ['All', 'Everything', 'All of them', 'Everything available', '1-7']
done = ['That is all', 'Done', 'No more', 'No thanks', 'Nevermind', 'Never', 'Forget it', 'None', 'No', 'Nope', 'No thank you', 'That is all', 'I am done']

#########################
#### First Decorator ####
#########################

def First():
    print("""#########################
#### First Decorator ####
#########################""")
    print("\t\t\t")

    # It’s not black magic, you just have to let the wrapper 
    # pass the argument:

    def a_decorator_passing_arguments(function_to_decorate):
        def a_wrapper_accepting_arguments(arg1, arg2):
            print("I got args! Look:", arg1, arg2)
            function_to_decorate(arg1, arg2)
        return a_wrapper_accepting_arguments

    # Since when you are calling the function returned by the decorator, you are
    # calling the wrapper, passing arguments to the wrapper will let it pass them to 
    # the decorated function

    @a_decorator_passing_arguments
    def print_full_name(first_name, last_name):
        print("My name is", first_name, last_name)

    # The above is the same as this: print_full_name = a_decorator_passing_arguments(print_full_name)

    print_full_name("Peter", "Venkman")
    # outputs:
    #I got args! Look: Peter Venkman
    #My name is Peter Venkman

##########################
#### Second Decorator ####
##########################

def Second():
    print("\t\t\t\t")
    print("""##########################
#### Second Decorator ####
##########################""")
    print("\t\t\t\t")
    def method_friendly_decorator(method_to_decorate):
        def wrapper(self, lie):
            lie = lie - 3 # very friendly, decrease age even more :-)
            return method_to_decorate(self, lie)
        return wrapper


    class Lucy(object):

        def __init__(self):
            self.age = 32

        @method_friendly_decorator
        def sayYourAge(self, lie):
            print("I am %s, what did you think?" % (self.age + lie))

    l = Lucy()
    l.sayYourAge(-3)
    #outputs: I am 26, what did you think?

#########################
#### Third Decorator ####
#########################

def Third():
    print("\t\t\t")
    print("""#########################
#### Third Decorator ####
#########################""")
    print("\t\t\t")
    def a_decorator_passing_arbitrary_arguments(function_to_decorate):
        # The wrapper accepts any arguments
        def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
            print("Do I have args?:")
            print(args)
            print(kwargs)
            # Then you unpack the arguments, here *args, **kwargs
            # If you are not familiar with unpacking, check:
            # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
            function_to_decorate(*args, **kwargs)
        return a_wrapper_accepting_arbitrary_arguments

    @a_decorator_passing_arbitrary_arguments
    def function_with_no_argument():
        print("Python is cool, no argument here.")

    function_with_no_argument()
    #outputs
    #Do I have args?:
    #()
    #{}
    #Python is cool, no argument here.

    @a_decorator_passing_arbitrary_arguments
    def function_with_arguments(a, b, c):
        print(a, b, c)

    function_with_arguments(1,2,3)
    #outputs
    #Do I have args?:
    #(1, 2, 3)
    #{}
    #1 2 3 

    @a_decorator_passing_arbitrary_arguments
    def function_with_named_arguments(a, b, c, platypus="Why not ?"):
        print("Do %s, %s and %s like platypus? %s" % (a, b, c, platypus))

    function_with_named_arguments("Bill", "Linus", "Steve", platypus="Indeed!")
    #outputs
    #Do I have args ? :
    #('Bill', 'Linus', 'Steve')
    #{'platypus': 'Indeed!'}
    #Do Bill, Linus and Steve like platypus? Indeed!

    class Mary(object):

        def __init__(self):
            self.age = 31

        @a_decorator_passing_arbitrary_arguments
        def sayYourAge(self, lie=-3): # You can now add a default value
            print("I am %s, what did you think ?" % (self.age + lie))

    m = Mary()
    m.sayYourAge()
    #outputs
    # Do I have args?:
    #(<__main__.Mary object at 0xb7d303ac>,)
    #{}
    #I am 28, what did you think?


##########################
#### Fourth Decorator ####
##########################

def Fourth():
    print("\t\t\t")
    print("""##########################
#### Fourth Decorator ####
##########################""")
    print("\t\t\t\t")
    # Decorators are ORDINARY functions
    def my_decorator(func):
        print("I am an ordinary function")
        def wrapper():
            print("I am function returned by the decorator")
            func()
        return wrapper

    # Therefore, you can call it without any "@"

    def lazy_function():
        print("zzzzzzzz")

    decorated_function = my_decorator(lazy_function)
    #outputs: I am an ordinary function

    # It outputs "I am an ordinary function", because that’s just what you do:
    # calling a function. Nothing magic.

    @my_decorator
    def lazy_function():
        print("zzzzzzzz")

    #outputs: I am an ordinary function


########################
#### Fifth Decorator####
########################

def Fifth():
    def counter2():
        if not hasattr(counter2, "counter"):
            counter2.counter = 0
        counter2.counter += 1


    print("\t\t\t\t\t\t\t")
    print("""########################
#### Fifth Decorator####
########################""")
    print("\t\t\t\t")


    def decorator_maker():
        counter2()
        if counter2.counter == 1:
            print("I make decorators! I am executed only once: "+\
                  "when you make me create a decorator.")
        elif counter2.counter >= 2:
            print("\tI make decorators! I am executed only once: "+\
                  "when you make me create a decorator.")

        def my_decorator(func):
            if counter2.counter == 1:
                print("I am a decorator! I am executed only when you decorate a function.")
            elif counter2.counter >= 2:
                print("\tI am a decorator! I am executed only when you decorate a function.")

            def wrapped():
                if counter2.counter == 1:
                    print("I am the wrapper around the decorated function. "
                          "I am called when you call the decorated function."
                          "As the wrapper, I return the RESULT of the decorated function.")
                if counter2.counter >= 2:
                    print("\tI am the wrapper around the decorated function. "
                          "\n\tI am called when you call the decorated function."
                          "\n\tAs the wrapper, I return the RESULT of the decorated function.")
                return func()
            if counter2.counter == 1:
                print("As the decorator, I return the wrapped function.")
            elif counter2.counter >= 2:
                print("\tAs the decorator, I return the wrapped function.")

            return wrapped
        if counter2.counter == 1:
            print("As a decorator maker, I return a decorator")
        elif counter2.counter >= 2:
            print("\tAs a decorator maker, I return a decorator")
        return my_decorator

    # Let’s create a decorator. It’s just a new function after all.
    new_decorator = decorator_maker()       
    #outputs:
    #I make decorators! I am executed only once: when you make me create a decorator.
    #As a decorator maker, I return a decorator

    # Then we decorate the function

    def decorated_function():
        print("I am the decorated function.")

    decorated_function = new_decorator(decorated_function)
    #outputs:
    #I am a decorator! I am executed only when you decorate a function.
    #As the decorator, I return the wrapped function

    # Let’s call the function:
    decorated_function()
    #outputs:
    #I am the wrapper around the decorated function. I am called when you call the decorated function.
    #As the wrapper, I return the RESULT of the decorated function.
    #I am the decorated function.


        ###################
        #### Shortened ####
        ###################

    print("\t\t\t\t\t\t\t\t\t")
    print("""\t###################
        #### Shortened ####
        ################### """)
    print("\t\t\t\t")
    def decorated_function():
        print("\tI am the decorated function.")
    # The following...
    decorator_maker()(decorated_function)()
    # The above...
    print("\t\t\t\t\t\t") # (Just creates a separation between the two results)
    # Is the same as this!
    decorated_function = decorator_maker()(decorated_function)
    decorated_function()
    # both output:
    #I make decorators! I am executed only once: when you make me create a decorator.
    #As a decorator maker, I return a decorator
    #I am the wrapper around the decorated function. I am called when you call the decorated function.
    #As the wrapper, I return the RESULT of the decorated function.
    #I am the decorated function.

    # Therefore, you can also do just `decorator_maker()(decorated_function)()`, skip the variable, and it will still print EVERYTHING.


        ########################
        ### Even MORE Short ####
        ########################

    print("\t\t\t\t\t\t")
    print("""\t########################
        ### Even MORE Short ####
        ######################## """)
    print("\t\t\t\t\t\t\t")
    # Function call using the "@" syntax!
    @decorator_maker()
    def decorated_function():
        print("\tI am the decorated function.")
    #outputs:
    #I make decorators! I am executed only once: when you make me create a decorator.
    #As a decorator maker, I return a decorator
    #I am a decorator! I am executed only when you decorate a function.
    #As the decorator, I return the wrapped function.

    #Eventually: 
    decorated_function()    
    #outputs:
    #I am the wrapper around the decorated function. I am called when you call the decorated function.
    #As the wrapper, I return the RESULT of the decorated function.
    #I am the decorated function.

    #Hey, did you see that? We used a function call with the "@" syntax! :-)



#########################
#### Sixth Decorator ####
#########################

def Sixth():
    def counter3():
        if not hasattr(counter3, "counter"):
            counter3.counter = 0
        counter3.counter += 1


    print("\t\t\t\t\t")
    print("""#########################
#### Sixth Decorator ####
#########################""")
    print("\t\t\t\t\t")
    def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
        counter3()
        if counter3.counter == 1:
            print("I make decorators! And I accept arguments:", decorator_arg1, decorator_arg2)
        else:
            print("\tI make decorators! And I accept arguments:", decorator_arg1, decorator_arg2)

        def my_decorator(func):
            # The ability to pass arguments here is a gift from closures.
            # If you are not comfortable with closures, you can assume it’s ok,
            # or read: http://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python
            if counter3.counter == 1:
                print("I am the decorator. Somehow you passed me arguments:", decorator_arg1, decorator_arg2)
            else:
                print("\tI am the decorator. Somehow you passed me arguments:", decorator_arg1, decorator_arg2)
                
            # Don't confuse decorator arguments and function arguments!
            def wrapped(function_arg1, function_arg2) :
                if counter3.counter == 1:
                    print ("I am the wrapper around the decorated function.\n"
                          "I can access all the variables\n"
                          "\t- from the decorator: {0} {1}\n"
                          "\t- from the function call: {2} {3}\n"
                          "Then I can pass them to the decorated function")
                else:
                    print ("\tI am the wrapper around the decorated function.\n"
                          "\tI can access all the variables\n"
                          "\t\t- from the decorator: {0} {1}\n"
                          "\t\t- from the function call: {2} {3}\n"
                          "\tThen I can pass them to the decorated function"
                           
                      .format(decorator_arg1, decorator_arg2,
                              function_arg1, function_arg2))
                return func(function_arg1, function_arg2)

            return wrapped

        return my_decorator

    @decorator_maker_with_arguments("Leonard", "Sheldon")
    def decorated_function_with_arguments(function_arg1, function_arg2):
        print ("I am the decorated function and only knows about my arguments: {0}"
               " {1}".format(function_arg1, function_arg2))

    decorated_function_with_arguments("Rajesh", "Howard")
    #outputs:
    #I make decorators! And I accept arguments: Leonard Sheldon
    #I am the decorator. Somehow you passed me arguments: Leonard Sheldon
    #I am the wrapper around the decorated function. 
    #I can access all the variables 
    #   - from the decorator: Leonard Sheldon 
    #   - from the function call: Rajesh Howard 
    #Then I can pass them to the decorated function
    #I am the decorated function and only knows about my arguments: Rajesh Howard


            ####################################################
            #### Shortened Version with Different arguments ####
            ####################################################

    print("\n")
    print("""\t####################################################
        #### Shortened Version with Different arguments ####
        ####################################################""")
    print("\n")
    c1 = "Penny"
    c2 = "Leslie"

    @decorator_maker_with_arguments("Leonard", c1)
    def decorated_function_with_arguments(function_arg1, function_arg2):
        print ("\tI am the decorated function and only knows about my arguments:"
               "\t{0} {1}".format(function_arg1, function_arg2))

    decorated_function_with_arguments(c2, "Howard")
    #outputs:
    #I make decorators! And I accept arguments: Leonard Penny
    #I am the decorator. Somehow you passed me arguments: Leonard Penny
    #I am the wrapper around the decorated function. 
    #I can access all the variables 
    #   - from the decorator: Leonard Penny 
    #   - from the function call: Leslie Howard 
    #Then I can pass them to the decorated function
    #I am the decorated function and only knows about my arguments: Leslie Howard


###########################
#### Seventh Decorator ####
###########################

def Seventh():
    def counter4():
        if not hasattr(counter4, "counter"):
            counter4.counter = 0
        counter4.counter += 1

    def counter5():
        if not hasattr(counter5, "counter"):
            counter5.counter = 0
        counter5.counter += 1

    def counter6():
        if not hasattr(counter6, "counter"):
            counter6.counter = 0
        counter6.counter += 1

    print("\n")
    print("""###########################
#### Seventh Decorator ####
###########################""")
    print("\n")
    def benchmark(func):
        counter4()
        """
        A decorator that prints the time a function takes
        to execute.
        """
        import time
        def wrapper(*args, **kwargs):
            t = time.clock()
            res = func(*args, **kwargs)
            if counter4.counter == 1:
                print(func.__name__, time.clock()-t)
            else:
                print("\t" + func.__name__, time.clock()-t)
            return res
        return wrapper


    def logging(func):
        counter5()
        """
        A decorator that logs the activity of the script.
        (it actually just prints it, but it could be logging!)
        """
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if len(kwargs) > 0:
                if counter5.counter == 1:
                    print(func.__name__, args, kwargs)
                else:
                    print("\t" + func.__name__, args, kwargs)
            else:
                if counter5.counter == 1:
                    print(func.__name__, args)
                else:
                    print("\t" + func.__name__, args)
            return res
        return wrapper


    def counter(func):
        counter6()
        """
        A decorator that counts and prints the number of times a function has been executed
        """
        def wrapper(*args, **kwargs):
            wrapper.count = wrapper.count + 1
            res = func(*args, **kwargs)
            if counter6.counter == 1:
                print("{0} has been used: {1}x".format(func.__name__, wrapper.count))
            else:
                print("\t{0} has been used: {1}x".format(func.__name__, wrapper.count))
            return res
        wrapper.count = 0
        return wrapper

    @counter
    @logging
    @benchmark
    def reverse_string(string):
        return string[::-1]

    print(reverse_string("Able was I ere I saw Elba"))
    print(reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!"))

    #outputs:
    #reverse_string ('Able was I ere I saw Elba',) {}
    #wrapper 0.0
    #wrapper has been used: 1x 
    #ablE was I ere I saw elbA
    #reverse_string ('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!',) {}
    #wrapper 0.0
    #wrapper has been used: 2x
    #!amanaP :lanac a ,noep a ,stah eros ,raj a ,hsac ,oloR a ,tur a ,mapS ,snip ,eperc a ,)lemac a ro( niaga gab ananab a ,gat a ,nat a ,gab ananab a ,gag a ,inoracam ,elacrep ,epins ,spam ,arutaroloc a ,shajar ,soreh ,atsap ,eonac a ,nalp a ,nam A


            ######################################
            #### Other Use of Same Decorators ####
            ######################################


    print("\n")
    print("""\t######################################
        #### Other Use of Same Decorators ####
        ######################################""")
    print("\n")
    @counter
    @benchmark
    def get_random_futurama_quote():
        import urllib.request
        request = urllib.request.Request("http://subfusion.net/cgi-bin/quote.pl?quote=futurama")
        result = bytes.decode(urllib.request.urlopen(request).read())
        try:
            value = result.split("<br><b><hr><br>")[1].split("<br><br><hr><br>")[0]
            return value.strip()
        except:
            import traceback
            traceback.print_exc()
            return "No, I'm ... doesn't!"


    print("\t" + get_random_futurama_quote())

    #outputs:
    #get_random_futurama_quote () {}
    #wrapper 0.02
    #wrapper has been used: 1x
    #The laws of science be a harsh mistress.
    #get_random_futurama_quote () {}
    #wrapper 0.01
    #wrapper has been used: 2x
    #Curse you, merciful Poseidon!

def count():
    if not hasattr(count, 'counter'):
        count.counter = 0
    count.counter += 1
    
while True:
    count()
    print("\t\t\t")
    if count.counter == 1:
        lvt = input("Which one do you want?: ").capitalize()
    else:
        lvt = input("Anything else?: ").capitalize()
    if lvt in firsts:
        print('\t\t')
        First()
    elif lvt in seconds:
        print("\t\t")
        Second()
    elif lvt in thirds:
        print("\t\t")
        Third()
    elif lvt in fourths:
        print("\t\t")
        Fourth()
    elif lvt in fifths:
        print("\t\t")
        Fifth()
    elif lvt in sixths:
        print("\t\t")
        Sixth()
    elif lvt in sevenths:
        print("\t\t")
        Seventh()
    elif lvt in alls:
        print("\t\t")
        First()
        Second()
        Third()
        Fourth()
        Fifth()
        Sixth()
        Seventh()
    elif lvt in done or not lvt:
        print("Okay then. Bye!")
        break
    else:
        print("Not a Decorator example! Please choose from numbers 1-7.")
        if count.counter == 1:
            count.counter = 0
        else:
            pass
