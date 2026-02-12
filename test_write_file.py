import functions.write_file as functions

Results = functions.write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(Results)

Results = functions.write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(Results)

Results = functions.write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(Results)

