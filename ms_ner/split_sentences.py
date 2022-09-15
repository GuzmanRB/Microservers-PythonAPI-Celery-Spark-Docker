from nltk.tokenize import sent_tokenize

def splitSentences(text,division):
    phrases=sent_tokenize(text)
    output=[phrases[i:i + division] for i in range(0, len(phrases), division)]
    return output