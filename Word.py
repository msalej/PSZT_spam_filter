class Word:

    def __init__(self, word):
        self.word=word
        self.spam=0
        self.ham=0

    def add_spam(self):
        self.spam=self.spam+1

    def add_ham(self):
        self.ham=self.ham+1

    def probability_spam(self):
        sum=self.spam+self.ham
        if sum==0:
            return 0
        else:
         return self.spam/(self.spam+self.ham)

    def probability_ham(self):
        sum=self.spam+self.ham
        if sum==0:
            return 0
        else:
         return self.ham/(self.spam+self.ham)







































