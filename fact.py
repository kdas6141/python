#!/usr/bin/env python3
# Kaushik Das
def fact(n):
	if n==0:
		return 1
	return n * fact(n-1)


def main():

	print(f"fact(0) : {fact(0)}")
	print(f"fact(1) : {fact(1)}")
	print(f"fact(2) : {fact(2)}")
	print(f"fact(3) : {fact(3)}")
	print(f"fact(4) : {fact(4)}")
	print(f"fact(5) : {fact(5)}")

if __name__ == "__main__":
  main()
