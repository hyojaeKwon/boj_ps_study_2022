import sys
import collections

Input = sys.stdin.readline

times = int(Input())

for _ in range(times):
    number_convenient = int(Input())

    origin_x, origin_y = map(int, Input().split())
    convenient = []*number_convenient

    for i in range(number_convenient):
        x,y = map(int, Input().split())
        convenient.append([x,y])

    festival_x, festival_y = map(int,Input().split())

    #모든 좌표의 기준을 50으로 설정
    festival_x = festival_x // 50
    festival_y = festival_y // 50


    table= [[[0]*festival_y for _ in range(festival_x)] for i in range(2)]
    print(len(table))
    #
    for i in range(number_convenient):
        #편의점 위치는 -2로 저장
        conveni_x = convenient[i][0] // 50 -1
        conveni_y = convenient[i][1] // 50 -1
        # print(conveni_y,conveni_x)
        table[conveni_y][conveni_x][0] = -1
        # print(convenient[i][0],convenient[i][1])
    #initial value 20으로 지정
    table[0][0][1] = 20

    #
    # BFS 시작 부분
    dx = [1,0]
    dy = [0,1]

    # queue = collections.deque
    queue = []
    queue.append([0,0])
    while queue:
        x,y = queue.pop(0)

        for j in range(2):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < festival_x and 0 <= ny < festival_y:
                beer = table[y][x][1] - 1
                # print(beer,x,y)

                if beer >= 0 and table[ny][nx][0] == -1:
                    table[ny][nx][1] = 20
                    queue.append([nx,ny])
                    continue

                if beer >= 0:
                    table[ny][nx][1] = beer
                    queue.append([nx,ny])





    # if (table[festival_y-1][festival_x-1] >= 0):
    #     print('happy')
    # else:
    #     print('sad')


    print(table)


    # 맥주 한 병으로 50m를 갈 수 있고, 20병이 있으므로 한번에 갈 수 있는 거리는 1000m 이다.
    # 즉, 편의점과 목적지의 좌표를 입력한 다음에 현재 자신과 거리가 1000m떨어져 있는지 확인한다.
    # 계속 이동하면서 목적지에 도착할 수 있는지 확인한다. => 한번 이동한 편의점은 다시 들를 수 없다는 것을 간과해선 안된다.
    #if 목적지 도달 => print happy else print sad


