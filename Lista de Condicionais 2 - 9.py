#9
def main(args):
	a=int(input("entre um numero:"))
	if (a % 2 == 0):
		print("o numero %d é par" % a)
	else:
		print("o numero %d é ímpar" % a)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
