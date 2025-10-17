class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_table = {}
        for i in range(len(s)):
            if s[i] in map_table:
                if map_table[s[i]] != t[i]:
                    return False
            else:
                if t[i] in map_table.values():
                    return False
                map_table[s[i]] = t[i]
        return True

    def isIsomorphic1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_t = {}
        map_t_s = {}

        for ch_s, ch_t in zip(s, t):
            if ch_s in map_s_t and map_s_t[ch_s] != ch_t:
                return False
            if ch_t in map_t_s and map_t_s[ch_t] != ch_s:
                return False

            map_s_t[ch_s] = ch_t
            map_t_s[ch_t] = ch_s

        return True

if __name__ == '__main__':
    print(Solution().isIsomorphic("badc","baba"))
    print(Solution().isIsomorphic("egg","add"))
    print(Solution().isIsomorphic("foo","bar"))
    print(Solution().isIsomorphic("paper","title"))
