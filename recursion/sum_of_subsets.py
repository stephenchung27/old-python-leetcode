def sum_of_subsets(numbers, target):
    def backtrack(index, result, current_sum, total_sum):
        if current_sum > target or total_sum < target: return
        if current_sum == target: results.append(result)

        result[index] = 1
        backtrack(index + 1, result.copy(), current_sum + numbers[index], total_sum - numbers[index])

        result[index] = 0
        backtrack(index + 1, result.copy(), current_sum,
                  total_sum - numbers[index])
    
    result = [0] * len(numbers)
    results = []

    backtrack(0, result, 0, sum(numbers))

    return results

print(sum_of_subsets([5, 10, 12, 13, 15, 18], 30))