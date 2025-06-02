day=int(input("Enter the day:"))
year=(day//365)
month=(day%365)//30
day=day-((year*365)+(month*30))
print("year:",year)
print("month:",month)
print("day:",day)
