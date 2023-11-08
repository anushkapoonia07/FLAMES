player1 = input("Player 1 name : ")
player1 = player1.lower()
player1.replace(" ", "")
player1_list = list(player1)

player2 = input("Player 2 name : ")
player2 = player2.lower()
player2.replace(" ", "")
player2_list = list(player2)

Next = True

while Next:
    for i in range(len(player1_list)):
        for j in range(len(player2_list)):
            if player1_list[i] == player2_list[j]:
                a = player1_list[i]
                player1_list.remove(a)
                player2_list.remove(a)
                l3 = player1_list + ["*"] + player2_list
                Next = True
                break
        else:
            continue
        break
    else:
        l3 = player1_list + ["*"] + player2_list
        Next = False

star_index = l3.index("*")
p1_list = l3[: star_index]
p2_list = l3[star_index + 1:]

count = len(player1_list) + len(player2_list)
output = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

while len(output) > 1:
    split_indx = (count % len(output) - 1)
    if split_indx >= 0:
        right = output[split_indx + 1:]
        left = output[: split_indx]
        output = right + left
    else:
        output = output[: len(output) - 1]

print("Relationship status :", output[0])
