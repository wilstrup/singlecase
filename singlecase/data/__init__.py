from typing import Union, Dict
import pandas as pd


class Data:
    """
    A class for constructing and storing single-case data.
    """

    def __init__(self, data: Union[pd.DataFrame, Dict]):
        """
        Args:
            data (pd.DataFrame): The data set.
        """
        if isinstance(data, dict):
            self._df = pd.DataFrame(data)
        elif isinstance(data, pd.DataFrame):
            self._df = data.copy()
        else:
            raise ValueError("data must be a pd.DataFrame or a dict")

        self._pvar = None

        # float columns are assumend to be dependent variables
        self._dvars = [col for col in self._df.columns if self._df[col].dtype == float]

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
        if pvar not in self._df.columns:
            raise ValueError("pvar must be the name of a column in the data frame")
        self._pvar = pvar

    @property
    def dvars(self):
        """
        Get the dependent variables.
        """
        return self._dvars

