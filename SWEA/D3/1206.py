for t in range(1, 11):
    num_build = int(input())
    building_list = list(map(int, input().split()))
    result = 0

    for i in range(2, num_build-2):
        # 자신 좌 2 우 2 빌딩 뽑아내기
        check_list = building_list[i-2:i+3]
        # 현재 빌딩은 가운데
        now_building = check_list[2]
        # 양쪽 2칸 비어있어야 하므로 5개중 제일 커야함
        if now_building == max(check_list):
            check_list.pop(2)
            # 제일 큰거 제외하고 두번째로 큰 빌딩 빼주기
            result += now_building-max(check_list)

    print("#{} {}".format(t, result))
