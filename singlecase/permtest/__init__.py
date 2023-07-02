import numpy as np
from typing import List, Tuple, Union, Callable    
import pandas as pd

from singlecase.data import Data

def permutation_test(data: Data,
                     statistic: Union[str, Callable] = 'mean',
                     num_rounds: int = 10000,
                     seed: int = None) -> pd.Series:
    """
    Perform a permutation test between two phases in a single-case data frame.

    Args:
        data (singlecase.Data): A single-case data set.
        statistic (Union[str, Callable], optional): The statistic to be used in the permutation test
            (either 'mean', 'median', or a custom callable). Default is 'mean'.
        num_rounds (int, optional): The number of iterations for the permutation test. Default is 10000.
        seed (int, optional): Random seed for reproducibility. Default is None.

    Returns:
        p_values (pd.Series): The calculated p-values in a pd.Series.
    """

    pvar = data.pvar
    phases = data._df[pvar].unique()
    if len(phases) != 2:
        raise ValueError(f"Only two phases are supported. The following phases were found in the phase variable : {pvar}: {phases}")

    if isinstance(statistic, str):
        if statistic == 'mean':
            statistic = np.mean
        elif statistic == 'median':
            statistic = np.median
        else:
            raise ValueError("statistic must be either 'mean', 'median', or a callable")

    np.random.seed(seed)

    p_values = {}

    df = data._df
    for dvar in data.dvars:
        phase1_data = df.loc[df[pvar] == phases[0], dvar].dropna().values
        phase2_data = df.loc[df[pvar] == phases[1], dvar].dropna().values

        observed_diff = statistic(phase2_data) - statistic(phase1_data)

        combined_data = np.concatenate((phase1_data, phase2_data))

        permuted_diffs = []
        for _ in range(num_rounds):
            np.random.shuffle(combined_data)
            permuted_phase1_data = combined_data[:len(phase1_data)]
            permuted_phase2_data = combined_data[len(phase1_data):]
            permuted_diff = statistic(permuted_phase2_data) - statistic(permuted_phase1_data)
            permuted_diffs.append(permuted_diff)

        permuted_diffs = np.array(permuted_diffs)
        p_value = (np.abs(permuted_diffs) >= np.abs(observed_diff)).sum() / num_rounds
        p_values[dvar] = p_value

    return pd.Series(p_values, name="p_value")


