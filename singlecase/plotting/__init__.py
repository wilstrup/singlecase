from typing import List, Tuple
import matplotlib.pyplot as plt

from singlecase.data import Data

def line_chart(data: Data, dvars: List[str] = None, num_per_row: int = 1, phases: List[str] = None, figure_size: Tuple[int, int] = (10, 8), title: str = None):
    """
    Plot the selected dependent variables on a line chart, with separate colors for each phase.

    Args:
        data (Data): The singlecase data to plot.
        dvars (List[str]): The dependent variables to plot. If None, all dependent variables are plotted.
        num_per_row (int): Number of plots per row. Default is 1.
        phases (List[str]): The phases to plot. If None, all phases are plotted.
        figure_size (Tuple[int, int]): The size of the figure. Default is (10, 8).
        title (str): The title of the plot. Default is None.
    """

    if dvars is None:
        dvars = data.dvars

    if phases is None:
        phases = data.phases

    phase_colors = plt.get_cmap('tab10', len(phases))

    rows = (len(dvars) - 1) // num_per_row + 1
    fig = plt.figure(figsize=figure_size)

    if title is not None:
        fig.suptitle(title)

    for idx, dvar in enumerate(dvars):
        ax = fig.add_subplot(rows, num_per_row, idx + 1)

        for i, phase in enumerate(phases):
            phase_data = data.phase_data(phase, dvar)
            ax.plot(phase_data, label=f"Phase: {phase}", color=phase_colors(i), zorder=3)
            ax.scatter(phase_data.index, phase_data, color=phase_colors(i), zorder=3) 

        # Get the min and max value for the current dvar
        min_y = min(data.phase_data(phase, dvar).min() for phase in phases)
        max_y = max(data.phase_data(phase, dvar).max() for phase in phases) 

        y_range = max_y - min_y
        min_y -= y_range * 0.05
        max_y += y_range * 0.05

        ax.set_ylim(min_y, max_y)

        if data.dvar_units[dvar] != "":
            ax.set_ylabel(data.dvar_units[dvar])

        ax.set_xlabel(data.index)
        ax.set_title(f'{dvar} over sessions')
        
        # Only add legend if there is more than one phase
        if len(phases) > 1:
            ax.legend()

    plt.tight_layout()
    plt.show()
