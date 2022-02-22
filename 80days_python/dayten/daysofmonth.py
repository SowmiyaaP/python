def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(y,m):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  y = is_leap(year)
  if month>12 or month<1:
      return "Invalid entry"
  if y == True and m == 2:
      return 29
  if y == False and m==2:
      return 28
  return month_days[month - 1]            


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
