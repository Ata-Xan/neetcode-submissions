class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        words_number=len(words)
        alphabet_number=len(order)
        if not 1<=words_number<=100:
            raise ValueError("The number of words should be between 1 and 100")
        
        if alphabet_number != 26:
            raise ValueError("The number of alphabet should be 26")

        word_order={v:k for k, v in enumerate(order)}

        words_length = [0]*words_number
        for i in range(words_number-1):
            current_word=words[i]
            next_word=words[i+1]
            if not words_length[i]:
                words_length[i]=len(current_word)
            words_length[i+1]=len(next_word)
            longest=max(words_length[i], words_length[i+1])
            # shortest=min(words_length[i], words_length[i+1])
            for j in range(longest):
                if j>words_length[i]-1:
                    break
                elif j>words_length[i+1]-1:
                    return False
                if word_order[current_word[j]]==word_order[next_word[j]]:
                    continue
                elif word_order[current_word[j]]<word_order[next_word[j]]:
                    break
                else:
                    return False  
        return True
