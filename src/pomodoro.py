from time import sleep
from sys  import stdout


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
        \033[31m_\033[32m\\|/\033[31m_
       /   \033[32m/ \033[31m\\
       | \33[32m\\/  \033[31m|
       \\_____/\033[0m
            """



def cycle(minutes: int=0, tomato_style: int=0) -> None:
    total_seconds  : int = minutes*60
    elapsed_seconds: int = 0
    style          : int = 0
    progress       : int = 0

    while True:
        if total_seconds<=elapsed_seconds: break

        progress = elapsed_seconds/total_seconds
        style = int(progress * len(tomatoes[tomato_style]))

        print("\033[2J\033[H", end="") # Clear Screen
        print(tomatoes[tomato_style][style])
        print(f"       Time: {(elapsed_seconds/60):.1f} Minutes")

        stdout.flush()
        sleep(1)
        elapsed_seconds+=1

    print("\033[2J\033[H", end="") # Clear Screen
    print(tomato_end)
    print("       Finished!")

