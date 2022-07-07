class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count_num_max = 0
        for sentence in sentences:
            count_num_current = len(sentence.split())
            if count_num_current > count_num_max:
                count_num_max = count_num_current
        return count_num_max