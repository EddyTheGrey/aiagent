import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        #Checks
        abs_path = os.path.abspath(working_directory)
        
        target_dir = os.path.normpath(os.path.join(abs_path, file_path))    
        
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        # Will be True or False
        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
        
        if valid_target_dir == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        #Actions
        command = ["python", target_dir]
        if args != None:
            
            command.extend(args)
        

        complete_process = subprocess.run(command,capture_output=True,text=True,timeout=30)

        if complete_process.returncode != 0:
            return f"Process exited with code {complete_process.returncode}"
        elif not complete_process.stdout and not complete_process.stderr:
            return "No output produced"
        else:
            output_str = f"STDOUT: {complete_process.stdout} \n STDERR: {complete_process.stderr}"

        return output_str
    
    except Exception as e:
        return f"Error: executing Python file: {e}"