import functions.run_python_file as functions

Results = functions.run_python_file("calculator", "main.py")
print(Results)

Results = functions.run_python_file("calculator", "main.py", ["3 + 5"])
print(Results)

Results = functions.run_python_file("calculator", "tests.py")
print(Results)

Results = functions.run_python_file("calculator", "../main.py")
print(Results)

Results = functions.run_python_file("calculator", "nonexistent.py")
print(Results)

Results = functions.run_python_file("calculator", "lorem.txt")
print(Results)
