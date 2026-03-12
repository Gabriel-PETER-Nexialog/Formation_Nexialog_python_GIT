"""Solution de reference pour le module 00."""


def greet(name: str) -> str:
    cleaned = name.strip()
    if not cleaned:
        return "Bonjour !"
    return f"Bonjour, {cleaned}!"
