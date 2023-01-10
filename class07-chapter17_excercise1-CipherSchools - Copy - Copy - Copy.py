def divide(a,b):
          try:
                    return a/b
          except ZeroDivisionError as err:
                    print(err)
                    # print("You cannot divide a number by zero")
          except TypeError as err:
                    print(err)

print(divide(4,0))