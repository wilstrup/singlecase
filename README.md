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
df = pd.DataFrame({...})  # Or load your data from a CSV, database, etc.
data = Data(df)
```

Now you're ready to perform single-case data analysis!

## Core Features

### Data Class

The `Data` class provides an object-oriented interface to represent your single-case data. It assumes any variable with datatype of float as a dependent variable. The dependent and phase variables can be accessed and modified using properties. For example:

```python
data.pvar = 'column_name'  # Set the phase variable
```

### Nonoverlap Pairs (NAP)

The `nap` function computes the Nonoverlap Pairs between two phases in a single-case data frame. It returns a pandas Series containing the NAP values for each dependent variable in the data set.

```python
from singlecase.effectsize import nap
nap_values = nap(data)
```

### Percent Non-overlapping Data (PND)

The `pnd` function computes the Percent Non-overlapping Data between two phases in a single-case data frame. It returns a pandas Series containing the PND values for each dependent variable in the data set.

```python
from singlecase.effectsize import pnd
pnd_values = pnd(data)
```

### Permutation Test

The `permutation_test` function performs a permutation test between two phases in a single-case data frame. It returns a pandas Series containing the p-values for each dependent variable in the data set.

```python
from singlecase.permtest import permutation_test
p_values = permutation_test(data)
```

## License

This project is licensed under the BSD 3-clause license - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The Single Case Research package is being developed by Casper Wilstrup.

