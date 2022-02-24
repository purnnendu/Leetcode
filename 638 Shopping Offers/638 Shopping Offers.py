"""
In LeetCode Store, there are n items to sell. Each item has a price. However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given an integer array price where price[i] is the price of the ith item, and an integer array needs where needs[i] is the number of pieces of the ith item you want to buy.

You are also given an array special where special[i] is of size n + 1 where special[i][j] is the number of pieces of the jth item in the ith offer and special[i][n] (i.e., the last integer in the array) is the price of the ith offer.

Return the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers. You are not allowed to buy more items than you want, even if that would lower the overall price. You could use any of the special offers as many times as you want.

Example 1:

Input: price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
Output: 14
Explanation: There are two kinds of items, A and B. Their prices are $2 and $5 respectively.
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B.
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.

Example 2:

Input: price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]
Output: 11
Explanation: The price of A is $2, and $3 for B, $4 for C.
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C.
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C.
You cannot add more items, though only $9 for 2A ,2B and 1C.
"""
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        n = len(special)
        num_items = len(price)

        @functools.cache
        def DFS(i, freq, items): # last special id taken, last special used freq

            min_price = 0
            for item, p, need in zip(items, price, needs):
                min_price += p*(need - item)

            # initialization: price without special offers

            for j in range(i, n):
                new_items = tuple()
                for k in range(num_items):
                    new_item = items[k] + special[j][k]
                    if new_item <= needs[k]:
                        new_items += (new_item,)
                    else:
                        break  # can't get another speical offer
                else:
                    if j == i:
                        offer_price = special[i][-1] + DFS(i, freq+1, new_items)
                    else:
                        offer_price = special[j][-1] + DFS(j, 1, new_items)

                    if offer_price < min_price:
                        min_price = offer_price

            return min_price

        return DFS(0,0,(0,)*num_items)
