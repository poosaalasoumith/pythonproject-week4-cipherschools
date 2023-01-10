with open("file1.txt", "w") as f:
          # data =f.read()
          # print(data)
          f.write("Hello")
with open("file1.txt") as f:
          # data=f.read()
          # print(data)
          f.write("please do it")
# print(f.closed)

with open("file.txt","r+") as f:
          f.seek(len(f.read()))
          f.write("Please do it")
