"""
Goalpost diagram renderer for Penalty Kick Analyzer using Matplotlib.
"""

from typing import List
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def draw_color_coded_goal(normalized_probabilities: List[float]) -> Figure:
    """
    Draw soccer goal with color-coded section shot probabilities.

    :param normalized_probabilities: List of probabilities for [Left, Middle, Right]
    :return: Matplotlib Figure object
    """
    goal_width, goal_height = 7.32, 2.44
    num_sections = len(normalized_probabilities)
    section_width = goal_width / num_sections

    sorted_indices = np.argsort(normalized_probabilities)
    color_map = ['#FF0000', '#F3FF00', '#2AFF00']  # Red, Yellow, Green
    section_colors = [None] * num_sections
    for rank, idx in enumerate(sorted_indices):
        section_colors[idx] = color_map[rank]

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.set_xlim(-1, goal_width + 1)
    ax.set_ylim(-1, goal_height + 1)
    ax.set_aspect('equal')
    ax.axis('off')

    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    # Draw white goalposts
    post_color = 'white'
    ax.plot([0, 0], [0, goal_height], color=post_color, linewidth=3)
    ax.plot([goal_width, goal_width], [0, goal_height], color=post_color, linewidth=3)
    ax.plot([0, goal_width], [goal_height, goal_height], color=post_color, linewidth=3)

    # Draw net inside the goal
    net_lines = 8
    for i in range(1, net_lines):
        x = i * goal_width / net_lines
        ax.plot([x, x], [0, goal_height], color='white', linestyle='dotted', alpha=0.5)
        y = i * goal_height / net_lines
        ax.plot([0, goal_width], [y, y], color='white', linestyle='dotted', alpha=0.5)

    # Draw color-coded probability sections
    for i, (norm_prob, color) in enumerate(zip(normalized_probabilities, section_colors)):
        x_start = i * section_width
        ax.add_patch(
            plt.Rectangle((x_start, 0), section_width, goal_height, color=color, alpha=0.5)
        )
        ax.text(
            x_start + section_width / 2,
            goal_height / 2,
            f"{norm_prob:.1%}",
            color="black",
            ha="center",
            va="center",
            fontsize=10,
            weight="bold",
        )

    plt.close(fig)
    return fig
