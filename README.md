### Grafy i ich zastosowania
Grupa projektowa "Komiwojażerzy" do laboratoriów z grafów.
AGH WFiIS 2023

## Notatki z zajęć
https://docs.google.com/document/d/1jTSSxTxERUc5G63uMR99I3LYdgY82Wl2X28DValzO7g/edit?usp=sharing

## Setup
  Wymagania:
  - Python 3.10+
  - Rust
  
  Polecam utworzyć wirtualne środowisko za pomocą:
  ```python -m venv path/to/venv```
  
  Aktywacja środowiska:
  ```source venv/bin/activate```
  
  Instalacja modułów:
  ```python -m pip install -r requirements.txt```
  
  Dodanie modułów z Global do ścieżki:
  ```python -m pip install -e . ``` (wywołane w folderze root)

Po dodaniu naszego projektu jako modułu, możemy uruchomić skrypty za pomocą np. ```python -m proj1.z1.py```

`UWAGA`: `proj6` nie należy uruchamiać jako moduł (struktura katalogu została zmieniona ze względu na kod w Rust). Kod Pythona uruchamiać normalnie, natomiast Rust poprzez `cargo run`. 


