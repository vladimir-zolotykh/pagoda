from django.shortcuts import render, redirect

DEFAULT_DISKS = 3
PEGS = ["A", "B", "C"]


def init_game(request, n=DEFAULT_DISKS):
    request.session["pegs"] = {
        "A": list(range(n, 0, -1)),
        "B": [],
        "C": [],
    }
    request.session["selected"] = None


def game(request):
    if "pegs" not in request.session:
        init_game(request)

    pegs = request.session["pegs"]
    selected = request.session.get("selected")

    message = ""

    if request.method == "POST":
        peg = request.POST.get("peg")

        if selected is None:
            # Select a disk
            if pegs[peg]:
                request.session["selected"] = peg
        else:
            # Try to move
            src = selected
            dst = peg

            if src != dst and pegs[src]:
                disk = pegs[src][-1]
                if not pegs[dst] or pegs[dst][-1] > disk:
                    pegs[src].pop()
                    pegs[dst].append(disk)
                else:
                    message = "Illegal move"

            request.session["selected"] = None
            request.session["pegs"] = pegs

    won = (
        pegs["C"] == sorted(pegs["C"], reverse=True) and len(pegs["C"]) == DEFAULT_DISKS
    )

    return render(
        request,
        "hanoi/game.html",
        {
            "pegs": pegs,
            "selected": selected,
            "message": message,
            "won": won,
        },
    )


def reset_game(request):
    init_game(request)
    return redirect("game")
