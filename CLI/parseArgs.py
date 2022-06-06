import os, sys
import file
import youtube

"""
parser ['command', 'args1', 'args2']
"""

def parse():
    dir = os.getcwd()
    while True:
        args = input(dir + '>')
        args = args.split(' ')

        try: 
            match args[0]:
                case "cd":
                    if cd(args[1]):
                        dir = args[1]
                    else:
                        print("Not a directory")

                case "echo":
                    echo(args)
                        
                case "exit":
                    cli_exit()
                
                case "clear":
                    clear()
                    
                case "cls":
                    clear()
                    
                case "touch":
                    file.create_file(dir, args[1])

                case "open":
                    file.open_file(dir, args[1])

                case "del":
                    file.del_file(dir, args[1])

                case "webm":
                    youtube.webm_download(args[1])

                case "mp4":
                    youtube.mp4_download(args[1])
                    
        except IndexError:
            print("Please fill in all proper arguments")
                
# Checks if the directory exists and returns a boolean
def cd(dir):
    if os.path.isdir(dir):
        return True
    else:
        return False

def echo(msg):
    for text in msg[1:]:
        print(text + " ", end='')
    print()

def cli_exit():
    sys.exit(0)
    
def clear():
    os.system('cls||clear')
    
if __name__ == '__main__':
    import main
    main.main()