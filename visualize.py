import matplotlib.pyplot as plt


def visualize(mt_results, mp_results, title):
    plt.plot(range(len(mt_results)), mt_results, color='green', marker='o')
    plt.plot(range(len(mp_results)), mp_results, color='red', marker='*')
    plt.ylabel("Time")
    plt.xlabel("jobs")
    plt.title(title)
    plt.show()
