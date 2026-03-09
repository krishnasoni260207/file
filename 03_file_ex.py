with open("file.txt") as f:
    content=f.read()
if("krishna" in content):
    print("The word 'krishna' is presrnt in file")
else:
    print("The word 'krishna' is not presrnt in file")
