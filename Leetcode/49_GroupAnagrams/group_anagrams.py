from typing import List, Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # худшее
        dict_groups = []
        ans = []
        for s in strs:
            word_dict = dict(Counter(s))
            for i, checker in enumerate(dict_groups):
                if word_dict == checker[0]:
                    dict_groups[i].append(word_dict)
                    ans[i].append(s)
                    break
            else:
                dict_groups.append([word_dict])
                ans.append([s])
        return ans

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        # не нужно привязываться к количеству букв в слове,
        # можно сортировать буквы в словах и это использовать как хэш
        sort_hash = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in sort_hash:
                sort_hash[sorted_s] = []
            sort_hash[sorted_s].append(s)
        return list(sort_hash.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams1(["eat","tea","tan","ate","nat","bat"]))