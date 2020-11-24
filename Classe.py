
# oggetto CSVFile
#    - init(filename)
#    - name
#    -  get_data()
#       return dati


class CSVFile:
    def __init__(self, name):
        self.filename = name

    def get_data(self):
        return [1,2,3,4]    

mio_file = CSVFile(name='shampoo_sales.csv')

print(mio_file.name)
print(mio_file.get_data())

