#!/usr/bin/env python3
# Kaushik Das
def fib(n):
	if n==0:
		return 0
	a = 0
	b = 1
	for i in range(1, n):
		c = a + b
		a = b
		b = c

	return a+b

def main():

	print(f"fib(0) : {fib(0)}")
	print(f"fib(1) : {fib(1)}")
	print(f"fib(2) : {fib(2)}")
	print(f"fib(3) : {fib(3)}")
	print(f"fib(4) : {fib(4)}")

if __name__ == "__main__":
  main()