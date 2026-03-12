"""Point d'entrée de l'exercice d'introduction."""

import sys

from intro import greet


def main(argv: list[str]) -> None:
    """Exécute le script de salutation.

    - Si un nom est fourni, il est utilisé tel quel
    - Sinon, une salutation générique est affichée
    """
    if len(argv) >= 2:
        name = " ".join(argv[1:])
    else:
        name = ""

    print(greet(name))


if __name__ == "__main__":
    main(sys.argv)
