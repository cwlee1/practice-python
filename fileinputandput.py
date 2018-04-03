
file = open("in.txt", "r")
file2 = open("out.txt", "w")


lines = file.readlines()

file2.writelines(lines)

file.close()