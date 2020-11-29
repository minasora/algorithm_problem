s_x, s_y, g_x, g_y = map(int, input().split())
s_y = -s_y
k = (g_y - s_y)/(g_x - s_x)
b = s_y - k * s_x
print(-b/k)