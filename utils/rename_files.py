import os

base_dir = r"C:\Users\Pedro\Documents\dados_organizados"

if os.path.isdir(base_dir):
    
    for folder_name in os.listdir(base_dir): # List all the folders inside a directory
        path_folder = os.path.join(base_dir, folder_name)

        if os.path.isdir(path_folder):
            counter = 1
            
            for file_name in os.listdir(path_folder): # List all the files inside a specific dog folder
                file_extension = os.path.splitext(file_name)[1] # Get the file extension (ex: .jpg, .png)
                
                new_file_name = f"{folder_name}_{counter}{file_extension}" # Structure new file name
                
                old_path = os.path.join(path_folder, file_name) # Get old file path
                new_path = os.path.join(path_folder, new_file_name) # Get new file path
                                
                os.rename(old_path, new_path) # Rename the file
                
                counter += 1
                
    print("\nAll the files was succeced renamed!")