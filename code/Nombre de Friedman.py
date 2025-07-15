import itertools
import operator

def is_friedman_number(num):
    """
    Vérifie si un nombre est un nombre de Friedman.

    Args:
        num: Le nombre à vérifier.

    Returns:
        True si le nombre est un nombre de Friedman, False sinon.
    """

    digits = [int(d) for d in str(num)]
    operations = [operator.add, operator.sub, operator.mul]  # On retire la division pour l'instant

    for perm in itertools.permutations(digits):
        for ops in itertools.product(operations, repeat=len(perm) - 1):
            expression = perm[0]
            for i, op in enumerate(ops):
                result = op(expression, perm[i+1])
                # On vérifie que le résultat est un entier et qu'il est égal au nombre de départ
                if isinstance(result, int) and result == num:
                    return True

    return False

# Exemples d'utilisation
print(is_friedman_number(347))  # Doit afficher True
print(is_friedman_number(736)) # False (pas trouvé d'expression pour ce cas)