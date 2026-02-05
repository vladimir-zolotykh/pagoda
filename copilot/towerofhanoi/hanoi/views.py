from django.shortcuts import render, redirect

# Default: 3 disks on peg 0
INITIAL_STATE = [["3", "2", "1"], [], []]


def hanoi_game(request):
    state = request.session.get("state", [peg.copy() for peg in INITIAL_STATE])

    if request.method == "POST":
        src = int(request.POST.get("src"))
        dst = int(request.POST.get("dst"))

        if state[src]:  # source not empty
            disk = state[src][-1]
            if not state[dst] or int(disk) < int(state[dst][-1]):
                state[src].pop()
                state[dst].append(disk)

        request.session["state"] = state
        return redirect("hanoi")

    return render(request, "hanoi.html", {"state": state})


def reset_game(request):
    request.session["state"] = [peg.copy() for peg in INITIAL_STATE]
    return redirect("hanoi")
