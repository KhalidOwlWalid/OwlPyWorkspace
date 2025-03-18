from pkg_resources import resource_filename, resource_isdir

def read_file():
    # Get the absolute path to the file
    file_path = resource_filename("my_custom_package", "data/example.txt")
    print(file_path)
    is_valid_dir = resource_isdir("my_custom_package", "data")
    print(is_valid_dir)
    
    # Read and print the file content
    with open(file_path, "r") as file:
        content = file.read()
    print(content)

if __name__ == "__main__":
    read_file()