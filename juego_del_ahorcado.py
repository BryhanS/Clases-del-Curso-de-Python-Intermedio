
#Funcion para leer la informacion
with open("./archivos/data.txt", "r",encoding="utf-8") as f:
        list_data = {
            'id':'',
            'word': ''
        }
        list_data = list(enumerate([i.rstrip("\n") for i in f]))

print(list_data[1])
#def run():
#    data()

#if __name__ == '__main__':
#    run()