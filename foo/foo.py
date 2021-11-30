import os

def dump_file(file_path):
    print(file_path + ":")
    with open(file_path) as file:
        print(file.read())

def main():
    data_files = [
        'local-data.txt', # No problems here
        # What path should I use to access @data//:external-data.txt?
    ]
    for file in data_files:
        dump_file(file)

    print("cwd: " + os.getcwd())

if __name__ == "__main__":
    main()
