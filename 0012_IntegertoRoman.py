class Solution:
    def intToRoman(self, num: int) -> str:
        val_to_roman = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        benchmark_vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ''

        for i in benchmark_vals:
            while num >= i:
                num -= i
                res += val_to_roman[i]
        
        return res
