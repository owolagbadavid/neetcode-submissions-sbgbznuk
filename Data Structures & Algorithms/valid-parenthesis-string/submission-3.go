func checkValidString(s string) bool {
    stack1 := make([]int, 0)
    stack2 := make([]int, 0)

	for i, c := range s {
		if string(c) == "(" {
			stack1 = append(stack1, i)
		} else if string(c) == "*" {
			stack2 = append(stack2, i)
		} else {
			if len(stack1) > 0 {
				stack1 = stack1[:len(stack1)-1]
			} else if len(stack2) > 0 {
				stack2 = stack2[:len(stack2)-1]
			} else {
				return false
			}
		}
	}

	if len(stack1) == 0 {
		return true
	} else if len(stack2) == 0 {
		return false
	}

	i1 := 0
	i2 := 0
	for i1<len(stack1) && i2<len(stack2) {
		if stack2[i2] > stack1[i1]{
			i1 += 1
			i2 += 1
		} else {
			i2 += 1
		}
	}

	return len(stack1[i1:]) == 0
}
