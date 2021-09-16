import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def entities_pie(categories):
    """
    Task 24: Display a single subplot that shows a pie chart for categories.

    The function should display a pie chart with the number of planets and the number of non-planets from categories.

    :param categories: A dictionary with planets and non-planets
    :return: Does not return anything
    """

    def in_the_pie(x):
        # print(x)
        return '{:.4f}%\n({:.0f})'.format(x, entities * x / 100)

    entities = 0
    pie_labels = []
    y = []
    for cat in categories:
        entities += len(categories[cat])
        y.append(len(categories[cat]))
        pie_labels.append(cat)
    planet_explode = [0.4, 0]
    plt.title("Planets and Non-Planets Objects")
    plt.pie(y, labels=pie_labels, explode=planet_explode, autopct=in_the_pie, shadow=True)
    # plt.show()
    # input("Press Enter to continue")
    # plt.close()
    plt.savefig('./img/pie.png')


def entities_bar(categories):
    """
    Task 25: Display a single subplot that shows a bar chart for categories.

    The function should display a bar chart for the number of 'low', 'medium' and 'high' gravity entities.

    :param categories: A dictionary with entities categorised into 'low', 'medium' and 'high' gravity
    :return: Does not return anything
    """
    fig, ax = plt.subplots()
    x = []
    y = []
    for cat in categories:
        x.append(cat)
        y.append(len(categories[cat]))
    plt.title(f"Entities sorted by gravity")
    plt.xlabel("Gravity type")
    plt.ylabel("Number of entities")
    bar_list = plt.bar(x, y, color='yrg')
    # bar_list[1].set_color('r')
    # bar_list[2].set_color('g')

    for i, rect in enumerate(bar_list):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., (0.95 if y[i] > 50 else 1.1) * height,
                y[i],
                ha='center', va='bottom', rotation=0)

    # plt.show()
    # input("Press Enter to continue")
    # plt.close()

    plt.savefig('./img/bar.png')


def orbits(summary):
    """
    Task 26: Display subplots where each subplot shows the "small" and "large" entities that orbit the planet.

    Summary is a nested dictionary of the form:
    summary = {
        "orbited planet": {
            "small": [entity, entity, entity],
            "large": [entity, entity]
        }
    }

    The function should display for each orbited planet in summary. Each subplot should show a bar chart with the
    number of "small" and "large" orbiting entities.

    :param summary: A dictionary containing the "small" and "large" entities for each orbited planet.
    :return: Does not return anything
    """
    total = len(summary)
    cols = 2 if total < 5 else 3
    rows = total // cols + 1
    x = [*summary[list(summary.keys())[0]].keys()]
    bar = 1
    for planet in summary:
        print(planet)
        y = [len(summary[planet][z]) for z in x]
        plt.subplot(rows, cols, bar)
        plt.bar(x, y)
        plt.title(f"{planet} orbits", pad=1)
        bar += 1
    plt.suptitle("Planet Orbits")
    plt.tight_layout()

    # print('Orbits')
    # print(summary)
    plt.savefig('./img/subplots.png')


def gravity_animation(categories):
    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """
    x = []
    y = []
    for cat in categories:
        x.append(cat)
        y.append(len(categories[cat]))

    fig, ax = plt.subplots()
    ax.set_xlim(0, 4)
    ax.set_ylim(0, max(y))
    line, = ax.plot(1, y[0])
    plt.title(f"Entities sorted by gravity")
    plt.xlabel("Gravity: 1 - Low, 2 - Medium, 3 - High")
    plt.ylabel("Number of entities")
    x_anim = []
    y_anim = []

    def a_frames(i):

        def my_func(fr):
            w = fr - int(fr)
            ind = 0 if fr <= 2 else 1
            return (1-w) * y[ind] + w * y[ind + 1]

        x_anim.append(i)
        y_anim.append(my_func(i))

        line.set_xdata(x_anim)
        line.set_ydata(y_anim)
        return line,

    animation = FuncAnimation(fig, func=a_frames, frames=np.arange(1, 3, 0.1), interval=100)
    animation.save('./img/anim.gif')
