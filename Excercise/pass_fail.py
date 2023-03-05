# Task: Determine whether Zaid passes the exam or not.

t=int(input( "Enter value for range: "))
for i in range(t):
    A, B, C = map(int, input().split()) # Multiple inputs
    total_score = A + B + C
    minimum_score = min(A,B,C)
    #Equality not checked for
    if total_score>=100 and minimum_score>=10: 
        #Yeah - we all make these mistakes. Printed 'Yes' instead of 'Pass' as expected
        print('PASS')           
    else:
        print('FAIL') 