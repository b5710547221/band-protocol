#input value string
value = input().split(" ")
value_pos = input().split(" ")
num_chick = int(value[0])
carry_roof  = int(value[1])
chick_arr = []
result_arr = [0 for result in range(0,num_chick)]
for chick_pos in range(0,num_chick):
    chick_pos = int(value_pos[chick_pos])
    chick_arr.append(chick_pos)
for chick_pos in range(0,num_chick):
    for chick_pos_compare in range(chick_pos,num_chick):
        if chick_arr[chick_pos] + carry_roof > chick_arr[chick_pos_compare]:
            result_arr[chick_pos] =result_arr[chick_pos]+1
#result maximum chick
print(max(result_arr))