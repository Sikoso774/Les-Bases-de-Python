lait=["vache", "souris", "levure", "bactérie"]
for laitier in lait:
    print(laitier)
for i in range(len(lait)):
    print(f" le lait {i} est composé de {lait[i]}")
for i, laitier in enumerate(lait):
    print(f"Le lait {i} est composé de {laitier}")