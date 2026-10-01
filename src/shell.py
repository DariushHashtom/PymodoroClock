import timer
from sys import stdout


logo: str = """
    \033[31m_\033[32m\\|/\033[31m_
   /88888\\
   8888888
   \\88888/\033[0m
   """

keys_help: dict[str, str] = {
    "q": "Quit"       ,
    "t": "Tomato      (Default: 25min)",
    "s": "Short Break (Default: 5 min)",
    "l": "Long Break  (Default: 15min)",
}

times: dict[str, float] = {
    "tomato"     : 25.0,
    "short_break": 5.0 ,
    "long_break" : 15.0,
}

tomato_style: int = 0
running: bool = True

def shell() -> None:
    global tomato_style, keys_help, logo, running

    while running:
        print("\033[2J\033[H", end="") # Clear Screen
        print(logo)
        for i in keys_help.keys():
            print(f" {i} - {keys_help[i]}")
        
        input_: str = input("Tomatooooo)> ")

        if   ( input_ == "q" ): running=False
        elif ( input_ == "t" ): timer.cycle(times["tomato"     ], tomato_style)
        elif ( input_ == "s" ): timer.cycle(times["short_break"], tomato_style)
        elif ( input_ == "l" ): timer.cycle(times["long_break" ], tomato_style)

        stdout.flush()

def main() -> None:
    shell()

if __name__ == "__main__":
    main()
