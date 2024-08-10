class Solution:
    def reverseVowels(self, s: str) -> str:
        # import string
        # translator=str.maketrans('', '', string.punctuation)
        # s=s.translate(translator)
        # if not s.isalpha():
        #     return s
        vowels=['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
        s_list=list(s)
        index_list=[]
        char_list=[]
        # char_list=[char for index in s if char in vowels])

        # index_list, char_list=zip(*[(index,char)for index, char in enumerate(s) if char in vowels])
        for index,char in enumerate(s):
            if char in vowels:
                index_list.append(index)
                char_list.append(char)
        if len(index_list)==0:
            return s
        char_list=char_list[::-1]

        print(char_list)  
        print(index_list)  
      
        for i, c in zip(index_list,char_list):
            s_list[i]=c 


        # index_char_list=[(index,char)for index, char in enumerate(s) if char in vowels]
        # print(index_char_list)
        # char_list=char_list[::-1]
        # print('print',index_list, char_list)
        # for index, item in zip(index_list,char_list):
        #     print(index, item)
        #     s_list[index]=item
        return ''.join(s_list)

            



        