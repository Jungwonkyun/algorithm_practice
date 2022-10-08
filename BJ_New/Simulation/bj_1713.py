frame = int(input())
good = int(input())
student = []
st_dict = dict()

s_list = list(map(int, input().split()))

for item in s_list:
    student.append(item)

picture = []
reference = []


for i in range(good):

    next_student = student[i]

    # 사진틀에 학생이 있으면
    if next_student in picture:
        for j in range(len(picture)):
            if next_student == picture[j]:
                reference[j] += 1

    # 사진틀에 학생이 없으면
    else:
        # 틀이 꽉차있으면
        if len(picture) >= frame:
            for j in range(frame):
                if reference[j] == min(reference):
                    del picture[j]
                    del reference[j]
                    break

        # 틀이 안 차있으면
        picture.append(next_student)
        reference.append(1)

picture.sort()
print(' '.join(map(str, picture)))
