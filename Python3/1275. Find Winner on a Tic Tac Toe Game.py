class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        A = [0]*8
        B = [0]*8
        l = len(moves)
        for n in range(l):
            if n%2:
                B[moves[n][0]] += 1
                B[moves[n][1]+3] += 1
                if moves[n][0]==moves[n][1]:
                    B[6]+=1
                if moves[n][0]+moves[n][1]==2:
                    B[7]+=1
            else:
                A[moves[n][0]] += 1
                A[moves[n][1]+3] += 1
                if moves[n][0]==moves[n][1]:
                    A[6]+=1
                if moves[n][0]+moves[n][1]==2:
                    A[7]+=1

        if max(A)==3:
            return 'A'
        elif max(B)==3:
            return 'B'
        elif l==9:
            return 'Draw'
        else:
            return 'Pending'

作者：heimisa000
链接：https://leetcode-cn.com/problems/find-winner-on-a-tic-tac-toe-game/solution/pythonyong-listchu-cun-huo-sheng-qing-kuang-by-hei/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
