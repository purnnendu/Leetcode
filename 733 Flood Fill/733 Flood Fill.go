func floodFill(image [][]int, sr int, sc int, newColor int) [][]int {
    oldColor := image[sr][sc]
    if oldColor == newColor {
        return image
    }
    helper(image, sr, sc, oldColor, newColor)
    return image
}

func helper(image [][]int, sr, sc, oldColor, newColor int) {
    if sr < 0 || sr >= len(image) || sc < 0 || sc >= len(image[0]) {
        return
    }
    if image[sr][sc] != oldColor {
        return
    }
    image[sr][sc] = newColor
    helper(image, sr-1, sc, oldColor, newColor)
    helper(image, sr+1, sc, oldColor, newColor)
    helper(image, sr, sc-1, oldColor, newColor)
    helper(image, sr, sc+1, oldColor, newColor)
    return
}
