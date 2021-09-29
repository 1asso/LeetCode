class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5, count10 = 0, 0
        for i in range(len(bills)):
            if bills[i] == 5:
                count5 += 1
            elif bills[i] == 10:
                count5 -= 1
                count10 += 1
            else:
                if count10:
                    count10 -= 1
                    count5 += 2
                count5 -= 3
            if count5 < 0 or count10 < 0:
                return False
        return True