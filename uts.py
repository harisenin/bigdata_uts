import spacy

sp = spacy.load('en_core_web_sm')

sentence = sp(u'Saya Bangga Jadi Warga Nahdlatul Ulama')

for word in sentence:
    print(word.text)