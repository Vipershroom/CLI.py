import os

def parse():
    cwd = os.getcwd()
    args = input(cwd + '>')
    args = args.split(' ')
    print(args)
    
if __name__ == '__main__':
    import main
    main.main()