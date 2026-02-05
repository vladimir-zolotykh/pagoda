from django.shortcuts import render, redirect


def index(request):
    # Initialize game state if not exists
    if "stacks" not in request.session:
        request.session["stacks"] = [[4, 3, 2, 1], [], []]  # 4 disks
        request.session["selected"] = None  # Index of stack to move FROM
        request.session["moves"] = 0

    stacks = request.session["stacks"]
    selected = request.session["selected"]
    msg = ""

    if request.method == "POST":
        stack_idx = int(request.POST.get("stack_idx"))

        if selected is None:
            # First click: Select source stack
            if stacks[stack_idx]:
                request.session["selected"] = stack_idx
            else:
                msg = "Stack is empty!"
        else:
            # Second click: Move to destination
            src = selected
            dst = stack_idx
            request.session["selected"] = None  # Clear selection

            if src != dst:
                disk_to_move = stacks[src][-1]
                # Validate move (Hanoi rules)
                if not stacks[dst] or stacks[dst][-1] > disk_to_move:
                    stacks[src].pop()
                    stacks[dst].append(disk_to_move)
                    request.session["moves"] += 1
                    request.session.modified = True
                else:
                    msg = "Invalid move: Cannot place larger disk on smaller one."

    return render(
        request,
        "hanoi/index.html",
        {
            "stacks": stacks,
            "selected": request.session.get("selected"),
            "moves": request.session.get("moves"),
            "error": msg,
            "win": len(stacks[2]) == 4,  # Win if all disks are on the last stack
        },
    )


def reset(request):
    request.session.flush()
    return redirect("index")
