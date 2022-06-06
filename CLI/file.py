import os

def create_file(dir, cmdArg):
    with open(f"{dir}\{cmdArg}","w") as f:
        f.write("")
        print("file created")
        

def open_file():
    pass

def del_file():
    pass

if __name__ == '__main__':
    import main
    main.main()