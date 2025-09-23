

def lee_archivo():
    filename = "foto.txt"
    filename2 = "foto2.txt"

    with open(filename, "r") as f1, open(filename2, "r") as f2:
        content1 = f1.read()
        content2 = f2.read()

        i = 0
        while i < len(content1) and i < len(content2):
            if content1[i] != content2[i]:
                print(f"La diferencia inicia en el carácter {i + 1}")
                print("foto.txt :", content1[i:i+50])
                print("foto2.txt:", content2[i:i+50])
                return
            i += 1

        if len(content1) != len(content2):
            print(f"La diferencia inicia en el carácter {i + 1} (uno de los archivos tiene mas caracteres)")
            print("foto.txt :", content1[i:i+50])
            print("foto2.txt:", content2[i:i+50])
        else:
            print("Los archivos son iguales.")

lee_archivo()
    

