class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        chars_copy=chars
        import random
        last_elm=chars[-1]
        # random_char=random.choice([i for i in chars if i != last_elm])
        chars_copy.append("X")
        s=""
        count=1
        len_chars=len(chars)-1
        chars_copy=chars
        for i in range(len_chars):
            
            print('first in loop char ',chars[i])
            print('first in loop count ',count)

            if chars_copy[i]==chars_copy[i+1]:
                print('current = further increment count')
                print('count before ', count)
                count=count+1
                print('count after ', count)

            else:
                s=s+chars_copy[i]
                print('current != further increment count, reset count')
                if count>1:
                    print('count greater than 1, append')
                    chars[i]=count
                    s=s+str(count)
                    print('string count appended ', s)
                    # chars[i]=count
                count=1
                print('resetted count ', count)
            
        print('prior chars ' , chars)
        print('final string ' ,s)
        chars[:]=list([str(ch) for ch in s])
        print('final chars ', chars)
        return len(s)


        