import "math"
import "fmt"
import "strconv"

func minPartitions(n string) int {
    max_val := 0.0
    for _, c := range n {
        digit, _ := strconv.Atoi(string(c))
        max_val = math.Max(max_val, float64(digit))
    }
    return int(max_val)
}
