from JQEditor.JQ_plt.settings import *
import matplotlib.pyplot as plt
import numpy as np


def set_color(val):
    """Выбор цвета решетки в зависимости от значения J"""
    if val == 1:
        return J_PLUS_COLOR
    elif val == -1:
        return J_MIN_COLOR
    elif val == 0:
        return 'white'


def draw_model0(N, J_horizontal, J_vertical):
    # Создание графика
    fig, ax = plt.subplots(figsize=(FIGSIZE_WIDTH, FIGSIZE_HEIGHT))

    # Отрисовка сетки
    hor_i = 0; ver_i = 0
    for i in range(N):
        for j in range(N):
            x = j * spacing
            y = i * spacing
            if j < N - 1:
                color = set_color(J_horizontal[hor_i])
                if color == J_PLUS_COLOR:
                    lw = J_PLUS_LINE_THICKNESS
                else:
                    lw = J_MIN_LINE_THICKNESS
                ax.plot([x, x + spacing], [y, y], color=color, linewidth=lw)
                hor_i += 1

    for i in range(N):
        for j in range(N):
            x = j * spacing
            y = i * spacing
            if i < N - 1:
                color = set_color(J_vertical[ver_i])
                if color == J_PLUS_COLOR:
                    lw = J_PLUS_LINE_THICKNESS
                else:
                    lw = J_MIN_LINE_THICKNESS
                ax.plot([x, x], [y, y + spacing], color=color, linewidth=lw)
                ver_i += 1

    if draw_clusters:
        cluster_val = 4 if CLUSTER_J_VAl == 1 else -4

        # Поиск класеров
        ind = 0
        for i in range(N):
            for j in range(N):
                x = j * spacing
                y = i * spacing

                # Проверка всех J вокруг квадрата
                # Закрасить квадрат, если кластер найден
                if j < N - 1 and i < N - 1:

                    sum_square = 0
                    sum_square += J_horizontal[ind]
                    sum_square += J_horizontal[ind + (N - 1)]
                    sum_square += J_vertical[ind + i]
                    sum_square += J_vertical[ind + i + 1]

                    # Выбор цвета кластеров
                    if sum_square == cluster_val:
                        square_color = CLUSTER_COLOR
                    else:
                        square_color = 'white'

                    if debug_output:
                        print(f'({square_color}: {sum_square})\t{J_horizontal[ind]}\t{J_horizontal[ind + (N - 1)]}'
                            f'\t{J_vertical[ind + i]}\t{J_vertical[ind + i + 1]}')

                    ax.fill([x, x+spacing, x+spacing, x], [y, y, y+spacing, y+spacing], color=square_color, alpha=CLUSTER_ALPHA)
                    ind += 1

    # Маркеры на границах
    for i in range(N):
        for j in range(N):
            x = j * spacing
            y = i * spacing
            ax.plot(x, y, f'{MARKER_COLOR}{MARKER}', markersize=MARKER_SIZE)

    # Настройки осей
    ax.set_xlim(-spacing, N * spacing)
    ax.set_ylim(-spacing, N * spacing)

    # Настройка меток по осям
    ticks_x = np.arange(0, N * spacing + spacing, spacing)
    ticks_y = np.arange(0, N * spacing + spacing, spacing)

    # Устанавливаем метки осей, исключая последнюю
    ax.set_xticks(ticks_x[:-1])
    ax.set_yticks(ticks_y[:-1])

    # Отображение подписей с делением на 2
    ax.set_xticklabels(ticks_x[:-1] // 2)
    ax.set_yticklabels(ticks_y[:-1] // 2)

    # Убрать верхнюю и правую границы графика (оси)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Стрелки на концах осей
    arrowprops = dict(facecolor='black', edgecolor='black')

    # Стрелка на оси X (вправо)
    ax.annotate('', xy=(N * spacing, -spacing), xytext=(-spacing, -spacing),
                arrowprops=dict(arrowstyle="->", **arrowprops))

    # Стрелка на оси Y (вверх)
    ax.annotate('', xy=(-spacing, N * spacing), xytext=(-spacing, -spacing),
                arrowprops=dict(arrowstyle="->", **arrowprops))

    fig.canvas.manager.set_window_title('Для настройки графика используйте JQEditor.JQ_plt.settings')

    # Настройки сетки и соотношения
    ax.grid(False)
    ax.set_aspect('equal')
    plt.show()