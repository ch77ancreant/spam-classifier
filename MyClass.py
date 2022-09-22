
class Mail:
    
    def __init__(self, column_names, my_mail):
        self.column_names = column_names
        self.my_mail = my_mail
        
    def get_occurrences(self):
        
        word_in_mail = self.my_mail.split(" ")
        num_occurrences = []
        for col in self.column_names:
            n = 0
            for word in word_in_mail:
                if len(col) <= len(word):
                    for i in range(len(word)-len(col)+1):
                        if col == word[i:i+len(col)]:
                            n += 1
                            
            num_occurrences.append(n)
            
        return num_occurrences
    
    