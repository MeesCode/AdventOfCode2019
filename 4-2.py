low = 236491
high = 713787

# low = 0
# high = 1000

counter = 0
for i in range(low, high+1):
    # check for decreasing digits
    pw = str(i)

    max_num = 0
    double_count = 1
    prev_num = None
    decreasing = False
    double_group = False

    # print(pw)

    for c in pw:
        num = int(c)
        max_num = max(max_num, num)

        # decreasing number
        if num < max_num:
            decreasing = True

        # count doubles
        if prev_num and prev_num == num:
            double_count += 1
        else:
            if double_count == 2:
                double_group = True
            double_count = 1

        prev_num = num

    if double_group and not decreasing:
        counter += 1
    else:
        if(pw[-2:][0] == pw[-2:][1] and not pw[-3:][0] == pw[-2:][1] and not decreasing):
            counter += 1
    # else:
    #     print("not good")

print(counter)
