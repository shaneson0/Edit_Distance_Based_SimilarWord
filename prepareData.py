import json

def getSentences():
    with open('./restaurant.json', 'r') as fp:
        res = json.load(fp)
        return res
    


if __name__ == "__main__":
    sentence = getSentences()
    print(sentence)





