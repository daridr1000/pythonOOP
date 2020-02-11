class InputOutString:
    def __init__(self):
        self.word = self.get_string()
    @staticmethod
    def get_string():
        return  input("Type a word! ")
    def print_string(self):
        print(self.word.upper())
    def is_palyndrome(self):
        return self.word==self.word[::-1]
string=InputOutString()
string.print_string()
print(string.is_palyndrome())
print(len(string.word))