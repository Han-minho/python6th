total_list = []

# 질문 입력
while True:
    qusetion = input("질문을 입력해주세요 : ")
    if(qusetion == "q"):
        break
    else:
        # 질문 리스트에 입력
        total_list.append({"질문":qusetion,"답변":""})

# 답변 입력
for i in total_list:
    print(i["질문"])
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer

print(total_list)