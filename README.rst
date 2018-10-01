Monte Carlo Simulator for Pandas Series
=======================================

.. image:: https://img.shields.io/badge/python-3.4+-blue.svg?style=flat
    :target: https://pypi.python.org/pypi/pandas-montecarlo
    :alt: Python version

.. image:: https://img.shields.io/pypi/v/pandas-montecarlo.svg?maxAge=60
    :target: https://pypi.python.org/pypi/pandas-montecarlo
    :alt: PyPi version

.. image:: https://img.shields.io/pypi/status/pandas-montecarlo.svg?maxAge=60
    :target: https://pypi.python.org/pypi/pandas-montecarlo
    :alt: PyPi status

.. image:: https://img.shields.io/travis/ranaroussi/pandas-montecarlo/master.svg?maxAge=1
    :target: https://travis-ci.org/ranaroussi/pandas-montecarlo
    :alt: Travis-CI build status

.. image:: https://img.shields.io/badge/Patreon-accepting-ff69b4.svg?style=flat
    :target: https://www.patreon.com/aroussi
    :alt: Patreon Status

.. image:: https://img.shields.io/github/stars/ranaroussi/pandas-montecarlo.svg?style=social&label=Star&maxAge=60
    :target: https://github.com/ranaroussi/pandas-montecarlo
    :alt: Star this repo

.. image:: https://img.shields.io/twitter/follow/aroussi.svg?style=social&label=Follow&maxAge=60
    :target: https://twitter.com/aroussi
    :alt: Follow me on twitter

\

**pandas-montecarlo** is a lightweight Python library for running simple
`Monte Carlo Simulations <https://en.wikipedia.org/wiki/Monte_Carlo_method>`_ on Pandas Series data.

`Changelog » <./CHANGELOG.rst>`__

-----

Quick Start
-----------

Let's run a monte carlo simulation on the returns of `SPY <https://finance.yahoo.com/quote/SPY>`_ (S&P 500 Spider ETF).

First, let's download SPY's data and calculate the daily returns.

.. code:: python

    from pandas_datareader import data

    df = data.get_data_yahoo("SPY")
    df['return'] = df['Adj Close'].pct_change().fillna(0)

Next, we'll import ``pandas_montecarlo`` and run monte carlo simulation
with 10 simulations (for demo simplifications) and bust/max drawdown set to ``-10.0%``
and goal threshhold set to ``+100.0%`` (defaults is ``>=0%``):

.. code:: python

    import pandas_montecarlo
    mc = df['return'].montecarlo(sims=10, bust=-0.1, goal=1)


**Plot simulations**

.. code:: python

    mc.plot(title="SPY Returns Monte Carlo Simulations")  # optional: , figsize=(x, y)

.. image:: https://raw.githubusercontent.com/ranaroussi/pandas-montecarlo/master/demo.png
   :width: 640 px
   :height: 360 px
   :alt: demo


**Show test stats**

.. code:: python

    print(mc.stats)

    # prints
    {
        'min':    0.98088401987146789,
        'max':    0.98088401987146934,
        'mean':   0.98088401987146911,
        'median': 0.98088401987146911,
        'std':    4.0792198665315552e-16,
        'maxdd': -0.17221175099828012,  # max drawdown
        'bust':   0.2,  # probability of going bust
        'goal':   0.0   # probability of reaching 100% goal
    }

**Show bust / max drawdown stats**

.. code:: python

    print(mc.maxdd)

    # prints
    {
        'min':    -0.27743285515585991,
        'max':    -0.00031922711279186444,
        'mean':   -0.07888087155686732,
        'median': -0.06010335858432081,
        'std':     0.062172124557467685
    }

**Access raw simulations' DataFrame**

.. code:: python

    print(mc.data.head())

.. code:: text

        original          1          2          3          4  ...       10
    0   0.000000   0.017745  -0.002586  -0.005346  -0.042107  ...  0.00139
    1   0.002647   0.000050   0.000188   0.010141   0.007443  ...  0.00108
    2   0.000704   0.002916   0.005324   0.000073  -0.003238  ...  0.00071
    3   0.004221   0.008564   0.001397   0.007950  -0.006392  ...  0.00902
    4   0.003328  -0.000511   0.005123   0.013491  -0.005105  ...  0.00252


Installation
------------

Install ``pandas_montecarlo`` using ``pip``:

.. code:: bash

    $ pip install pandas_montecarlo --upgrade --no-cache-dir

Requirements
------------

* `Python <https://www.python.org>`_ >=3.4
* `Pandas <https://github.com/pydata/pandas>`_ (tested to work with >=0.18.1)
* `Matplotlib <https://matplotlib.org>`_ (tested to work with >=1.5.3)


Legal Stuff
------------

**pandas-montecarlo** is distributed under the **GNU Lesser General Public License v3.0**. See the `LICENSE.txt <./LICENSE.txt>`_ file in the release for details.


P.S.
------------

Please drop me an note with any feedback you have.

**Ran Aroussi**
