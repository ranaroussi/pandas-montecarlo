#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Monte Carlo Simulator
# https://github.com/ranaroussi/pandas-montecarlo
#
# Copyright 2017 Ran Aroussi
#
# Licensed under the GNU Lesser General Public License, v3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/lgpl-3.0.en.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


__version__ = "0.0.2"
__author__ = "Ran Aroussi"
__all__ = ['montecarlo']

import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.base import PandasObject

def montecarlo(series, sims=100, bust=-1, goal=0):

    if not isinstance(series, pd.Series):
        raise ValueError("Data must be a Pandas Series")

    class __make_object__:
        """Monte Carlo simulation results"""
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    def plot(title="Monte Carlo Simulation Results", figsize=None):
        fig, ax = plt.subplots(figsize=figsize)
        ax.plot(cumsum, lw=1, alpha=.8)
        ax.plot(cumsum["original"], lw=3, color="r", alpha=.8, label="Original")
        ax.axhline(0, color="black")
        ax.legend()
        ax.set_title(title, fontweight="bold")
        plt.ylabel("Results")
        plt.xlabel("Occurrences")
        plt.show()
        plt.close()

    results = [series.values]
    for i in range(1, sims):
        results.append(series.sample(frac=1).values)

    df = pd.DataFrame(results).T
    df.rename(columns={0:'original'}, inplace=True)

    cumsum = df.cumsum()
    total = cumsum[-1:].T
    dd = cumsum.min()[cumsum.min() < 0]
    nobust = cumsum[cumsum.min()[cumsum.min() > -abs(bust)].index][-1:]

    return __make_object__(**{
        "data": df,
        "stats": {
            "min": total.min().values[0],
            "max": total.max().values[0],
            "mean": total.mean().values[0],
            "median": total.median().values[0],
            "std": total.std().values[0],
            "maxdd": dd.min(),
            "bust": len(dd[dd <= -abs(bust)]) / sims,
            "goal": (nobust >= abs(goal)).sum().sum() / sims,
        },
        "maxdd": {
            "min": dd.min(),
            "max": dd.max(),
            "mean": dd.mean(),
            "median": dd.median(),
            "std": dd.std()
        },
        "plot": plot
    })


PandasObject.montecarlo = montecarlo