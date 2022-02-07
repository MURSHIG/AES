from AesEverywhere import aes256


def main():
    inp = int(input("What do you want?\nEncrypt(1)\nDecrypt(2)\n"))
    if inp == 1:
        inp = int(input("What to encrypt?\nFile(1)\nText(2)\n"))
        if inp == 1:
            path = input("Drag'n drop file\n").split(" ")[0]
            decr = open(path, "r").read()
            encr = aes256.encrypt(decr, input("Password\n"))
            lenght_of_file = len(path.split("/")[-1])
            path_to_write = path[:-lenght_of_file] + "encrypted_" + path.split("/")[-1]
            open(path_to_write, "wb").write(encr)
            print(f"This writed to {path_to_write}\n: {encr} ")
        else:
            encr = aes256.encrypt(input("What the text to encrypt?"), input("Password\n"))
            print(f"Output: \n{encr} ")
    else:
        inp = int(input("What to decrypt?\nFile(1)\nText(2)\n"))
        if inp == 1:
            path = input("Drag'n drop file\n").split(" ")[0]
            encr = open(path, "r").read()
            decr = aes256.decrypt(encr, input("Password\n"))
            lenght_of_file = len(path.split("/")[-1])
            path_to_write = path[:-lenght_of_file] + "decrypted_" + path.split("/")[-1]
            open(path_to_write, "wb").write(decr)
            print(f"This writed to {path_to_write}\n: {decr} ")
        else:
            decr = aes256.decrypt(input("What the text to decrypt?"), input("Password\n"))
            print(f"Output: \n{decr} ")


if __name__ == '__main__':
    main()
