class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        pack = list(map(str, digits))

        tmpRes = ''.join(pack)
        tmpRes = int(tmpRes)

        tmpRes +=1

        return ([int(i) for i in str(tmpRes)])