import os
def get_files_info(working_directory, directory="."):
    try:
        
        abs_path = os.path.abspath(working_directory)
        
        target_dir = os.path.normpath(os.path.join(abs_path, directory))    
        
        if not os.path.isdir(target_dir):
            return f'Error: "{target_dir}" is not a directory'
        
        # Will be True or False
        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
        
        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        contents = os.listdir(target_dir)
        return_string = f"Result for {directory} directory:\n"
        if directory == ".":
            return_string = f"Result for current directory:\n"
        else:
             return_string = f"Result for '{directory}' directory:\n"
        for i, X in enumerate(contents):
            name = X
            file_size = os.path.getsize(target_dir+'/'+X)
            is_dir = os.path.isdir(target_dir+'/'+X)
            return_string += f"- {name}: file_size={file_size} bytes, is_dir={is_dir}"
            if i+1 < len(contents):
                    return_string += "\n"
        return return_string
    except Exception as e:
        print(f"Error: {e}")
    