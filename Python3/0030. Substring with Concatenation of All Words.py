class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_dic = {}
        for i in words:
            if i not in word_dic:
                word_dic[i] = 1
            else:
                word_dic[i] += 1
        res = []
        n = len(s)
        w_len = len(words[0])
        w_num = len(words)
        for i in range(n-w_len*w_num+1):
            t_dic = dict(word_dic)
            for j in range(i,i+w_len*w_num,w_len):
                if(s[j:j+w_len] in t_dic):
                    t_dic[s[j:j+w_len]] -= 1
                    if(t_dic[s[j:j+w_len]]==0):
                        del t_dic[s[j:j+w_len]] 
                else:
                    break
            if not t_dic:
                res.append(i)
        
        return res
