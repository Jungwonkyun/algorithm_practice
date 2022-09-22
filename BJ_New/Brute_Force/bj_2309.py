dwarf_list = []
height_total = 0 
check = False

no_dwf1 = 0
no_dwf2 = 0
 
#난쟁이 키 업데이트
for i in range(9): 
    dwarf_list.append(int(input()))

#전체 키에서 100을 뺀 값 만큼 난쟁이 키가 빠져아함
height_total = sum(dwarf_list)
difference = height_total - 100 

#합이 키차이가 나오면 break하고 키 기억
for i in range(8):
    for j in range(i+1,9):
        if dwarf_list[i]+dwarf_list[j] == difference:
            no_dwf1 = dwarf_list[i]
            no_dwf2 = dwarf_list[j]
            check = True
            break
    
    if check == True:
        break

#가짜 난쟁이 색출
dwarf_list.remove(no_dwf1)
dwarf_list.remove(no_dwf2)

dwarf_list.sort() 

for i in range(7):
    print(dwarf_list[i])



