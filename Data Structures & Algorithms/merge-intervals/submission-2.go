func merge(intervals [][]int) [][]int {
    res := [][]int{}

	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][0] == intervals[j][0] {
			return intervals[i][1] < intervals[j][1]
		}
		return intervals[i][0] < intervals[j][0]
	})

	last := intervals[0]
	for i := 1; i <= len(intervals); i++ {
		if i < len(intervals) && last[1] >= intervals[i][0] {
			last[1] = max(intervals[i][1], last[1])
		} else {
			res = append(res, last)
			if i < len(intervals) {
				last = intervals[i]
			}
		}
	}

	return res
}
