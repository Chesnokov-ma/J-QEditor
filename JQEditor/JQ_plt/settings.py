# Настройка внешнего вида

FIGSIZE_WIDTH = 5
FIGSIZE_HEIGHT = 5

J_PLUS_COLOR = 'red'
J_MIN_COLOR = 'black'
J_PLUS_LINE_THICKNESS = 1.3
J_MIN_LINE_THICKNESS = 1.1

MARKER_COLOR = 'k'          # цвет маркеров в узлах системы согласно matplotlib
MARKER = 'D'                # форма маркеров в узлах системы согласно matplotlib
MARKER_SIZE = 3

draw_clusters = True        # отрисовка кластеров
CLUSTER_J_VAl = 1          # искать кластеры среди +-J (1 = +J | -1 = -J)
CLUSTER_COLOR = J_PLUS_COLOR if CLUSTER_J_VAl == 1 else J_MIN_COLOR
CLUSTER_ALPHA = 0.2        # прозрачность

debug_output = False
spacing = 2                # дополнительное расстояние между узлами

