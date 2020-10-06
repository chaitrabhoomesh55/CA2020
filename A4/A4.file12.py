12. Write a function to compute 5/0 and use try/except to catch the exceptions 

def error():
    return 5/0


try: 
    error()
except ZeroDivisionError:  
    print("division by zero")
except Exception.err:
    print("encountered an exception")
finally:
    print("try again & input non-zero values")
