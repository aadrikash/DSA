class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        left = 0 
        right = 0
        my_dict = {}
        max_len = 0

        while right < n:
            my_dict[fruits[right]] = my_dict.get(fruits[right],0)+1

            if len(my_dict)> 2:
                my_dict[fruits[left]]  -= 1
                if my_dict[fruits[left ]]  == 0:
                    del my_dict[fruits[left]]
                left += 1
            if len(my_dict) <= 2:
                max_len = max(max_len, right - left + 1)
            right += 1
        return max_len


'''
        n = len(fruits)
        ans = 0

        for i in range(n):
            basket = {}
            count = 0

            for j in range(i, n):

                basket[fruits[j]] = basket.get(fruits[j], 0) + 1

                if len(basket) > 2:
                    break

                count += 1
                ans = max(ans, count)

        return ans
'''