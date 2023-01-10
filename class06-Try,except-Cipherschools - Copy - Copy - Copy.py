while True:
          try:
                    age=int(input("Enter your age: "))
                    break
          except ValueError:
                    print("invalid input.....")
          except:
                    print("unexpected error....")
if age>18:
          print("You can play the game")
else:
          print("You cannot play this game")




# if we use try.......we should conformly use except
# with out except we cant use the try option.