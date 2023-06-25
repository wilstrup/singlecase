import pytest
import pandas as pd
import numpy as np

from singlecase.permtest import permutation_test 

def test_permutation_test_basic():
    # Prepare data
    df = pd.DataFrame({
        "measure 1": np.concatenate([np.random.normal(0, 1, 50), np.random.normal(1, 1, 50)]),
        "measure 2": np.concatenate([np.random.normal(0, 1, 50), np.random.normal(1, 1, 50)]),
        "phase": ['A'] * 50 + ['B'] * 50
    })

    # Run test
    result = permutation_test(df, dvars=['measure 1', 'measure 2'], pvar='phase')

    # Check result - the p-value should be close to 0 due to large difference in distributions
    assert result['measure 1'] < 0.05
    assert result['measure 2'] < 0.05


def test_permutation_test_custom_statistic():
    # Prepare data
    df = pd.DataFrame({
        "measure 1": np.concatenate([np.random.normal(0, 1, 50), np.random.normal(1, 1, 50)]),
        "measure 2": np.concatenate([np.random.normal(0, 1, 50), np.random.normal(1, 1, 50)]),
        "phase": ['A'] * 50 + ['B'] * 50
    })

    # Custom statistic
    def custom_statistic(data):
        return np.percentile(data, 75)  # 75th percentile

    # Run test
    result = permutation_test(df, dvars=['measure 1', 'measure 2'], pvar='phase', statistic=custom_statistic)

    # Check result - the p-value should be close to 0 due to large difference in distributions
    assert result['measure 1'] < 0.05
    assert result['measure 2'] < 0.05
