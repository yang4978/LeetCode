class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        word_length = {}                   # 记录每个单词的长度，方便后续使用
        l = len(words)                     # 计算总共多少个单词

        for i in range(l):
            word_length[i] = len(words[i]) # 计算每个单词长度，用单词的序号作为标志
        
        res = []                           # 结果
        temp_length = 0                    # 当前单词串中，字母的总个数
        word_list = []                     # 当前单词串

        for i in range(l):                                                                      
            if temp_length + len(word_list) + word_length[i] <= maxWidth:
                                            # 如果要满足单词串中可以新加一个单词，必须保证
                                            # 原字符串的字母数 + 间隔数 + 新单词的字母数 <= maxWidth
                                            # 由于单词之间最小间隔为1
                                            # 加上新单词后，单词串中的间隔数为 原字符串的单词书
                                            # 比如原来单词串中有['dog', 'cat', 'bird'] 3个单词
                                            # 原字符串字母数为 3+3+4 = 11
                                            # 加入新单词'fish'后，总共4个单词
                                            # 他们中间有3个空隙，不等式可以写成：
                                            # 11 + 3（间隔） + 4（'fish'字母数） <= maxWidth

                                            # 如满足上述条件，在word_list里添加单词，更新temp_length
                temp_length += word_length[i]
                word_list.append(words[i])


                                            # 否则说明这一行已经无法填入新单词
                                            # 开始向res里加入这一行
            else:
                n = len(word_list)          # 单词个数

                                            # 这一行可以填入的空格数：
                                            # 空格数 = maxWidth - 单词串的字母总数temp_length
                space = maxWidth - temp_length      

                if n == 1:                  # 如果这一行只有一个单词
                                            # 填入单词和所需要的空格即可
                    res.append(word_list[-1]+' '*space)              

                                            # 如果这一行有多个单词
                                            # 计算每个间隙需要的空格数
                else:
                    n_i = n - 1             # 间隔数

                                            # 由于空格数是尽可能均匀分配的
                                            # 假设space = a * n_i + b
                                            # 即 space // n_i = a 且 space % n_i = b
                                            # 那么所有的间隔都有至少a个空格
                                            # 又由于左侧放置的空格要更多
                                            # 所以从左往右数的前b个间隔，每个要多一个空格
                    a = space // n_i
                    b = space % n_i

                                            # 现在开始书写句子
                    sentence = ''           
                                            # 注意这里的循环不能用i，否则会刷新原来循环中的i，造成错误
                    for k in range(n_i):      
                        interval_num = a    # 所有的间隔都有至少a个空格

                                            # 从左往右数的前b个间隔，每个要多一个空格
                        if k < b:
                            interval_num += 1
                        sentence += word_list[k] + ' '*interval_num
                    
                                            # 由于n_i = n - 1，也就是说最后一个单词没有填写
                                            # 所以sentence += 最后一个单词
                    sentence += word_list[-1]
                    res.append(sentence)    # 将句子填入结果res

                                            # 一行代码的简洁版如下
                                            # 直接代替else下面的全部内容→_→
                    #res.append(('').join([word_list[k]+' '*(space//(n-1)+int(k<space%(n-1))) for k in range(n-1)])+word_list[-1])
                
                                            # 句子填入之后，不要忘了现在循环到的单词
                                            # 新的单词序列里只有这一个单词
                                            # 更新单词序列word_list和单词串的字母数temp_length
                temp_length = word_length[i]
                word_list = [words[i]]

                                            # 最后一行的情况比较特殊
                                            # 每个单词之间只有1个空格
                                            # 句子剩余部分用空格补齐
            if i == l - 1:
                n_i = len(word_list) - 1    # 间隔数
                                            # 由于每个间隔只填入一个空格
                                            # 空格数 = maxWidth - 单词串的字母数 - 间隔数
                space = maxWidth - temp_length - n_i

                                            # 填写sentence
                                            # 逻辑和之前一样，只不过填入空隙的空格只有一个
                sentence = ''

                for k in range(n_i):
                    sentence += word_list[k] + ' '

                sentence += word_list[-1]

                sentence += ' ' * space     # 把剩下的空格补齐
                res.append(sentence)


                                            # 同样，一行代码的简洁版如下
                                            # 直接代替if i == l - 1:下面的全部内容→_→
                #res.append((' ').join(word_list)+' '*(maxWidth-temp_length-(len(word_list)-1)))
        return res
