class sentence:
    def __init__(self, string, tone=None):
        self.string = str(string)
        self.length = len(self.string)
        self.words = len(self.string.split())
        self.tone = tone

    def correct(self):
        x = ''
        word_list = self.string.split()
        for word in word_list:
            x = x + ' ' + word
        x = x.rstrip()
        x = x.lstrip()
        x = x[0].capitalize() + x[1:len(x)]
        if (x[len(x) - 1] == '.' and (self.tone == 'Assertive.' or not self.tone)) or (
                x[len(x) - 1] == '?' and self.tone == 'Interrogative.') or (
                x[len(x) - 1] == '!' and self.tone == 'Exclamative.'):
            pass
        else:
            if self.tone == 'Interrogative.':
                if x.endswith('.') or x.endswith('!'):
                    x = x[0:len(x)-1] + '?'
                else:
                    x = x[0:len(x)] + '?'
            elif self.tone == 'Assertive.' or not self.tone:
                if x.endswith('?') or x.endswith('!'):
                    x = x[0:len(x) - 1] + '.'
                else:
                    x = x[0:len(x)] + '.'
            elif self.tone == 'Exclamative.':
                if x.endswith('.') or x.endswith('?'):
                    x = x[0:len(x) - 1] + '!'
                else:
                    x = x[0:len(x)] + '!'
        self.string = x
        return self.string


sen = sentence(input('Type:'))
y = sen.correct()
print(y)
