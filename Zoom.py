total_num, every_kth = map(int, input().split(" "))
num_lst = input().split(" ")
final_text = " ".join(num_lst[every_kth - 1::every_kth])
print(final_text)
