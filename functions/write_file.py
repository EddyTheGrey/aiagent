import os

def write_file(working_directory, file_path, content):
    try:
        
        #Creat Full path string
        abs_path = os.path.abspath(working_directory)
        
        target_dir = os.path.normpath(os.path.join(abs_path, file_path))    
        
        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        # Will be True or False
        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
        
        #Check Path
        if valid_target_dir == False:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        #Make path
        if not os.path.exists(target_dir):
            os.makedirs(os.path.dirname(target_dir),exist_ok=True)
        
        with open(target_dir,"w") as f:
             f.write(content)
             
             return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        print(f"Error: {e}")