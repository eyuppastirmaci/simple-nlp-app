from gensim.models import Word2Vec
import pandas as pd


class WordVector:
    """
    Kelime vektör sınıfı.
    """

    def __init__(self, path: str, encoding: str):
        """
        Yapıcı metot.
        """
        self._data = pd.read_csv(path, encoding=encoding).text.tolist()
        self._corpus = self.__get_corpus()
        self.word_embedding = self.__get_model(1)
        self.model_cbow = self.__get_model(0)

    def __get_model(self, sg):
        """
        Kelime vektör modeli oluşturan metot
        """
        return Word2Vec(self._corpus, sg=sg)

    def __get_corpus(self):
        corpus = []
        for sentence in self._data:
            corpus.append(sentence.split())
        return corpus