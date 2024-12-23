three_ps_apples = int(input())
two_ps_apples = int(input())
one_ps_apples = int(input())

three_ps_bananas = int(input())
two_ps_bananas = int(input())
one_ps_bananas = int(input())

apples_score = three_ps_apples * 3 + two_ps_apples * 2 + one_ps_apples * 1
bananas_score = three_ps_bananas * 3 + two_ps_bananas * 2 + one_ps_bananas * 1

if apples_score > bananas_score:
    print('A')
elif apples_score == bananas_score:
    print('T')
elif bananas_score > apples_score:
    print('B')