def solution(triangle):

    answer = top_down(triangle)

    return answer

def bottom_up(triangle):
    floor = len(triangle) - 1 

    while floor > 0:
        for i in range(floor):
            triangle[floor-1][i] += max(triangle[floor][i], triangle[floor][i+1])
        floor -= 1
        
    return triangle[0][0]

def top_down(triangle):
    floor = 1
    
    while floor < len(triangle):
        for i in range(floor + 1):
            if i == 0:
                triangle[floor][i] += triangle[floor-1][0]
            elif i == floor:
                triangle[floor][i] += triangle[floor-1][i-1]
            else:
                triangle[floor][i] += max(triangle[floor-1][i-1], triangle[floor-1][i])
        floor += 1
        
    return max(triangle[len(triangle)-1])