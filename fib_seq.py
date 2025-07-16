
fib_seq = [0,1]

term_amount = 1

n1 = 0
n2 = 1

if term_amount <=0:
    print("Please enter a valid number for term_amount : ")
elif term_amount == 1:
    print(n1)
else:
    print("Fib Seq : ")

    count = 0
    while count < term_amount:
        print(n1)
        fib_sum = n1 + n2
        # Update Values
        n1 = n2
        n2 = fib_sum
        count += 1

























