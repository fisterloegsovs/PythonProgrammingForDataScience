message = "Hello, world!"
print(len(message))
f = open("message.txt","w")
f.writelines(message)
f.close()
