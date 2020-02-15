class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            s = list(IP.split('.'))
            if len(s) != 4:
                return "Neither"
            for c in s:
                if not c.isdigit() or int(c)>255 or str(int(c)) != c:
                    return "Neither"
            
            return "IPv4"

        else:
            set_alnum = set(str(i) for i in range(10)) | set(chr(i) for i in range(ord('a'),ord('g'))) | set(chr(i) for i in range(ord('A'),ord('G')))

            s = list(IP.split(':'))
            if len(s) != 8:
                return "Neither"
            for c in s:
                if len(c)<1 or len(c)>4 or len(set(c)|set_alnum)>22:
                    return "Neither"
            
            return "IPv6"
