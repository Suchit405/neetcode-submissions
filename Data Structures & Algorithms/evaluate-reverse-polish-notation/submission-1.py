class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # hash_map = {"+" : +, "-" : -, "*" : *, "/" : /}
        arr = []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                a = int(arr.pop())
                b = int(arr.pop())
                if i == "+":
                    arr.append(b + a)
                elif i == "-":
                    arr.append(b - a)
                elif i == "*":
                    arr.append(b * a)
                elif i == "/":
                    arr.append(b / a)
            else:
                arr.append(i)
        return int(arr[0])