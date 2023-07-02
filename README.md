# Single Case Research Package

The Single Case Research package is a Python library designed to assist in conducting single-case research studies. The package provides tools to analyze single-case data sets. It is designed for simplicity and ease of use, with a range of methods to calculate various statistical measures for single-case data sets. The package is perfect for analysts and researchers dealing with single-case designs, providing a framework to load, manage, and manipulate such data, along with robust statistical functions to interpret the data.

More functionality will be added as the package is further developed

## Installation

You can install the package using pip:

```shell
pip install singlecase
```


## Usage

To use `singlecase`, first import the package into your Python environment:

```python
from singlecase.data import Data
```

Then, create a `Data` object with either a pandas DataFrame or a dictionary:

```python
data = Data({
    'phase': ['A1', 'A1', 'A1', 'B', 'B', 'B', 'A2', 'A2', 'A2'],
    'dvar1': [1.0, 2.5, 3.2, 4.2, 5.5, 6.2, 2.0, 2.4, 3.1],
    'dvar2': [2.5, 3.2, 4.6, 5.6, 6.2, 7.8, 3.3, 4.1, 4.8],
})
```

Now you're ready to perform single-case data analysis.

## Core Features

### Data Class

The `Data` class provides an object-oriented interface to represent your single-case data. It assumes any variable with datatype of float as a dependent variable. The dependent and phase variables can be accessed and modified using properties. For example:

```python
data.pvar = 'column_name'  # Set the phase variable, if it is not named 'phase'
```

### Nonoverlap Pairs (NAP)

The `nap` function computes the Nonoverlap Pairs between two phases in a single-case data frame. It returns a pandas Series containing the NAP values for each dependent variable in the data set.

```python
from singlecase.effectsize import nap
nap_values = nap(data, phases["A1", "B"])
```

### Percent Non-overlapping Data (PND)

The `pnd` function computes the Percent Non-overlapping Data between two phases in a single-case data frame. It returns a pandas Series containing the PND values for each dependent variable in the data set.

```python
from singlecase.effectsize import pnd
pnd_values = pnd(data, phases=["A1", "B"])
```

### Permutation Test

The `permutation_test` function performs a permutation test between two phases in a single-case data frame. It returns a pandas Series containing the p-values for each dependent variable in the data set. The p-value is the probability that the two phases have the same mean.

```python
from singlecase.permtest import permutation_test
p_values = permutation_test(data, phases=["A1","A2"])
```


## Complete example

This complete example creates a new `singlecase.Data` from a Python dictionary. The dataset has two dependent variables `dvar1` and `dvar2`. The phase variable is called `phase` and consists of the two phases "A" and "B". Based on this data, the PND and NAP values are calculated and printed. The probability that the two phases have the same mean is then calculated using permutation tests and printed. Since the data contains only two phases, it is not necessary to specify which phases to compare in `pnd`, `nap` and `permutation_test` function calls.

```python
import pandas as pd
from singlecase.data import Data
from singlecase.effectsize import pnd, nap
from singlecase.permtest import permutation_test

# Create a sample data
data_dict = {
    'phase': ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B'],
    'dvar1': [1.0, 2.5, 3.2, 4.6, 2.8, 5.6, 3.7, 4.2, 5.5, 6.2, 7.3, 8.5],
    'dvar2': [2.5, 3.2, 4.6, 5.1, 4.8, 5.2, 6.7, 5.6, 6.2, 7.8, 8.4, 7.2],
}

# Instantiate Data object
data = Data(data_dict)

# Calculate PND
pnd_values = pnd(data)
print(f"PND values:\n{pnd_values}\n")

# Calculate NAP
nap_values = nap(data)
print(f"NAP values:\n{nap_values}\n")

# Calculate the p-value the mean of the two phases being the same
perm_p = permutation_test(data)
print(f"Probability that A and B phases have same mean:\n{perm_p}\n")
```


## License

This project is licensed under the BSD 3-clause license - see the LICENSE file for details.

## About the package

The Single Case Research package is supported by [Abzu](https://www.abzu.ai) as part of an ongoing mission to improve scientific research powered by artificial intelligence.

The primary author of the package is [Casper Wilstrup](https://twitter.com/cwilstrup). New contributors are welcome.

