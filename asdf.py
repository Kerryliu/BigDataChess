import chess
asdf = []
with open('output.txt') as f:
    content = f.readlines()
    for line in content:
        if len(line) > 6:
            word = line.split()
            for i in range(0, len(word) - 1):
                try:
                    temp = asdf[i]
                    if word[i] in temp:
                        if word[i+1] in temp[word[i]]:
                            temp[word[i]][word[i+1]] += 1
                        else:
                            temp[word[i]][word[i+1]] = 1
                        asdf[i] = temp
                    else:
                        temp[word[i]] = {word[i+1]: 1}
                        asdf[i] = temp
                except IndexError:
                    asdf.append({word[i] : {word[i+1]: 1}}) #next word, next word count

#print(asdf)
board = chess.Board()
print(board)
while True:
    humanInput = input("Enter move: ")
    try:
        board.push_san(humanInput)
        break;
    except ValueError:
        print("...")
print(board)
print()
for j in range(0, len(asdf) - 1,2):
    nextMoves = asdf[j]
    try:
        possibleMoves = nextMoves[humanInput]
    except KeyError:
        print("fuck.")
        break;
    potato = sorted(possibleMoves, key=possibleMoves.get,reverse=True)
    for meh in potato:
        try:
            board.push_san(meh)
            break;
        except:
            print("...")
    print(board)
    print()
    if board.is_checkmate():
        print("AI wins~")
    while True:
        humanInput = input("Enter move: ")
        try:
            board.push_san(humanInput)
            break;
        except ValueError:
            print("...")
    print(board)
    print()
    if board.is_checkmate():
        print("Human wins~")
