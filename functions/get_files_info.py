import os

def get_files_info(working_directory, directory="."):
    working_directory_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_path, directory))
    valid_target_dir = os.path.commonpath([working_directory_path, target_dir])
    
    if valid_target_dir != working_directory_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(target_dir) == False:
        return f'Error: "{directory}" is not a directory'

    output_string = ""

    for item in os.listdir(target_dir):
        try:
            abs_path = os.path.join(target_dir, item)
            current_item_size = os.path.getsize(abs_path)
            current_item_is_dir = os.path.isdir(abs_path)
        except:
            return f"Error: Unable to get info about {item}"

        output_string += f"- {item}: file_size={current_item_size} bytes, is_dir={current_item_is_dir}\n"
    
    return output_string