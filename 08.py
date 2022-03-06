
#I completed today's pydle in 1 tries, my time was 00:25:00, here is my solution:

def coding_problem_08(s, k, show_string = False):
	#"""
	#Given an integer k and a string s, find the length of the longest substring that contains at most k distinct
	#characters.
	#Example:

	#>>> coding_problem_08('abcba', 2)  # longest substring with at most 2 distinct characters is 'bcb'
	#3
	#>>> coding_problem_08('edabccccdccba', 3)  # 'bccccdccb'
	#9
	#"""
    def check_sub(begin, end):
        if end >= len(s):
            return False
        used = set()
        repeats = 0
        for i in s[begin:end]:
            if i not in used:
                used.add(i)
                repeats += 1
                if repeats > k:
                    return False
        return True

    if show_string:
        start, end = 0, 0
    current_start, current_end, current_length, length = 0, 0, 0, 0
    current_substring = s[current_start:current_end]
    while current_start < len(s):
        if check_sub(current_start, current_end +1):
            current_end += 1
            current_length = current_end - current_start
            if current_length > length:
                length = current_length
                start = current_start
                end = current_end
        else:
            current_start += 1
    if show_string:
        print(s[start:end])
    return length
    
print(coding_problem_08('edabccccdccba', 3, True))