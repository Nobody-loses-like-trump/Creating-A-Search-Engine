import time

sentences = ["This is good",
             "python is good",
             "python is not python snake"]

# sleep_time = 10 ** -300
sentences_2 = []
len_max = 0
for i in sentences:
    if len(i) > len_max:
        len_max = len(i)
len_max = len(str(len_max))

string = input("Please input your query string: ")
time_start = time.time()
list_2 = string.lower().split(" ")

for i in sentences:
    score = 0
    length = 0
    content = i.lower().split(" ")
    for j in list_2:
        if j in content:
            score += content.count(j)
            length += len(j) * content.count(j)
    if score > 0:
        app = score + length/10**len_max
        sentences_2.append((i, app))

sentences_2.sort(key=lambda x: x[1], reverse=True)
# time.sleep(sleep_time)
# print(f"{len(sentences_2)} results found ({time.time() - time_start - sleep_time} seconds):")
print(f"{len(sentences_2)} results found ({time.time() - time_start} seconds):")
for index, value in enumerate(sentences_2):
    print(f"{index + 1}.\t{value[0]}")
