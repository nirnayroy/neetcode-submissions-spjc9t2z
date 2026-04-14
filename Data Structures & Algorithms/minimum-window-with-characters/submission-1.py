class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_dict, reqd_dict = {}, {}
        min_substr = ''
        have, need = 0, 0

        ptr = 0
        for char in t:
            if char not in reqd_dict:
                need += 1
                reqd_dict[char] = 1
                char_dict[char] = 0
            else:
                reqd_dict[char] += 1

        for n, c in enumerate(s):
            if c in reqd_dict:
                char_dict[c] += 1
                if char_dict[c] == reqd_dict[c]:
                    have += 1

                while have == need:
                    if s[ptr] in char_dict:
                        char_dict[s[ptr]] -= 1
                        if char_dict[s[ptr]] < reqd_dict[s[ptr]]:
                            have -= 1
                    ptr += 1
                    if min_substr == '':
                        min_substr = s[ptr-1:n+1]
                    if len(min_substr) > n-ptr+1:
                        min_substr = s[ptr-1:n+1]


        return min_substr


            
                

            

                