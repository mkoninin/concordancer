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

text = 'Носила свитер недолго, но уже появились катышки, затяжки, быстро растянулся. . На свитере никакой информации о производителе, о том, как ухаживать за ним. Ну и качество, конечно, оставляет желать лучшего. За эти деньги точно что-то ещё получше можно найти. В общем, жаль потраченных денег. А продавцу следует лучше выбирать то, что он продаёт. Хотя, наверное, ему плевать. Скорее всего, покупает на Садоводе и перепродает. А там, мне прекрасно известно, какое г..но может продаваться'


# %%
from razdel import sentenize
from razdel import tokenize

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
print(doc.token)
# %%

for token in doc.tokens:
    # if token.lemma == 'мыть':
    print(token) 
# %%
