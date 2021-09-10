import matplotlib.pyplot as plt
import tui
import utils.process



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
    x = []
    y = []
    for cat in categories:
        x.append(cat)
        y.append(len(categories[cat]))
    plt.title(f"Entities sorted by gravity")
    plt.xlabel("Gravity type")
    plt.ylabel("Number of entities")
    plt.bar(x, y)
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
    print('Orbits')
    print(summary)


def gravity_animation(categories):
    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """
    print('Gravity animation')
    print(categories)
