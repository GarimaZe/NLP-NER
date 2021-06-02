import spacy

spacy_nlp=spacy.load('zh_core_web_sm')
document = spacy_nlp("To enrich my prospective organization & myself by constantly taking on new challenges, learning new skills and applying them to become a successful professional and to serve for the betterment of my organization.To enrich my prospective organization & myself by constantly taking on new challenges, learning new skills and applying them to become a successful professional and to serve for the betterment of my organization.")
for span in document.sents:
    sentence = [document[i] for i in range(span.start, span.end)]
    print(sentence)