class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = collections.defaultdict(list)

        for p in paths:
            temp = list(p.split(' '))
            add = temp[0]
            for t in temp[1:]:
                path,content = t.split('(')
                files[content[:-1]].append(add+'/'+path)
        
        return [i for i in files.values() if len(i)>1]
