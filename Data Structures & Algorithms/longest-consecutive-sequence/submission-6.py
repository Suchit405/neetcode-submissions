class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        srt = list(sorted(set(nums)))
        print(srt)
        cnt_set = []
        count = 0
        if srt == []:
            return 0
        for i in range(1, len(srt)):
            if srt[i] == srt[i - 1] + 1:
                count += 1
            elif srt[i] != srt[i - 1] + 1:
                cnt_set.append(count)
                count = 0
        cnt_set.append(count)
        return sorted(cnt_set)[len(cnt_set) - 1] + 1