from preprocess import TweetPreProcess
from data_file import DataFile
from word_vector import WordVector


def preprocessing(column_index, data_path, encoding, meta_characters, out_path):
    # Ön işleme
    preprocess = TweetPreProcess(meta_characters)
    data_file = DataFile(data_path, preprocess, out_path, encoding)
    data_file.pre_process_column(column_index)


def word_embedding(encoding, out_path):
    # Kelime gömme
    word_vector = WordVector(out_path, encoding)
    model_sg = word_vector.model_sg
    model_cbow = word_vector.model_cbow

    # Skip-Gram modelinin yukarı kelimesiyle ilişkilendirdiği kelimeler.
    print(model_sg.wv.most_similar("yukarı"))
    print(model_cbow.wv.most_similar("yukarı"))
    print("***************")
    print(model_sg.wv.most_similar("boğa"))
    print(model_cbow.wv.most_similar("boğa"))
    print("***************")
    print(model_sg.wv.most_similar("ayı"))
    print(model_cbow.wv.most_similar("ayı"))


def main():
    # Parametreler
    meta_characters = ["rt ", "\n", "\t"]
    column_index = 8
    data_path = "data/data.csv"
    out_path = "data/preprocessed-data.csv"
    encoding = 'utf-8'

    preprocessing(column_index, data_path, encoding, meta_characters, out_path)
    word_embedding(encoding, out_path)


if __name__ == "__main__":
    main()
