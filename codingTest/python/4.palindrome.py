class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Input: s = "Was it a car or a cat I saw?"

        checkValue = s.lower()
        checkValue = checkValue.replace(' ', '')
        checkValue = checkValue.replace('?', '')

        if checkValue == checkValue[::-1]:
            return True


solution = Solution()

print(solution.isPalindrome("Was it a car or a cat I saw?"))

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # 문자열을 소문자로 변환
#         checkValue = s.lower()
#         # 알파벳과 숫자만 남기고 나머지 문자 제거
#         checkValue = ''.join(char for char in checkValue if char.isalnum())

#         # 변환된 문자열이 회문인지 확인
#         is_palindrome = checkValue == checkValue[::-1]

#         # 중간 결과를 출력
#         print(f"value: {checkValue}")

#         return is_palindrome

# # 예제 문자열
# input_string = "Was it a car or a cat I saw?"
# # 솔루션 객체 생성 및 회문 여부 판별
# solution = Solution()
# result = solution.isPalindrome(input_string)
# print(result)  # True 출력
