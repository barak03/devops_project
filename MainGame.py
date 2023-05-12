from Live import load_game, welcome

print(welcome(input("Enter your name: ")))
try:
    load_game()
except KeyboardInterrupt:
    exit()
except Exception as e:
    print(f"Error accord {e}")
