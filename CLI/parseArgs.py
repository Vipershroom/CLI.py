import os, sys
import file

"""
parser ['command', 'args1', 'args2']
"""

def parse():
    dir = os.getcwd()
    while True:
        args = input(dir + '>')
        args = args.split(' ')
        
        match args[0]:
            case "cd":
                if cd(args[1]):
                    dir = args[1]
                else:
                    print("Not a directory")
                    
            case "exit":
                cli_exit()
                
            case "touch":
                file.create_file(dir, args[1])
                
# Checks if the directory exists and returns a boolean
def cd(dir):
    if os.path.isdir(dir):
        return True
    else:
        return False
    
def cli_exit():
    sys.exit(0)
    
if __name__ == '__main__':
    import main
    main.main()