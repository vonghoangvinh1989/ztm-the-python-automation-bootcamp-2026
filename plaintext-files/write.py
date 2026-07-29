# note: it will create a file if does not exist but overwrite if exists
with open("poem.txt", "w") as file:
    file.write("Roses are red,\n")
    file.write("Violets are blue,\n")
    file.write("Sugar is sweet,\n")
    file.write("And so are you!,\n")
