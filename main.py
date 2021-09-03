# w = writing, a = appending, r = reading, r+ = reading and writing
file = open("./data.csv", "a")
file.write("id,name,email\n")
file.write("1,Jamila,jamila@gmail.com\n")
file.write("2,Adam,adam@gmail.com\n")
file.write("3,Steve,steve@gmail.com\n")
file.close()