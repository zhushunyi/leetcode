class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        sentence_set = sentence.split(' ')
        for i in dict:
            for j in range(0,len(sentence_set)):
                k = len(i)
                if i == sentence_set[j][:k]:
                    sentence_set[j] = i
        return ' '.join(sentence_set)



#hash
def replaceWords(self, roots, sentence):
    rootset = set(roots)

    def replace(word):
        for i in xrange(1, len(word)):
            if word[:i] in rootset:
                return word[:i]
        return word

    return " ".join(map(replace, sentence.split()))
