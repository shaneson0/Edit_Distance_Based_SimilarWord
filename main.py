
from prepareData import getSentences
import time
from gensim.models import Word2Vec
from WED import WED
from Trie import solution



# prepare model
sentences = getSentences()
model = Word2Vec(min_count=2, size=100)
model.build_vocab(sentences)
model.train(sentences, total_examples=model.corpus_count, epochs=model.iter)

params = {"w": 2, "b": 0, "l": 0.5, "m": 0.5}
wed = WED(embedding=model, params=params)  

def perpareTarget(word):
    suffixs = ['餐廳','餅店','酒家']
    targets = [word + s for s in suffixs]
    return [word] + targets


def findSimilarityWord(target):
    mostSimilarity = 1000
    mostSimilarityWord = ''
    findSimilarityWordStart = time.time()

    C = solution(sentences)

    C.prepare(target, 1)
    sentences2 = C.return_res()

    return_res_time = time.time()

    # print("sentence2: ", sentences2, ',time :', return_res_time - findSimilarityWordStart)
    # sentences2.append(tsentences2)
    for word in sentences2:
        websimilarity = wed.similar(word, target)

        if websimilarity == 0:
            return word

        if websimilarity < mostSimilarity:
            mostSimilarity = websimilarity
            mostSimilarityWord = word
    
    # print("word: ", mostSimilarityWord)
    return mostSimilarityWord





if __name__ == "__main__":
    s = time.time()
    target = "森宝美食"
    res = findSimilarityWord(target)
    print("res: ", res)
    e = time.time()
    print("time: time: %.5f\n", e - s)

