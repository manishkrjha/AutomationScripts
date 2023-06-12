import os

def add_spaces_to_files(directory_path, num_spaces):
    
    txt_files = [file for file in os.listdir(directory_path) if file.endswith('.txt')]

    for file_name in txt_files:
        file_path = os.path.join(directory_path, file_name)

    
        with open(file_path, 'r') as file:
            lines = file.readlines()

    
        lines_with_spaces = [line.rstrip() + ' ' * num_spaces + '\n' for line in lines]

    
        with open(file_path, 'w') as file:
            file.writelines(lines_with_spaces)

    print("Spaces added to all files.")

# Add folder path here
directory_path = 'TextFiles'
num_spaces = 73


add_spaces_to_files(directory_path, num_spaces)
