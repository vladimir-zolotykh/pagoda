import time
from django.shortcuts import render, redirect

PEGS = ["A", "B", "C"]
MIN_DISKS = 3
MAX_DISKS = 8


def hanoi_moves(n, src, aux, dst):
    if n == 0:
        return
    yield from hanoi_moves(n - 1, src, dst, aux)
    yield (src, dst)
    yield from hanoi_moves(n - 1, aux, src, dst)


def init_game(request, n, delay):
    request.session["n"] = n
    request.session["delay"] = delay
    request.session["pegs"] = {
        "A": list(range(n, 0, -1)),
        "B": [],
        "C": [],
    }
    request.session["moves"] = list(hanoi_moves(n, "A", "B", "C"))
    request.session["step"] = 0


def start(request):
    if request.method == "POST":
        n = int(request.POST.get("n", 3))
        delay = int(request.POST.get("delay", 500))

        if n < MIN_DISKS or n > MAX_DISKS:
            n = 3

        init_game(request, n, delay)
        return redirect("game")

    return render(request, "hanoi/start.html")


def game(request):
    if "pegs" not in request.session:
        return redirect("start")

    pegs = request.session["pegs"]
    moves = request.session["moves"]
    step = request.session["step"]
    delay = request.session["delay"]

    message = ""

    if step < len(moves):
        src, dst = moves[step]

        disk = pegs[src].pop()
        pegs[dst].append(disk)

        request.session["step"] = step + 1
        request.session["pegs"] = pegs

        # server-side delay (milliseconds)
        time.sleep(delay / 1000.0)
    else:
        message = "Solved."

    won = len(pegs["C"]) == request.session["n"]

    return render(
        request,
        "hanoi/game.html",
        {
            "pegs": pegs,
            "message": message,
            "won": won,
            "delay": delay,
            "running": step < len(moves),
        },
    )


def reset_game(request):
    request.session.flush()
    return redirect("start")
