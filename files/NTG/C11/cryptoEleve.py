class symmetricCrypto:

    def __init__(self, message, clef):
        assert (isinstance(message, str)), 'Message doit être une chaine de caractère !'
        self.messageTex = message                # message en clair
        self.messageBin = self.encoder(message)  # message encodé en binaire
        self.clef = self.encoder(clef)           # clé de chiffrement
    
    def encoder(self, message):
        ''' encode le message de texte UTF-8 en binaire '''
        messageBinaire = ''
        for lettre in message:
            messageBinaire += self.completerOctet(f'{ord(lettre):b}')  
        return messageBinaire
    
    def decoder(self, messageBinaire):
        ''' decode le message de binaire vers text UTF-8 '''
        message = ''
        for idx in range(0,len(messageBinaire),8):
            message += chr(int(messageBinaire[idx:idx+8],2))
        return message

    def crypter(self, message = None):
        ''' crypte le message'''
        if message == None: message = self.messageBin
        else : message = message

        maxLen = len(message)
        clefLocale = self.clef
        while len(message) > len(clefLocale) : # on recopie la clef de chiffrement autant de fois que nécessaire.
            clefLocale += self.clef
        clefLocale = clefLocale[:len(message)]
        
        return ''.join([self.xor(message[i], clefLocale[i]) for i in range(maxLen)])

    def decrypter(self, message):
        ''' méthode pour décrypter le message à partir de la clé de chiffrement '''
        pass

    @staticmethod
    def completerOctet(msg):
        ''' complète un octet '''
        while len(msg) % 8 != 0:
            msg = '0' + msg
        return msg

    @staticmethod

    def xor(bit1, bit2):
        ''' porte logique xor
        renvoie un string '0' ou '1' en fonction de la valeur du bit1 et du bit2
        '''
        pass


if __name__ == '__main__':
    ''' à compléter '''
