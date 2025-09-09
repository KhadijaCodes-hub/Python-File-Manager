file = open("sample.txt",'r')
content = file.read()
file.close()
print(f"Content of the file is : {content}")