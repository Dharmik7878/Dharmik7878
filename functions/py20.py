def pen(os,p,s):
    ns=(os+p)-s
    return ns

old_stock=int(input("enter the old stock:"))
purches=int(input("Enter the purches pen:"))
sel=int(input("Enter the seled pen:"))
cur_stock=pen(old_stock,purches,sel)
print("curent stock is:",cur_stock)

