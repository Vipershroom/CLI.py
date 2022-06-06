import os
import errno

def create_file(dir, cmdArg):
    with open(f"{dir}\{cmdArg}","w") as f:
        f.write("")
        print(f"file {cmdArg} created")
        

def open_file(dir, cmdArg):
    with open(f"{dir}\{cmdArg}", 'r') as f:
        lines = f.readlines()

        if len(lines) > 100:
            print("WARNING! your file is over 100 lines.\nProceed? (Y/n)")
            resp = input()
            if resp == 'n':
                return

        for line in lines:
            print(line, end='')
        print()
        
def del_file(dir, cmdArg):
    print(f"Are you sure you would like to delete {cmdArg} in {dir}? \n(Y/n)")
    resp = input()
    if resp == 'n':
        return
    try:
        os.remove(cmdArg)
        print(f"File {cmdArg} deleted")
    except (FileNotFoundError, PermissionError) as error:
        print(f"Error deleting file, {error}")

if __name__ == '__main__':
    import main
    main.main()