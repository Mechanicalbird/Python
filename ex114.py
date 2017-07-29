while True:
     try:
         number = int(input("what is your number!\n"))
         print(18/number)
         break
     except:
         print("Make sure you enter a number")
     finally:
         print("Thank you")
