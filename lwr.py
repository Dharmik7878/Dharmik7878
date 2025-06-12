my_list=["tridev\n","compute\n","and\n","tuition\n","classes\n","bhavnagar"]
fp=open("myfile1.txt","w")
fp.writelines(my_list)
fp.close()

fp=open("myfile1.txt","r")
print(fp.readlines())
fp.close()
