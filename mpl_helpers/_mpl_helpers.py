import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np


def ax_off(ax, which='x'):
    """Turn off a specific axis in an ``ax``."""
    getattr(ax, f'get_{which}axis')().set_visible(False)
    return ax


def axes_off(ax):
    """Turn off all axes in an ``ax``."""
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    return ax


def darken_rgb(rgb, p):
    """Darken an "rgb" value by p proportion."""
    assert 0 <= p <= 1, "Proportion must be [0, 1]"
    return [int(x * (1 - p)) for x in rgb]


def despine(ax, top=True, left=True, bottom=True, right=True):
    """Selectively remove spines from an ``ax``."""
    for spine, on in zip(
        ('top', 'left', 'bottom', 'right'), (top, left, bottom, right)
    ):
        ax.spines[spine].set_visible(not on)
    return ax


def grouped_bar_positions(num_groups, num_categories, cluster_width=0.2):
    """Create groups centered on integers with a fixed category size."""
    clusters = []

    for i in range(num_categories):
        clusters.append(np.linspace(
            i - cluster_width,
            i + cluster_width,
            num_groups))

    return list(zip(*clusters))


def is_luminous(rgb):
    """Is an "rgb" value luminous.

    Notes
    -----
    Determined using the formula at:

        https://www.w3.org/TR/WCAG20/#relativeluminancedef

    """
    new_color = []

    for c in rgb:
        if c <= 0.03928:
            new_color.append(c / 12.92)
        else:
            new_color.append(((c + 0.055) / 1.055) ** 2.4)
    L = sum([x * y for x, y in zip([0.2126, 0.7152, 0.0722], new_color)])

    return True if L < 0.179 else False


def lighten_rgb(rgb, p):
    """Will lighten an "rgb" value by p percent."""
    assert 0 <= p <= 1, "Proportion must be [0, 1]"
    return [int((255 - x) * p + x) for x in rgb]


def maximum_xlim_bounds(axes):
    mins, maxes = zip(*[ax.get_xlim() for ax in axes])
    return min(mins), max(maxes)


def maximum_ylim_bounds(axes):
    mins, maxes = zip(*[ax.get_ylim() for ax in axes])
    return min(mins), max(maxes)


def ticklabels_to_integer(ax, axis='y'):
    getattr(ax, f'{axis}axis').set_major_locator(
        mticker.MaxNLocator(integer=True))
    return ax


def ticklabels_to_percent(ax, axis='y', precision=1):
    getattr(ax, f'{axis}axis').set_major_formatter(
        mticker.FuncFormatter(
            lambda s, position: f'{{0:0.{precision}f}}%'.format(s * 100)))
    return ax


def ticklabels_to_scientific(ax, axis='y', precision=2):
    getattr(ax, f'{axis}axis').set_major_formatter(
        mticker.FuncFormatter(
            lambda s, position: f'{{:0.{precision}e}}'.format(s)))
    return ax


def ticklabels_to_thousands_sep(ax, axis='y'):
    getattr(ax, f'{axis}axis').set_major_formatter(
        mticker.FuncFormatter(lambda s, position: f'{int(s):,}'))
    return ax


def remove_every_other_tick(ax, axis):
    if axis == 'x':
        for i in range(len(ax.get_yticklabels())):
            if i % 2 == 0:
                ax.yaxis.get_major_ticks()[-i].tick1On = False
                plt.setp(ax.get_yticklabels()[-i], visible=False)
    elif axis == 'y':
        for i in range(len(ax.get_yticklabels())):
            if i % 2 == 0:
                ax.yaxis.get_major_ticks()[-i].tick1On = False
                plt.setp(ax.get_yticklabels()[-i], visible=False)
    return ax


def ticks_off(ax, which='both'):
    assert which in ('x', 'y', 'both'), 'Which must be `x`, `y`, or `both`.'
    axis = ('x', 'y') if which == 'both' else (which, )

    for axe in axis:
        for tic in getattr(ax, f'{axe}axis').get_major_ticks():
            tic.tick1On = tic.tick2On = False

    return ax
