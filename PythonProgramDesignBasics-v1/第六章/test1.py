def main():
    test1_file = open("test1_file.py","w")
    for i in range(2):
        test1_file.write(f"{input(": ")}\n")

if __name__=="__main__":
    main()