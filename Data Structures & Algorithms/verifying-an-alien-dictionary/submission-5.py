class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        word_order = {char: i for i, char in enumerate(order)}

        for i in range(len(words)-1):
            current_word = words[i]
            next_word=words[i+1]

            for j in range(min(len(current_word), len(next_word))):
                if current_word[j] == next_word[j]:
                    continue

                if word_order[current_word[j]] > word_order[next_word[j]]:
                    return False

                break;
            else:
                if len(current_word)>len(next_word):
                    return False
        
        return True