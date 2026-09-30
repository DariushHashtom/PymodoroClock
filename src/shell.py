import timer


logo: str = """
    \033[31m_\033[32m\\|/\033[31m_
   /88888\\
   8888888
   \\88888/\033[0m
   """

keys_help: dict[str, str] = {
    "q": "Quit"       ,
    "t": "Tomato"     ,
    "s": "Short Break",
    "l": "Long Break" ,
}

times: dict[str, float] = {
    "tomato"     : 25.0,
    "short_break": 5.0 ,
    "long_break" : 15.0,
}

def shell() -> None:
    while True:
        print(logo)
        for i in keys_help.keys():
            print(f" {i} - {keys_help[i]}")
        
        input_: str = input("Tomatooooo> ")

def main() -> None:
    print("Hello, World!")

if __name__ == "__main__":
    main()
