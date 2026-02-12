import functions.get_file_content as functions

Results = functions.get_file_content("calculator", "lorem.txt")
print(Results)

Results = functions.get_file_content("calculator", "main.py")
print(Results)

Results = functions.get_file_content("calculator", "pkg/calculator.py")
print(Results)

Results = functions.get_file_content("calculator", "/bin/cat")
print(Results)

Results = functions.get_file_content("calculator","pkg/does_not_exist.py")
print(Results)



