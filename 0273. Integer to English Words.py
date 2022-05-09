class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def convert(num):
            if num < 20:
                return to19[num - 1:num]
            if num < 100:
                return[tens[num // 10 - 2]] + convert(num % 10)
            if num < 1000:
                return [to19[num // 100 - 1]] + ['Hundred'] + convert(num % 100)
            if num < 10 ** 6:
                return convert(num // 1000) + ['Thousand'] + convert(num % 1000)
            if num < 10 ** 9:
                return convert(num // 10 ** 6) + ['Million'] + convert(num % 10 ** 6)
            return convert(num // 10 ** 9) + ['Billion'] + convert(num % 10 ** 9)
        return ' '.join(convert(num)) if num else 'Zero'