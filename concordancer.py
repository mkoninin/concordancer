# %%

class concordancer:
    def __init__(documents: list) -> None:
        '''
        на входе список со строками, которые он разберет на предложения и леммы-слова-синтакс.разбор и т.д.
        '''
        pass

    def lemma(lemma: str) -> list[tuple]:
        '''
        на входе лемма слова
        на выходе - список с адресами где встречаются слова с данной леммой
        '''
        pass

    def word(word: str) -> list[tuple]:
        pass

# %%

text = 'Мама мыла раму. Рама мыла маму.'


# %%
from razdel import sentenize
from razdel import tokenize

# %%
sentences = list(sentenize(text))

for sentence in sentences:
    print(list(tokenize(sentence.text)))
# %%
sentence.text
# %%

from natasha import (
    Segmenter,
    MorphVocab,
    
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    
    PER,
    NamesExtractor,

    Doc
)
segmenter = Segmenter()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
morph_vocab = MorphVocab()

doc = Doc(text)
# %%
doc.segment(segmenter)

doc.tag_morph(morph_tagger)
doc.parse_syntax(syntax_parser)
for token in doc.tokens:
    token.lemmatize(morph_vocab)
print(doc.tokens)
# %%

for token in doc.tokens:
    if token.lemma == 'мыть':
        print(token) 
# %%
