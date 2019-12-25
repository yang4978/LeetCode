class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain = {}
        for s in cpdomains:
            num, s = s.split(" ")
            num = int(num)
            part = s.split(".")
            temp = ""
            
            for i in range(len(part)-1,-1,-1):
                temp = part[i] + '.' + temp if temp else part[i]
                if temp not in domain:
                    domain[temp] = num
                else:
                    domain[temp] += num
            
        return [str(num)+" "+s for s,num in domain.items()]
