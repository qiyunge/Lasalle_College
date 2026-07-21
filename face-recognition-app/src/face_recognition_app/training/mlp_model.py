from __future__ import annotations

from typing import Any

from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, StratifiedKFold
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


SEARCH_PARAMETERS = {
    "classifier__hidden_layer_sizes": [(64,), (128,), (128, 64)],
    "classifier__activation": ["relu", "tanh"],
    "classifier__alpha": [0.0001, 0.001, 0.01],
    "classifier__learning_rate_init": [0.0001, 0.001],
}


def create_mlp_pipeline(
    *,
    hidden_layer_sizes: tuple[int, ...] = (128,),
    max_iter: int = 300,
    random_state: int = 42,
) -> Pipeline:
    """Create a reproducible, scaled MLP classification pipeline."""
    if not hidden_layer_sizes or any(size <= 0 for size in hidden_layer_sizes):
        raise ValueError("Hidden-layer sizes must contain positive integers.")
    if max_iter <= 0:
        raise ValueError("Maximum iterations must be positive.")

    return Pipeline(
        [
            ("scaler", StandardScaler()),
            (
                "classifier",
                MLPClassifier(
                    hidden_layer_sizes=hidden_layer_sizes,
                    max_iter=max_iter,
                    # Hyperparameter search already validates with stratified CV.
                    # Scikit-learn 1.7's internal early-stopping scorer applies
                    # np.isnan to string class predictions and fails.
                    early_stopping=False,
                    random_state=random_state,
                ),
            ),
        ]
    )


def create_hyperparameter_search(
    pipeline: Pipeline,
    *,
    search_kind: str = "random",
    cv: int = 5,
    n_iter: int = 12,
    random_state: int = 42,
    n_jobs: int = -1,
) -> GridSearchCV | RandomizedSearchCV:
    """Wrap an MLP pipeline in grid or randomized cross-validation search."""
    if search_kind not in {"grid", "random"}:
        raise ValueError("Search kind must be 'grid' or 'random'.")
    if cv < 2:
        raise ValueError("Cross-validation folds must be at least 2.")
    if n_iter <= 0:
        raise ValueError("Random-search iterations must be positive.")

    splitter = StratifiedKFold(
        n_splits=cv,
        shuffle=True,
        random_state=random_state,
    )
    common_options = {
        "estimator": pipeline,
        "scoring": "accuracy",
        "cv": splitter,
        "n_jobs": n_jobs,
        "refit": True,
        "verbose": 1,
        "return_train_score": False,
    }
    if search_kind == "grid":
        return GridSearchCV(
            param_grid=SEARCH_PARAMETERS,
            **common_options,
        )
    return RandomizedSearchCV(
        param_distributions=SEARCH_PARAMETERS,
        n_iter=n_iter,
        random_state=random_state,
        **common_options,
    )


def training_history(model: Pipeline) -> dict[str, Any]:
    """Return JSON-serializable training information from a fitted pipeline."""
    classifier = model.named_steps["classifier"]
    return {
        "loss": [float(value) for value in classifier.loss_curve_],
        "validation_score": [
            float(value)
            for value in (getattr(classifier, "validation_scores_", None) or [])
        ],
        "iterations": int(classifier.n_iter_),
        "classes": [str(value) for value in classifier.classes_],
    }
