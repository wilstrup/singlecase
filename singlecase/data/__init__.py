import pandas as pd
from typing import List, Union, Tuple, Callable
from singlecase.permtest import permutation_test


class Data:
    """
    A class for constructing and storing single-case data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Args:
            data (pd.DataFrame): The data set.
        """
        self.data = data.copy()

        self._pvar = None

        # float columns are assumend to be dependent variables
        self._dvars = [col for col in self.data.columns if self.data[col].dtype == float]

    @property
    def pvar(self):
        """
        Get the phase variable.
        """
        return self._pvar
    
    @pvar.setter
    def pvar(self, pvar: str):
        """
        Set the phase variable.
        """
        if pvar not in self.data.columns:
            raise ValueError("pvar must be the name of a column in the data frame")
        self._pvar = pvar

    @property
    def dvars(self):
        """
        Get the dependent variables.
        """
        return self._dvars



    def permutation_test(self, statistic: Union[str, Callable] = 'mean', num_rounds: int = 10000, seed: int = None):
        return permutation_test(self.data, self.dvars, self.pvar, phases=self.data[self.pvar].unique(), statistic=statistic, num_rounds=num_rounds, seed=seed)

