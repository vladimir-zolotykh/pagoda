from django.shortcuts import render, redirect


def initialize_game(request):
    request.session["towers"] = {"A": [4, 3, 2, 1], "B": [], "C": []}
    request.session["moves"] = 0


def game(request):
    if "towers" not in request.session:
        initialize_game(request)

    towers = request.session["towers"]
    moves = request.session["moves"]
    message = ""
    win = False

    if request.method == "POST":
        from_tower = request.POST.get("from_tower")
        to_tower = request.POST.get("to_tower")

        if from_tower == to_tower or from_tower not in towers or to_tower not in towers:
            message = "Invalid move."
        elif not towers[from_tower]:
            message = "No disks on source tower."
        else:
            disk = towers[from_tower].pop()  # Top disk (largest num = larger disk)
            if (
                towers[to_tower] and disk > towers[to_tower][-1]
            ):  # Cannot place larger on smaller
                message = "Cannot place larger disk on smaller."
                towers[from_tower].append(disk)  # Undo
            else:
                towers[to_tower].append(disk)
                moves += 1
                request.session["moves"] = moves

        # Check win
        if len(towers["C"]) == 4 and towers["C"] == [4, 3, 2, 1]:
            win = True

        request.session["towers"] = towers

    context = {"towers": towers, "moves": moves, "message": message, "win": win}
    return render(request, "hanoi.html", context)


def reset(request):
    if request.method == "POST":
        initialize_game(request)
    return redirect("game")
