from scanner import Scanner
ff
def main():
    s = Scanner('not true or false')
    tokens = s.scanAll()
    print(tokens)

if __name__ == '__main__':
    main()
