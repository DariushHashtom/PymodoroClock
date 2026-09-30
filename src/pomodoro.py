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
tomatoes: list[str] = [
        """
     \033[31m_\033[32m\|/\033[31m_
    /     \\
    |     |
    \\_____/\033[0m
        """,
        """
     \033[32m\|/\033[31m
    /   \\
    \\___/\033[0m
        """,

        """
     \033[31m_\033[32m\|/\033[31m_
    /88888\\
    8888888
    \\88888/\033[0m
        """,
        """
     \033[32m\|/\033[31m
    /888\\
    \\888/\033[0m
        """
]

def show(left_time: int) -> None:
    #print("\033[2J\033[H", end="") # Clear Screen

    # Print Screen
    print(f"""
    {tomatoes[0]}
    Time Left: {left_time}


    {tomatoes[1]}
    Time Left: {left_time}


    {tomatoes[2]}
    Time Left: {left_time}


    {tomatoes[3]}
    Time Left: {left_time}
    """)

def cycle() -> None:
    show(10)
    stdout.flush()
