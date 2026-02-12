import os
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Return file content from a specified file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(type=types.Type.STRING, description="Path to the Python file to run"),
            "working_directory": types.Schema(type=types.Type.STRING, description="Directory to run the file in"),
        },
        required=["file_path"],
    ),
)
def get_file_content(working_directory, file_path):
        try:
        
            abs_path = os.path.abspath(working_directory)
            
            target_dir = os.path.normpath(os.path.join(abs_path, file_path))    
            
            if not os.path.isfile(target_dir):
                return f'Error: File not found or is not a regular file: "{file_path}"'
            
            # Will be True or False
            valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
            
            if valid_target_dir == False:
                return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
            
            content = ""
            MAX_CHARS =10000
            with open(target_dir) as f:
                file_content_string = f.read(MAX_CHARS)
                content += file_content_string
                if f.read(1):
                    content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
        except Exception as e:
            print(f"Error: {e}")
        