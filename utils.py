def get_user_input(prompt, default):
    value = input(f"{prompt} (default: {default}) [Press Enter to skip]: ").strip()
    return value if value else default