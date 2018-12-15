<h1 align="center">mpl-helpers</h2>

<p align="center">A Python 3.6 library for tweaking <code>matplotlib</code> figures</p>

<p align="center">
  <a href="#installation"><strong>Installation</strong></a>
  ·
  <a href="#tutorial"><strong>Tutorial</strong></a>
  ·
  <a href="#contributing"><strong>Contributing</strong></a>
</p>

<p align="center">
  <a href="https://codeclimate.com/github/clintval/mpl-helpers/maintainability"><img src="https://api.codeclimate.com/v1/badges/5974a2c5309b6c3ff975/maintainability"></img></a>
  <a href="https://github.com/clintval/mpl-helpers/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></img></a>
</p>

<br>

<h3 align="center">Installation</h3>

```
❯ pip install mpl_helpers
```

Please not this project is under active and early development.

Documentation, tests, and a consistent API will be provided in due time!

<br>

<h3 align="center">Tutorial</h3>

```python
from mpl_helpers import *
```

<br>

**axis_off**: turn off x, y, or all axis in an `ax`

**darken_rgb**: darken an RGB value by a given percent

**despine**: remove either of the four spines in a cartesian `ax`

**grouped_bar_positions**: create equi-spaced positions centered around integers

**is_luminous**: determines if an RGB value is luminous

**lighten_rgb**: lighten an RGB value by a given percent

**maximum_xlim_bounds**: return the maximum xlim bounds by all `ax` objects

**maximum_ylim_bounds**: return the minimum xlim bounds by all `ax` objects

**ticklabels_to_integer**: use an integer formatter on ticklabels

**ticklabels_to_percent**: use a percent formatter on ticklabels

**ticklabels_to_scientific**: use a scientific notation formatter on ticklabels

**ticklabels_to_thousands_sep**: use a thousands seperated comma formatter on ticklabels

**remove_every_other_tick**: remove every other tick

**ticks_off**: turn off x, y, or all axis ticks in an `ax`


<br>

<h3 align="center">Contributing</h3>

Pull requests, feature requests, and issues welcome!

To make a development install:

```bash
❯ git clone git@github.com:clintval/mpl-helpers.git
❯ pip install -e 'mpl-helpers'
```
