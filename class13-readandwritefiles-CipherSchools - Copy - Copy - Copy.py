with open("file2.txt","r") as rf:
          with open("file.txt","w") as wf:
                    wf.write(rf.read())