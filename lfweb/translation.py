from modeltranslation.translator import translator, TranslationOptions
from models import Collection, Yarn, News, Tecnicalcard

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'abstract','text','slug')

translator.register(News, NewsTranslationOptions)


class CollectionTranslationOptions(TranslationOptions):
    fields = ('name','title', 'abstract','description','slug')

translator.register(Collection, CollectionTranslationOptions)

class YarnTranslationOptions(TranslationOptions):
    fields = ('name','title',)

translator.register(Yarn, YarnTranslationOptions)

class TecnicalcardTranslationOptions(TranslationOptions):
    fields = ('alttext',)

translator.register(Tecnicalcard, TecnicalcardTranslationOptions)

