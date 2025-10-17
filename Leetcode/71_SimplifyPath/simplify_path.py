class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        simple_path = []
        for i in range(len(path)):
            if path[i] == "" or path[i] == ".":
                continue
            elif path[i] == "..":
                if simple_path:
                    simple_path.pop()
            else:
                simple_path.append(path[i])
        return "/" + "/".join(simple_path)

if __name__ == '__main__':
    print(Solution().simplifyPath("/home/user/Documents/../Pictures"))
    print(Solution().simplifyPath("/home/"))
    print(Solution().simplifyPath("/home//foo/"))
    print(Solution().simplifyPath("/../"))
    print(Solution().simplifyPath("/.../a/../b/c/../d/./"))


