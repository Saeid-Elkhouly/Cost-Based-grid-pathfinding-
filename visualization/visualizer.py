import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def visualize_grid(grid, path=None):
    """
    grid: 2D list with costs (0 = obstacle)
    path: list of positions [(row, col), ...]
    """
    nrows = len(grid)
    ncols = len(grid[0])
    data = [[0 if cell == 0 else 1 for cell in row] for row in grid]

    cmap = mcolors.ListedColormap(['black', 'white', 'green', 'red'])
    fig, ax = plt.subplots()

    # Draw grid
    ax.imshow(data, cmap=cmap, origin='upper')

    # Draw path if exists
    if path:
        for r, c in path:
            ax.add_patch(plt.Rectangle((c-0.5, r-0.5), 1, 1, color='green', alpha=0.5))
        # Start & Goal
        sr, sc = path[0]
        gr, gc = path[-1]
        ax.add_patch(plt.Rectangle((sc-0.5, sr-0.5), 1, 1, color='blue', alpha=0.7))
        ax.add_patch(plt.Rectangle((gc-0.5, gr-0.5), 1, 1, color='red', alpha=0.7))

    ax.set_xticks(range(ncols))
    ax.set_yticks(range(nrows))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)
    plt.show()
