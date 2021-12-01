/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
	return bfs(root)
}

func bfs(root *TreeNode) [][]int {
	res := [][]int{}

	if root == nil {
		return res
	}

	curLevelNodes := []*TreeNode{root}

	// odd level .. left to right
	// even level .. right to left
	level := 1
	for len(curLevelNodes) > 0 {
		levelNodesVal := []int{}
		nextLevelNodes := []*TreeNode{}

		for i := 0; i < len(curLevelNodes); i++ {
			idx := i
			if level%2 == 0 {
				idx = len(curLevelNodes) - 1 - i
			}

			levelNodesVal = append(levelNodesVal, curLevelNodes[idx].Val)

			if curLevelNodes[i].Left != nil {
				nextLevelNodes = append(nextLevelNodes, curLevelNodes[i].Left)
			}
			if curLevelNodes[i].Right != nil {
				nextLevelNodes = append(nextLevelNodes, curLevelNodes[i].Right)
			}
		}

		curLevelNodes = nextLevelNodes
		res = append(res, levelNodesVal)
		level++
	}

	return res
}
