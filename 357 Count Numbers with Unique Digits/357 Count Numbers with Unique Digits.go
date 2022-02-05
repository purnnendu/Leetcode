func countNumbersWithUniqueDigits(n int) int {
    if n == 0 {
        // Base case
        // only 0 for [0, 1) interval
        return 1

    }else if n == 1 {

        // Base case
        // Only 0 ~ 9 for [0, 10) interval
        return 10

    }else{

        // General case
        // cur count = current count of unique digits contributed from [ 10^(n-1), 10^n ) interval
        // countNumbersWithUniqueDigits(n-1) = count of unique digits contributed from [0, 10^(n-1) ) interval
        // countNumbersWithUniqueDigits(n-1) + cur count = count of unique digits from [0, 10^n ) interval

        cur_count := 9

        for i := 1 ; i < n ; i++{
            cur_count = cur_count * (10 - i)
        }

        return countNumbersWithUniqueDigits(n-1) + cur_count

    }
}
