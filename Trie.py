# coding=utf8

from prepareSentences import getRawSentences

#前缀树节点结构
class TrieNode(object):
    def __init__(self):
        # 是否构成一个完成的单词，因为只有小写单词，所以把单词转到0-26之间
        self.is_word = False
        self.children = {}
        self.children_words = []
        self.words = ""
#前缀树的类
class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        """insert a string called s from root."""
        p = self.root
        n = len(s)
        for i in range(n):
            
            if p.children.__contains__(s[i]):
                p = p.children[s[i]]
                if i == n - 1:
                    p.is_word = True
                    p.words = s
                    return
            else:
                new_node = TrieNode()
                if i == n - 1:
                    new_node.is_word = True
                    new_node.words = s
                p.children[s[i]] = new_node
                p = new_node


class solution(object):

    def __init__(self, A):
        self.trie = Trie()
        for i in range(len(A)):
            self.trie.insert(A[i])
    
    # init argument for dp
    def prepare(self, Target, K):
        self.target = Target
        self.k = K
        self.n = len(Target)
        self.res = []

        self.f = [i for i in range(self.n+1)]
        

    # def __init__(self,A,Target,K):
    #     self.target = Target
    #     self.k = K
    #     self.n = len(Target)
    #     self.res = []
        
    #     #init Tire
    #     self.trie = Trie()
    #     for i in range(len(A)):
    #         self.trie.insert(A[i])
            
    #     #init f[""][0,...,n] 
    #     self.f = [i for i in range(self.n+1)]
        
    #dfs函数:在节点p,前缀Sp,f[j]:f[Sp][j]即前缀Sp转换成Target的前j个字符的最小编辑距离。
    #todo:Sp+"a",...,Sp+"z",will update :f-->nf，
    def dfs(self, p,f):
        nf  = [0 for i in range(self.n+1)]
        
        #从root节点开始看是否有A中字符串
        if p.is_word:
            # print("p.word: ", p.words, ', f[n]: ', f[self.n],',f: ', f)

            #这个字符串的最小编辑距离不大于K,加入结果res里
            if f[self.n]<=self.k:
                self.res.append({'word': p.words, 'score': f[self.n]})
                
        #继续向下找p的子节点
        #next prefix's char is i in A
        for i in p.children:
        # for i in range(26):
            #儿子节点为空，跳过
            if p.children[i] == None:
                continue
            #特殊处理nf[0]
            #f[Sq][0] = 0
            #现在Sq-->Sp,也就是f[Sq][0]-->f[Sp][0]，前缀多了一个字符,变成Target[0]
            #因为f[Sp][0] = len(Sp),现在Sp多了一个字符，只要在原来的f[0]基础上加1就可以。
            nf[0] = f[0]+1
            
            #next Target's char is self.target[j-1]
            for j in range(1,self.n+1):
                #case1,2,3###i:Sp-->nf  i-1:Sq-->f
                #f[Sp][j] = min{f[Sp][j-1]+1,        f[Sq][j-1]+1,             f[Sq][j]+1}
                nf[j] = min(nf[j-1]+1,f[j-1]+1,f[j]+1)
                
                #case4
                #f[Sp][j] = min{f[Sp][j],f[Sq][j-1]|Sp[last] = Target[j-1]}
                #把字符转成0-26之间
                if self.target[j-1] == i:
                    
                    nf[j] = min(nf[j],f[j-1])
                # c = ord(self.target[j-1])-ord("a")
                # if i == c:
                #     nf[j] = min(nf[j],f[j-1])
            #寻找子节点
            self.dfs(p.children[i],nf)
        return self.res       
    #也就是从root节点开始深度遍历前缀树，并且更新每一轮的f值，将编辑距离小于K的字符串加到res里，最后返回res

    def dfs2(self, p, f):
        if p.is_word:
            #这个字符串的最小编辑距离不大于K,加入结果res里
            if f[self.n]<=self.k:
                self.res.append({'word': p.words, 'score': f[self.n]})
        


   
    #dfs返回result
    def return_res(self):
        # 直接飞到target[0]
        # p = self.trie.root.children[self.target[0]]
        # self.f[0] = 0
        p = self.trie.root

        res = self.dfs(p,self.f)
        res = sorted(res, key=lambda x: x['score'])
        res = [r['word'] for r in res]
        return res

    def return_prefix(self):
        pass

# A = ["abc","abd","abcd","adc","a"]
# Target = "ac"
# K = 1
# C = solution(A)
# C.prepare(Target, K)
# # C = solution(A,Target,K)
# print(C.return_res())

# chekc restaurant names

# import time
# from gensim.models import Word2Vec
# from WED import WED

# sentences = getRawSentences()
# model = Word2Vec(min_count=2, size=100)
# model.build_vocab(sentences)
# model.train(sentences, total_examples=model.corpus_count, epochs=model.iter)

# # Target = "泰记"
# # Target = "華記小廚"
# # Target = "大街餐廳"
# # Target = "大冒險家餐廳"
# Target = "大冒險家"


# s = time.time()

# print(sentences)
# C = solution(sentences)

# s1 = time.time()

# print("tims: ", s1-s)

# #< int(len(Taget) * 0.6)
# C.prepare(Target, int(len(Target) * 0.6 ))
# print(C.return_res())
# sentences2 = C.return_res()

# s2 = time.time()

# print("tims: ", s2-s)




# params = {"w": 2, "b": 0, "l": 0.5, "m": 0.5}
# wed = WED(embedding=model, params=params)  
# # print(wed.similar('泰記小廚', '華記小廚')) 0.2894707027457877
# # print(wed.similar('泰記小廚', '泰記')) 0.6640544962599546

# mostSimilarity = 1000
# mostSimilarityWord = ''
# for word in sentences2:
#     websimilarity = wed.similar(word, Target)
#     print("word: ", word, ", Target: ", Target,  ", similarity: ", websimilarity)
#     if websimilarity < mostSimilarity:
#         mostSimilarity = wed.similar(word, Target)
#         mostSimilarityWord = word


# print("mostSimilarityWord: ", mostSimilarityWord)
# print("mostSimilarity: ", mostSimilarity)






