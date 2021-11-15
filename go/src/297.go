/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

var NULL_STR string = "null"
var NULL_VAL int = -1001

type Codec struct {
}

func Constructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	if root == nil {
		return "[]"
	}

	elements := []string{}
	queue := []*TreeNode{}
	queue = append(queue, root)

	for len(queue) > 0 {
		node := queue[0]
		if node.Val == NULL_VAL {
			elements = append(elements, NULL_STR)
			queue = queue[1:]
			continue
		}

		if node.Left != nil {
			queue = append(queue, node.Left)
		} else {
			queue = append(queue, &TreeNode{
				Val: NULL_VAL,
			})
		}

		if node.Right != nil {
			queue = append(queue, node.Right)
		} else {
			queue = append(queue, &TreeNode{
				Val: NULL_VAL,
			})
		}

		elements = append(elements, strconv.Itoa(node.Val))
		queue = queue[1:]
	}

	return "[" + strings.Join(elements, ",") + "]"
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	// fmt.Println(data)
	data = data[1 : len(data)-1] // remove the "[]"
	elements := strings.Split(data, ",")

	// fmt.Println(len(elements))
	if len(elements) < 3 {
		return nil
	}

	rootVal, _ := strconv.Atoi(elements[0])
	root := &TreeNode{
		Val: rootVal,
	}
	queue := []*TreeNode{}
	queue = append(queue, root)

	i := 1
	for ; i < len(elements); i = i + 2 {
		parent := queue[0]
		queue = queue[1:]

		left := elements[i]
		right := elements[i+1]

		if left != NULL_STR {
			leftVal, _ := strconv.Atoi(left)
			leftNode := &TreeNode{
				Val: leftVal,
			}
			parent.Left = leftNode
			queue = append(queue, leftNode)
		}

		if right != NULL_STR {
			rightVal, _ := strconv.Atoi(right)
			rightNode := &TreeNode{
				Val: rightVal,
			}
			parent.Right = rightNode
			queue = append(queue, rightNode)
		}
	}

	return root
}

/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor();
 * deser := Constructor();
 * data := ser.serialize(root);
 * ans := deser.deserialize(data);
 */