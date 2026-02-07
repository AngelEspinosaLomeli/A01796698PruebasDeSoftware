"""
Módulo para contar la frecuencia de palabras de un archivo.
"""

# pylint: disable=invalid-name

import sys
import time


def get_words_from_file(file_path):
    """Lee un archivo y devuelve una lista de todas las palabras encontradas."""
    words = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                try:
                    # Dividimos la línea por espacios en blanco
                    parts = line.split()
                    for word in parts:
                        # Limpiamos puntuación básica si es necesario
                        clean_word = word.strip().lower()
                        if clean_word:
                            words.append(clean_word)
                except (UnicodeDecodeError, AttributeError):
                    print(f"Error: Invalid data at line {line_num}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return words


def count_frequencies(word_list):
    """Cuenta la frecuencia de cada palabra utilizando el algoritmo básico del diccionario."""
    freq_dict = {}
    for word in word_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict


def main():
    """Función de ejecución principal."""
    if len(sys.argv) < 2:
        print("Usage: python wordCount.py fileWithData.txt")
        return

    start_time = time.time()
    file_path = sys.argv[1]

    all_words = get_words_from_file(file_path)
    counts = count_frequencies(all_words)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Preparar el reporte
    header = f"{'Word':<20} | {'Frequency':<10}\n"
    separator = "-" * 33 + "\n"
    output = header + separator

    # Ordenamos las palabras alfabéticamente para mejor lectura
    for word in sorted(counts.keys()):
        output += f"{word:<20} | {counts[word]:<10}\n"

    footer = f"\nExecution Time: {elapsed_time:.6f} seconds\n"
    final_report = output + footer

    print(final_report)

    with open("WordCountResults.txt", "w", encoding='utf-8') as f:
        f.write(final_report)


if __name__ == "__main__":
    main()

    
