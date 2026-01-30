#include <iostream>
#include <omp.h>

#define N 1000
#define chunk 500
#define mostrar 15

void imprimeArreglo(float* d);

int main()
{
    std::cout << "Sumando Arreglos en Paralelo!\n";
    float a[N], b[N], c[N];

    // 1. Inicialización correcta de AMBOS arreglos
    for (int i = 0; i < N; i++)
    {
        a[i] = i * 10.0f;
        b[i] = (i + 3) * 3.7f;
    }

    int pedazos = chunk;

    // 2. Corrección de 'shared' y simplificación de la directiva
#pragma omp parallel for shared(a, b, c, pedazos) schedule(static, pedazos)
    for (int i = 0; i < N; i++)
    {
        c[i] = a[i] + b[i];
    }

    std::cout << "Arreglo A (Primeros " << mostrar << "):" << std::endl;
    imprimeArreglo(a);
    std::cout << "Arreglo B (Primeros " << mostrar << "):" << std::endl;
    imprimeArreglo(b);
    std::cout << "Resultado Suma (C):" << std::endl;
    imprimeArreglo(c);

    return 0;
}

void imprimeArreglo(float* d)
{
    for (int x = 0; x < mostrar; x++)
        std::cout << d[x] << " | ";
    std::cout << std::endl;
}