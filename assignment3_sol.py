def is_pal_no_loop_recur(s):
	if s.upper() != s[::-1].upper():
		return False
	return True

def is_pal_loop(s):
	str_len = len(s)
	upper_alphanum_s = s.upper()
	for i in range(str_len//2):
		if upper_alphanum_s[i] != upper_alphanum_s[str_len-1-i]:
			return False
	return True


def is_pal_recur(s):
	def is_pal(s):
		if len(s) <= 1:
			return True
		else:
			return s[0] == s[-1] and is_pal(s[1:-1])
	return is_pal(s.upper())

print(f"is_pal_no_loop_recur('abccba'): {is_pal_no_loop_recur('abccba')}\n")
print(f"is_pal_no_loop_recur('abccbe'): {is_pal_no_loop_recur('abccbe')}\n")
print(f"is_pal_loop('abccba'): {is_pal_loop('abccba')}\n")
print(f"is_pal_loop('abccbe'): {is_pal_loop('abccbe')}\n")
print(f"is_pal_recur('abccba'): {is_pal_recur('abccba')}\n")
print(f"is_pal_loop('abccbe'): {is_pal_loop('abccbe')}\n")