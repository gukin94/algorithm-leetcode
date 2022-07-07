class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(list(map(lambda sentence: len(sentence.split()), sentences)))