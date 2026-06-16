import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan


def evaluate_model(results):
    metrics = {
        "R^2": results.rsquared,
        "Adjusted R^2": results.rsquared_adj,
        "F-stat": results.fvalue,
        "F p-value": results.f_pvalue,
    }

    return metrics


def plot_residuals(results):
    plt.scatter(results.fittedvalues, results.resid)
    plt.axhline(0, color="red")
    plt.xlabel("Predicted")
    plt.ylabel("Residuals")
    plt.title("Residuals vs Predicted")
    plt.savefig("plots/residuals.png")


def plot_qq(results):
    plt.figure(figsize=(6, 6))
    sm.qqplot(results.resid, line="45", fit=True)
    plt.title("Q-Q Plot of Regression Residuals")
    plt.savefig("plots/qq_plot.png")


def test_heteroskedasticity(model):

    result = het_breuschpagan(model.resid, model.model.exog)
    lm_stat, lm_pvalue, f_stat, f_pvalue = result

    return lm_pvalue
