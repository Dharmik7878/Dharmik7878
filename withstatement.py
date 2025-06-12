with open("today.txt","w") as fp:
    fp.write("Hello How are You")
    fp.write("\nI am Fine")
    fp.write("\nTridev Computer classes")
    fp.write("\nBhavnagar")
    print("Thank you")
    print("current cursor postion:",fp.tell())
    fp.seek(3)
