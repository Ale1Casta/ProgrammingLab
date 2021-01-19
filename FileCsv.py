#======================
# Classe per file CSV
#======================

class CSVFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name


<<<<<<< HEAD
    def get_data(self, start=None, end=None):
=======
<<<<<<< HEAD
<<<<<<< HEAD
    def get_data(self, start=None, end=None):
=======
    def get_data(self):
>>>>>>> f8000b3ff3dd57c5b058889892e7579568cae2cd
=======
    def get_data(self):
>>>>>>> origin/main
>>>>>>> 8f495fbaabc69f8a3f9b0a07999d83178ccff670

        # Inizializzo una lista vuota per salvare i valori
        values = []

        # Provo ad aprire il file per estrarci i dati. Se non ci riesco, prima avverto del'errore, 
        # poi devo abortire. Questo e' un errore "un-recoverable", ovvero non posso proseguire con
        # la lettura dei dati se non riesco ad aprire il file!
<<<<<<< HEAD

        try:
            my_file = open(self.name, 'r')
=======
<<<<<<< HEAD
<<<<<<< HEAD
        try: my_file = open(self.name, 'r')
=======
        try:
            my_file = open(self.name, 'r')
>>>>>>> f8000b3ff3dd57c5b058889892e7579568cae2cd
=======
        try:
            my_file = open(self.name, 'r')
>>>>>>> origin/main
>>>>>>> 8f495fbaabc69f8a3f9b0a07999d83178ccff670
        except Exception as e:
            
            # Stampo l'errore
            print('Errore nella lettura del file: "{}"'.format(e))
            
            # Esco dalla funzione tornando "niente".
            return None
        
        # Ora inizio a leggere il file linea per linea
        for line in my_file:
            
            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')

            # Se NON sto processando l'intestazione...
            if elements[0] != 'Date':
                    
                # Setto la data ed il valore
                date  = elements[0]
                value = elements[1]
                
                # La variabile "value" al momento e' ancora una stringa, poiche' ho letto da file di testo,
                # quindi converto a valore floating point, e se nel farlo ho un errore avverto. Questo e'
                # un errore "recoverable", posso proseguire (semplicemente salto la linea).
                try:
                    value = float(value)
                except Exception as e:
                    
                    # Stampo l'errore
                    print('Errore nela conversione a float: "{}"'.format(e))
                    
                    # Vado al prossimo "giro" del ciclo, quindi NON eseguo quanto viene dopo (ovvero l'append)
                    continue
                
                # Infine aggiungo alla lista dei valori questo valore
                values.append(value)
        
        # Chiudo il file
        my_file.close()
        
        # Quando ho processato tutte le righe, ritorno i valori
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f495fbaabc69f8a3f9b0a07999d83178ccff670
        if (start==None and end==None):
            return values
        elif(start>end or start<1):
            return 'Valori incorretti per restituzione dati'
        else:
            try:
                return values[start-1:end]
            except Exception as e:
                print(e)

        return values
    
        
<<<<<<< HEAD

=======
>>>>>>> f8000b3ff3dd57c5b058889892e7579568cae2cd
=======
        return values
    
        
>>>>>>> origin/main
>>>>>>> 8f495fbaabc69f8a3f9b0a07999d83178ccff670
#======================
# Corpo del programma
#======================

mio_file = CSVFile(name='shampoo_sales.csv')
print('Nome del file: "{}"'.format(mio_file.name))
<<<<<<< HEAD

=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f495fbaabc69f8a3f9b0a07999d83178ccff670
print(mio_file.get_data(2,5))
print('Dati contenuti nel file: "{}"'.format(mio_file.get_data()))
<<<<<<< HEAD
=======
>>>>>>> f8000b3ff3dd57c5b058889892e7579568cae2cd
=======
print('Dati contenuti nel file: "{}"'.format(mio_file.get_data()))
>>>>>>> origin/main
>>>>>>> 8f495fbaabc69f8a3f9b0a07999d83178ccff670

