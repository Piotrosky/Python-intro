import numpy as np
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.weights import entropy_weights


def main():
    # -------------------------------------------------
    # 1. ZNORMALIZOWANA macierz decyzyjna (min–max)
    # -------------------------------------------------
    # Alternatywy: A1, A2, A3, A4
    # Kryteria:
    # C1 – koszt (min)
    # C2 – jakość (max)
    # C3 – czas realizacji (min)

    norm_matrix = np.array([
        [0.00, 0.3333, 0.00],
        [1.00, 1.0000, 1.00],
        [0.50, 0.6667, 0.6667],
        [0.20, 0.0000, 0.3333]
    ], dtype=float)

    alternatives = ["A1", "A2", "A3", "A4"]

    # -------------------------------------------------
    # 2. Typy kryteriów
    #  1  -> maksymalizacja
    # -1 -> minimalizacja
    # -------------------------------------------------
    types = np.array([-1, 1, -1])

    # -------------------------------------------------
    # 3. Wagi kryteriów
    # (wyznaczone na podstawie danych oryginalnych)
    # -------------------------------------------------
    weights = np.array([0.4237, 0.2985, 0.2778])

    print("Wagi kryteriów:")
    for i, w in enumerate(weights, start=1):
        print(f"C{i}: {w:.4f}")

    # -------------------------------------------------
    # 4. TOPSIS
    # -------------------------------------------------
    topsis = TOPSIS()
    topsis_scores = topsis(norm_matrix, weights, types)

    # -------------------------------------------------
    # 5. SPOTIS
    # SPOTIS działa na danych oryginalnych + granicach
    # -------------------------------------------------
    original_matrix = np.array([
        [5000, 7, 30],
        [6000, 9, 45],
        [5500, 8, 40],
        [5200, 6, 35]
    ], dtype=float)

    bounds = np.array([
        [5000, 6000],  # koszt
        [6, 9],        # jakość
        [30, 45]       # czas
    ], dtype=float)

    spotis = SPOTIS(bounds)
    spotis_scores = spotis(original_matrix, weights, types)

    # -------------------------------------------------
    # 6. Wyniki
    # -------------------------------------------------
    print("\n=== Wyniki TOPSIS ===")
    for alt, score in zip(alternatives, topsis_scores):
        print(f"{alt}: {score:.4f}")

    print("\n=== Wyniki SPOTIS ===")
    for alt, score in zip(alternatives, spotis_scores):
        print(f"{alt}: {score:.4f}")

    # -------------------------------------------------
    # 7. Rankingi
    # -------------------------------------------------
    topsis_ranking = np.argsort(-topsis_scores)
    spotis_ranking = np.argsort(spotis_scores)

    print("\nRanking TOPSIS:")
    for i, idx in enumerate(topsis_ranking, start=1):
        print(f"{i}. {alternatives[idx]}")

    print("\nRanking SPOTIS:")
    for i, idx in enumerate(spotis_ranking, start=1):
        print(f"{i}. {alternatives[idx]}")


if __name__ == "__main__":
    main()
