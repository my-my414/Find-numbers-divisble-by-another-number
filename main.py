my_list=[12,65,54,39,12,339,221]
num=13
result=list(filter(lambda x:(x%num==0),my_list))
print("Numbers divisble by",num,"are",result)
