import spacy

nlp = spacy.load('en_core_web_sm')

recipe = open('wood-claudeAI-recipe.txt', 'r')
text = recipe.read()
textstring = str(text)
print(textstring)