from time import sleep
from sys  import stdout
import os
import asyncio


if (os.name == "nt"): ...
else                :
    from   sys     import stdin
    from   select  import select
    from   termios import tcgetattr, tcsetattr, TCSADRAIN
    import tty

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
elapsed_seconds: int =0

async def wait() -> None:
    global isnt_stopped, elapsed_seconds
    await asyncio.sleep(1)
    elapsed_seconds+=(1*isnt_stopped)

def cycle(minutes: int=0, tomato_style: int=0) -> None:
    global isnt_stopped, elapsed_seconds

    if   (os.name == "nt"): ...
    else:
        stdin_fd = stdin.fileno()
        old_terminal_settings = tcgetattr(stdin_fd)

        tty.setcbreak(stdin_fd)

        try:
            total_seconds  : int = minutes*60
            elapsed_seconds      = 0
            style          : int = 0
            progress       : int = 0

            while True:
                ready = select([stdin], [], [], 0)[0]
                if (ready):
                    input_: str = stdin.read(1)

                    if   (input_ == "s"                 ): isnt_stopped=0
                    elif (input_ == "r"                 ): isnt_stopped=1
                    elif (input_ == " "                 ): isnt_stopped=not isnt_stopped
                    elif (input_ == "q" or input_ == "e"): break

                if total_seconds<=elapsed_seconds: break

                progress = elapsed_seconds/total_seconds
                style = int(progress * len(tomatoes[tomato_style]))

                print("\033[2J\033[H", end="") # Clear Screen
                if   (isnt_stopped==0): print(tomato_stopped)
                else                  : print(tomatoes[tomato_style][style])
                print(f"       Time: {(elapsed_seconds/60):.1f} Minutes")

                stdout.flush()

                asyncio.run(wait())

            print("\033[2J\033[H", end="") # Clear Screen
            print(tomato_end)
            print("       Finished!")
        finally:
            tcsetattr(stdin_fd, TCSADRAIN, old_terminal_settings)

