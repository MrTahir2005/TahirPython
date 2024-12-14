2.Reading a file

# readline single line
file=open('/content/TAHIR PYTHON.txt','r')
content=file.readline()
print(content)
file.close()


# readlines reads multiple lines
file=open('/content/TAHIR PYTHON.txt','r')
content=file.readlines()
print(content)
file.close()
