ans = 0
for a in range(100,999):
    for b in range(100,999):
        c = a * b
        if len(str(c)) > 5:
            if str(c)[0] + str(c)[1] + str(c)[2] == str(c)[-1] + str(c)[-2] + str(c)[-3]:
                if c > ans:
                    ans = c
                    print(ans)
            