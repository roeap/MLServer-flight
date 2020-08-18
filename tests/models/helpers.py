import pytest

from mlserver.models.sklearn import _SKLEARN_PRESENT
from mlserver.models.xgboost import _XGBOOST_PRESENT

skipif_sklearn_missing = pytest.mark.skipif(
    not _SKLEARN_PRESENT, reason="scikit-learn is not present"
)

skipif_xgboost_missing = pytest.mark.skipif(
    not _XGBOOST_PRESENT, reason="xgboost is not present"
)
