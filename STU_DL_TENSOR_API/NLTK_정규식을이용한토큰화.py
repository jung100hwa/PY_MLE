from nltk.tokenize import RegexpTokenizer

text = "Hello th!ere! How's everything going? Call me at 123-456-7890."

tokenizer = RegexpTokenizer(r'[\w]+')
print(tokenizer.tokenize(text))

tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
print(tokenizer.tokenize(text))

tokenizer = RegexpTokenizer(r'\s+', gaps=True)
print(tokenizer.tokenize(text))

tokenizer = RegexpTokenizer(r'\s+', gaps=False)
print(tokenizer.tokenize(text))