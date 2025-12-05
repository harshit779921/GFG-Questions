class Solution:
    def minDist(self, arr, x, y):
        last_x = -1
        last_y = -1
        min_dist = float('inf')

        for i in range(len(arr)):
            if arr[i] == x:
                last_x = i

            if arr[i] == y:
                last_y = i

            if last_x != -1 and last_y != -1:
                min_dist = min(min_dist, abs(last_x - last_y))

        return min_dist if min_dist != float('inf') else -1
