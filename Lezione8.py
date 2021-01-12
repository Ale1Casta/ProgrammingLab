#======================
# Classe per file CSV
#======================

class CSVFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name


    def get_data(self, start=None, end=None):

        # Inizializzo una lista vuota per salvare i valori
        values = []

        # Provo ad aprire il file per estrarci i dati. Se non ci riesco, prima avverto dell'errore, 
        # poi devo abortire. Questo e' un errore "un-recoverable", ovvero non posso proseguire con
        # la lettura dei dati se non riesco ad aprire il file!
        try: my_file = open(self.name, 'r')
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
                    print('Errore nella conversione a float: "{}"'.format(e))
                    
                    # Vado al prossimo "giro" del ciclo, quindi NON eseguo quanto viene dopo (ovvero l'append)
                    continue
                
                # Infine aggiungo alla lista dei valori questo valore
                values.append(value)
        
        # Chiudo il file
        my_file.close()
        
        # Quando ho processato tutte le righe, ritorno i valori
        if (start==None and end==None):
            return values
        elif(start>end or start<1):
            return 'Valori incorretti per restituzione dati'
        else:
            try:
                return values[start-1:end]
            except Exception as e:
                print(e)

#=================
# parte lezione 8
#=================

class Model(object):

    def fit(sef, data):
        pass

    def predict(self):
        pass

class IncrementModel(Model):

    def fit(self, data):
        raise NotImplementedError('Questo modello non prevede un fit')

    def predict(self, prev_months):

        incr=0

        for i in range(len(prev_months)-1):
            incr+=prev_months[i+1]-prev_months[i]

        return prev_months[len(prev_months)-1]+incr/(len(prev_months))




#======================
# Corpo del programma
#======================

mio_file = CSVFile(name='shampoo_sales.csv')

print('Nome del file: "{}"'.format(mio_file.name))
print(mio_file.get_data(2,5))

modello= IncrementModel()
print(modello.predict(mio_file.get_data(2,5)))
