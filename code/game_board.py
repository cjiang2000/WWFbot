class game:
	def __init__(self):
		self.board = [[0,0,0,4,0,0,3,0,3,0,0,4,0,0,0],
				 	  [0,0,1,0,0,2,0,0,0,2,0,0,1,0,0],
					  [0,1,0,0,1,0,0,0,0,0,1,0,0,1,0],
					  [4,0,0,3,0,0,0,2,0,0,0,3,0,0,4],
				 	  [0,0,1,0,0,0,1,0,1,0,0,0,1,0,0],
					  [0,2,0,0,0,3,0,0,0,3,0,0,0,2,0],
					  [3,0,0,0,1,0,0,0,0,0,1,0,0,0,3],
				 	  [0,0,0,2,0,0,0,5,0,0,0,2,0,0,0],
					  [3,0,0,0,1,0,0,0,0,0,1,0,0,0,3],
					  [0,2,0,0,0,3,0,0,0,3,0,0,0,2,0],
					  [0,0,1,0,0,0,1,0,1,0,0,0,1,0,0],
					  [4,0,0,3,0,0,0,2,0,0,0,3,0,0,4],
					  [0,1,0,0,1,0,0,0,0,0,1,0,0,1,0],
					  [0,0,1,0,0,2,0,0,0,2,0,0,1,0,0],
					  [0,0,0,4,0,0,3,0,3,0,0,4,0,0,0]]
		self.first_turn = True
		inFile = open("wordlist.txt", 'r')
		self.wordlist = []
		for line in inFile:
			self.wordlist.append(line)

	def playWord(self, word, startx, starty, endx, endy):
		count = 0
		self.first_turn = False
		if validWord(word, startx, starty, endx, endy):
			for x in range(startx, endx + 1):
				for y in range(starty, endy + 1):
					self.board[x][y] = word[count]
					count = count + 1
			return True
		else:
			print("Invalid Word")
			return False

	def validWord(self, word, startx, starty, endx, endy):
		if word not in wordlist:
			return False
		if word.length != (starty - startx + endy - endx):
			return False
		count = 0
		for x in range(startx, endx + 1):
				for y in range(starty, endy + 1):
					if board[x][y].isalpha() and board[x][y] != word[count]:
						return False
					count = count + 1	
		return True