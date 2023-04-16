**[PL]**

# Algorytm Minimax 

Algorytm MiniMax jest to popularna technika wykorzystywana w grach dwuosobowych o sumie zerowej i niskiej złożoności obliczeniowej. Algorytm ten służy do wyznaczenia najlepszej strategii dla gracza, mając na uwadze ruchy przeciwnika oraz zakładając, że przeciwnik gra optymalnie. Pozwala on na wybór najlepszego zagrania, na kilka ruchów do przodu.

Algorytm MiniMax działa na zasadzie przeszukiwania drzewa gry, w którym każdy węzeł reprezentuje stan planszy po wykonaniu określonego ruchu. Algorytm przeszukuje drzewo gry rekurencyjnie, wybierając kolejno ruchy graczy i oceniając wartość każdego węzła na podstawie heurystyk. Dla gracza maksymalizującego wartość algorytm wybiera ruch, który maksymalizuje wartość węzła, a dla gracza minimalizującego wartość algorytm wybiera ruch, który minimalizuje wartość węzła.

# Przycinanie alpha-beta

Metoda przycinania alfa-beta (ang. alpha-beta pruning) jest popularną techniką optymalizacji algorytmu MiniMax, pozwalającą znacznie ograniczyć liczbę analizowanych węzłów w drzewie gry. Metoda ta polega na porównywaniu wartości alfa i beta w czasie przeszukiwania drzewa gry i eliminowaniu z analizy części poddrzew, które nie mają szans na osiągnięcie najlepszego wyniku.

Algorytm Minimax z wykorzystaniem metody przycinania alfa-beta działa na zasadzie przechodzenia drzewa gry, przeszukując jednocześnie maksymalnie jeden poziom węzłów dla każdego z graczy. Przy przeszukiwaniu każdego węzła algorytm porównuje wartość alfa i beta, gdzie alfa oznacza najlepszy dotychczas znaleziony wynik dla gracza maksymalizującego wartość, a beta - dla gracza minimalizującego wartość. Jeśli wartość beta jest mniejsza lub równa wartości alfa, to przycinamy dalsze przeszukiwanie poddrzewa, ponieważ przeciwnik nie wybierze takiego węzła. W ten sposób, algorytm eliminuje z analizy pewne fragmenty drzewa, które nie mają znaczenia dla ostatecznego
wyniku.

Metoda przycinania alfa-beta znacznie redukuje liczbę analizowanych węzłów w drzewie gry i pozwala na znaczne przyspieszenie algorytmu MiniMax. 

# Zadanie

Tematem projektu jest implementacja algorytmu MiniMax z obcinaniem α – β oraz zbadanie wpływu głębokości przeszukiwania dla gry Młynek na 6 pionków (ang. Six Men’s Morris) uwzględniając warunek, że dla różnych ruchów o tej samej jakości, algorytm powinien zwracać losowy z nich.


=========================================================================================

**[ENG]**

# Minimax Algorithm
The MiniMax algorithm is a popular technique used in two-player zero-sum games with low computational complexity. This algorithm is used to determine the best strategy for a player, taking into account the opponent's moves and assuming that the opponent plays optimally. It allows for the selection of the best move, several moves ahead.

The MiniMax algorithm works by searching a game tree, where each node represents the state of the board after a specific move. The algorithm searches the game tree recursively, sequentially selecting players' moves and evaluating the value of each node based on heuristics. For the maximizing player, the algorithm chooses the move that maximizes the value of the node, and for the minimizing player, the algorithm chooses the move that minimizes the value of the node.

# Alpha-Beta Pruning

The alpha-beta pruning method is a popular optimization technique for the MiniMax algorithm, allowing for a significant reduction in the number of analyzed nodes in the game tree. This method involves comparing the alpha and beta values during the search of the game tree and eliminating from analysis the sub-trees that have no chance of achieving the best result.

The MiniMax algorithm using the alpha-beta pruning method works by traversing the game tree, simultaneously searching a maximum of one level of nodes for each player. When traversing each node, the algorithm compares the alpha and beta values, where alpha represents the best result found so far for the maximizing player and beta for the minimizing player. If the beta value is less than or equal to the alpha value, the algorithm prunes the further search of the subtree, because the opponent will not choose that node. In this way, the algorithm eliminates from analysis certain parts of the tree that are irrelevant to the final result.

The alpha-beta pruning method significantly reduces the number of analyzed nodes in the game tree and allows for a significant acceleration of the MiniMax algorithm.

# Task

The project's topic is the implementation of the MiniMax algorithm with alpha-beta pruning and the examination of the influence of the search depth for the game Six Men's Morris, taking into account the condition that for different moves of the same quality, the algorithm should return one of them randomly.
