# Visualização de Otimização de Colônia de Formigas

###### [English Below]

## Descrição

Este repositório contém um visualizador de Otimização por Colônia de Formigas (ACO) usando a biblioteca Pygame. O objetivo é encontrar o caminho mais curto que visita um conjunto de pontos gerados aleatoriamente em uma tela. O algoritmo ACO é uma técnica inspirada no comportamento das formigas para encontrar caminhos eficientes em um grafo.

## Dependências

Para executar este projeto, você precisará das seguintes bibliotecas Python:

- `pygame`: Usada para renderização gráfica e interação com o usuário.
- `random`: Biblioteca padrão do Python usada para gerar pontos aleatórios.

Você pode instalar o `pygame` usando o pip:

```bash
pip install pygame
```

Para executar o visualizador basta digitar:

```bash
python3 main.py
```

## Estrutura do Projeto

- **main**: O arquivo principal que executa o visualizador.
- **point**: Define a classe `Point` para representar os pontos no espaço 2D.
- **ant_colony_optimizer**: Implementa o algoritmo de Otimização por Colônia de Formigas.
- **pygame_renderer**: Contém a classe `PygameRenderer` que gerencia a renderização gráfica usando Pygame.
- **utils**: Funções que são utilizadas em vários pontos do código

## Futuras Implementações

- **Documentação**
  - Conceitos sobre ACO e computação genética/evolutiva
  - Detalhamento do conteúdo e funcionamento de cada classe
- **Funcionalidades**
  - Modularização da inicialização para aceitar matriz de distâncias e listas de adjacências
  - Modularização das classes para facilitar os experimentos com outros algoritmos

---

# Ant Colony Optimization Visualization

## Description

This repository contains a visualization of Ant Colony Optimization (ACO) using the Pygame library. The goal is to find the shortest path that visits a set of randomly generated points on a screen. The ACO algorithm is a technique inspired by the behavior of ants to find efficient paths in a graph.

## Dependencies

To run this project, you will need the following Python libraries:

- `pygame`: Used for graphical rendering and user interaction.

- `random`: Standard Python library used to generate random points.

You can install pygame using pip:

```bash
pip install pygame
```

To run the visualization, simply type:

```bash
python3 main.py
```

## Project Structure

- **main**: The main file that runs the visualization.

- **point**: Defines the Point class to represent points in 2D space.

- **ant_colony_optimizer**: Implements the Ant
  Colony Optimization algorithm.

- **pygame_renderer**: Contains the `PygameRenderer` class that manages graphical rendering using Pygame.

- **utils**: Functions that are used in various parts of the code.

## Future Implementations

- **Documentation**
  - Concepts about ACO and genetic/evolutionary computing.
  - Detailed content and functionality of each class.
- **Features**
  - Modularization of initialization to accept distance matrices and adjacency lists.
  - Modularization of classes to facilitate experiments with other algorithms.
