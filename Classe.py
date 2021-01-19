
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
<<<<<<< HEAD
=======

<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> f8000b3ff3dd57c5b058889892e7579568cae2cd
=======
>>>>>>> origin/main
>>>>>>> 8f495fbaabc69f8a3f9b0a07999d83178ccff670
