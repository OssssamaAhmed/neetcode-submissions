class Solution:
    def threeSum(self, sorted_num: List[int]) -> List[List[int]]:
        sorted_num.sort()
        result = []
        for i in range(len(sorted_num)):
            if i > 0 and sorted_num[i] == sorted_num[i - 1]:
                continue
            j = i + 1
            k = len(sorted_num) - 1      
            while j < k:
                if sorted_num[i] + sorted_num[j] + sorted_num[k] > 0:
                    k -=1
                elif sorted_num[i] + sorted_num[j] + sorted_num[k] < 0:
                    j+=1
                elif sorted_num[i] + sorted_num[j] + sorted_num[k] == 0:
                    result.append([sorted_num[i], sorted_num[j], sorted_num[k]])
                    j+=1
                    while j < k and sorted_num[j] == sorted_num[j - 1]:
                        j+=1
        return result
                

            

