#def main():
   # print("I have a message for you")
  #  message()
 #   print("goodBye")

#def message():
  #  print("I am Noah")
 #   print("king of the Britons")

#main()


def main():
    show_intrest(rate =0.01,periods=10, principal= 10000.0)
    show_intrest(10000.0, rate = 0.01, periods = 10)
    show_interest(1000.0, rate=0.01, 10)

def show_intrest(principal, rate, periods):
    intrest = principal * rate * periods
    print("the simple intrest will be$",
          format(intrest,",.2f"), sep='')

    main()
