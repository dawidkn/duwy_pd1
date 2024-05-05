import numpy as np

def oblicz_transformacje(punkt_referencyjny, kat):
    # Obliczenie macierzy obrotu dla danego kąta
    macierz_obrotu = np.array([[np.cos(kat), -np.sin(kat)],
                               [np.sin(kat), np.cos(kat)]])
    # Przesunięcie do punktu referencyjnego
    przesuniecie = np.array(punkt_referencyjny)
    return macierz_obrotu, przesuniecie

# Przykład użycia funkcji
punkt_referencyjny = (0, 0)
kat = np.pi/4  # Przykładowy kąt (45 stopni)
transformacja = oblicz_transformacje(punkt_referencyjny, kat)
macierz_obrotu, przesuniecie = transformacja
print("Macierz obrotu:")
print(macierz_obrotu)
print("Przesunięcie:")
print(przesuniecie)