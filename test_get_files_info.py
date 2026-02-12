import functions.get_files_info as functions

Results = functions.get_files_info("calculator", ".")
print(Results)

Results = functions.get_files_info("calculator", "pkg")
print(Results)

Results = functions.get_files_info("calculator", "/bin")
print(Results)

Results = functions.get_files_info("calculator", "../")
print(Results)