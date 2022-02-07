"""
We are playing the Guessing Game. The game will work as follows:

    I pick a number between 1 and n.
    You guess a number.
    If you guess the right number, you win the game.
    If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
    Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.

Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.

Example 1:

Input: n = 10
Output: 16
Explanation: The winning strategy is as follows:
- The range is [1,10]. Guess 7.
    - If this is my number, your total is $0. Otherwise, you pay $7.
    - If my number is higher, the range is [8,10]. Guess 9.
        - If this is my number, your total is $7. Otherwise, you pay $9.
        - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
        - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
    - If my number is lower, the range is [1,6]. Guess 3.
        - If this is my number, your total is $7. Otherwise, you pay $3.
        - If my number is higher, the range is [4,6]. Guess 5.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
            - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
            - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
        - If my number is lower, the range is [1,2]. Guess 1.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
            - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.

Example 2:

Input: n = 1
Output: 0
Explanation: There is only one possible number, so you can guess 1 and not have to pay anything.

Example 3:

Input: n = 2
Output: 1
Explanation: There are two possible numbers, 1 and 2.
- Guess 1.
    - If this is my number, your total is $0. Otherwise, you pay $1.
    - If my number is higher, it must be 2. Guess 2. Your total is $1.
The worst case is that you pay $1.
"""

# Simple fun solution

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        res = [0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 21, 24, 27, 30, 34, 38, 42, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 86, 90, 94, 98, 102, 106, 110, 114, 119, 124, 129, 134, 139, 144, 149, 154, 160, 166, 172, 178, 182, 186, 190, 194, 198, 202, 206, 210, 214, 218, 222, 226, 230, 234, 238, 242, 246, 250, 254, 258, 262, 266, 270, 274, 278, 282, 286, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 376, 382, 388, 394, 400, 406, 412, 418, 424, 430, 436, 442, 448, 454, 460, 466, 473, 480, 487, 494, 501, 508, 515, 522, 529, 536, 543, 550, 555, 560, 565, 570, 575, 580, 585, 590, 595, 600, 605, 610, 615, 620, 625, 630, 635, 640, 645, 650, 655, 660, 666, 674, 680, 686, 692, 698, 703, 708, 713, 718, 723, 728, 733, 738, 743, 748, 753, 758, 763, 768, 773, 778, 783, 788, 793, 798, 803, 808, 813, 818, 823, 828, 833, 838, 843, 848, 853, 858, 863, 868, 873, 878, 883, 888, 893, 898, 904, 910, 916, 922, 928, 934, 940, 946, 952]
        return res[n-1]

# Alternate

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def rec(a, b):
            if b < 5:
                return [0, 0, 1, 2, 4][b]
            elif b == a+2:
                return a+1
            else:
                return min(i + max(rec(a,i-1),rec(i+1,b)) for i in range(b-3, a, -4))
        return rec(1, n)
