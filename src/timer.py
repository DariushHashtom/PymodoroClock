from time import sleep
from sys  import stdout
import os
import threading


if (os.name == "nt"): ...
else                :
    from sys import stdin
    import termios, tty

# Tomatoes:
#  _\|/_
# /     \
# |     |
# \_____/
#
#  \|/
# /   \
# \___/
#
#  _\|/_
# /88888\
# 8888888
# \88888/
#
#  \|/
# /888\
# \888/
tomatoes: list[list[str]] = [
    # Tomato Style 1:
    #   \|/
    #  /   \
    #  \___/
    #
    #   \|/
    #  /   \
    #  \88_/
    #
    #   \|/
    #  /8  \
    #  \888/
    #
    #   \|/
    #  /888\
    #  \888/
    #
    #  _\|/_
    # /     \
    # |     |
    # \_____/
    #
    #  _\|/_
    # /     \
    # |     |
    # \88888/
    #
    #  _\|/_
    # /     \
    # 8888888
    # \88888/
    #
    #  _\|/_
    # /88888\
    # 8888888
    # \88888/
    #
    #  _\|/_
    # /   / \
    # | \/  |
    # \_____/
    [
            """\n
         \033[32m\\|/\033[31m
        /   \\
        \\___/\033[0m
            """,
            """\n
         \033[32m\\|/\033[31m
        /   \\
        \\88_/\033[0m
            """,
            """\n
         \033[32m\\|/\033[31m
        /8  \\
        \\888/\033[0m
            """,
            """\n
         \033[32m\\|/\033[31m
        /888\\
        \\888/\033[0m
            """,

            """
        \033[31m_\033[32m\\|/\033[31m_
       /     \\
       |     |
       \\_____/\033[0m
            """,
            """
        \033[31m_\033[32m\\|/\033[31m_
       /     \\
       |     |
       \\88888/\033[0m
            """,
            """
        \033[31m_\033[32m\\|/\033[31m_
       /     \\
       8888888
       \\88888/\033[0m
            """,
            """
        \033[31m_\033[32m\\|/\033[31m_
       /88888\\
       8888888
       \\88888/\033[0m
            """
    ],

    # Tomato Style 2:
    # 
    #   \|/
    #  /888\
    #  \888/
    #
    #  _\|/_
    # /88888\
    # 8888888
    # \88888/
    #
    #  _\|/_
    # /   / \
    # | \/  |
    # \_____/
    [
            """\n
         \033[32m\\|/\033[31m
        /888\\
        \\888/\033[0m
            """,
            """
        \033[31m_\033[32m\\|/\033[31m_
       /88888\\
       8888888
       \\88888/\033[0m
            """
    ]
]

tomato_end: str = """
        \033[32m_\\|/
       /   / \\
       | \\/  |
       \\_____/\033[0m
            """

tomato_stopped: str = """
        \033[33m_\\|/_
       /     \\
       | | | |
       \\_____/\033[0m
            """

isnt_stopped: int = 1
running: bool = True

def get_input() -> str:
    global isnt_stopped, running

    try:
        if (os.name == "nt"): ...
        else:
            stdin_fd = stdin.fileno()
            stdin_old_terminal_settings = termios.tcgetattr(stdin_fd)
            tty.setcbreak(stdin_fd)

        if (running == True):
            if   (os.name == "nt"): ...
            else                  : input_: str = stdin.read(1)
                
            if   (input_ == "s"                 ): isnt_stopped=0
            elif (input_ == "r"                 ): isnt_stopped=1
            elif (input_ == " "                 ): isnt_stopped=not isnt_stopped
            elif (input_ == "q" or input_ == "e"): running=False
    finally:
        if (os.name != "nt"): termios.tcsetattr(stdin_fd, termios.TCSADRAIN, stdin_old_terminal_settings)

def cycle(minutes: int=0, tomato_style: int=0) -> None:
    global isnt_stopped, running

    running = True
    total_seconds  : int = minutes*60
    elapsed_seconds: int = 0
    style          : int = 0
    progress       : int = 0

    while running:
        threading.Thread(target=get_input, daemon=True).start()
        if total_seconds<=elapsed_seconds: break

        progress = elapsed_seconds/total_seconds
        style = int(progress * len(tomatoes[tomato_style]))

        print("\033[2J\033[H", end="") # Clear Screen
        if   (isnt_stopped==0): print(tomato_stopped)
        else                  : print(tomatoes[tomato_style][style])
        print(f"       Time: {(elapsed_seconds/60):.1f} Minutes")

        stdout.flush()
        sleep(1)
        elapsed_seconds+=(1*isnt_stopped)

    print("\033[2J\033[H", end="") # Clear Screen
    print(tomato_end)
    print("       Finished!")

