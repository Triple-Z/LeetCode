func exist(board [][]byte, word string) bool {
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			if findWord(board, word, 0, i, j) {
				return true
			}
		}
	}

	return false
}

func findWord(board [][]byte, word string, wordIdx, i, j int) bool {
	if i >= len(board) || i < 0 || j >= len(board[0]) || j < 0 {
		return false
	}

	if word[wordIdx] != board[i][j] {
		return false
	}

	board[i][j] = byte('/')

	if wordIdx == len(word)-1 {
		return true
	}

	if findWord(board, word, wordIdx+1, i+1, j) ||
		findWord(board, word, wordIdx+1, i-1, j) ||
		findWord(board, word, wordIdx+1, i, j+1) ||
		findWord(board, word, wordIdx+1, i, j-1) {
		return true
	}

	// backtrack
	board[i][j] = word[wordIdx]
	return false
}

