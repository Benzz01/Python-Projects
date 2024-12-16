BASE_HOURS = 40
OT_MULTI = 1.5
hours = float(input("IDK: "))
pay_rate = float(input("Next num:" ))

if hours> BASE_HOURS:
    overtime_hours = hours - BASE_HOURS
    overtime_pay = overtime_hours * pay_rate * OT_MULTI
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
        gross_pay = hours * pay_rate
        print("the gross pay is $",(gross_pay))

if 'z' < 'a' :
        print("z is less than a")
else:
        print("z is not less than a")

s1= "New York"
s2 = "boston"
if s1 > s2:
  print(s2)
  print(s1)
else:
    print(s1)
    print(s2)
