import matplotlib.pyplot as plt

import config
import evaluation
import loader
import risk
import stationarity
from model import FactorModel

SELECTED_FACTORS = ["Factor - Value vs Growth", "Factor - Credit"]


def run_models(df):
    full_model = FactorModel(df)
    full_results = full_model.fit()

    reduced_model = FactorModel(df, SELECTED_FACTORS)
    reduced_results = reduced_model.fit()

    print("=== Full Model ===")
    print(full_results.summary())
    print("\n=== Reduced Model ===")
    print(reduced_results.summary())

    return full_results, reduced_results


def run_evaluation(results):
    metrics = evaluation.evaluate_model(results)
    print("\n=== Model Evaluation ===")
    for k, v in metrics.items():
        print(f"  {k}: {v:.4f}")
    evaluation.plot_residuals(results)
    evaluation.plot_qq(results)
    lm_pvalue = evaluation.test_heteroskedasticity(results)
    print(f"Breush-Pagan p-value: {lm_pvalue:.4f}")


def run_strategy(df, results):
    betas = results.params.drop("const")
    factor_portfolio = df[betas.index].mul(betas, axis=1).sum(axis=1)

    fund_sharpe = risk.sharpe_ratio(df[config.TARGET_COL])
    factor_sharpe = risk.sharpe_ratio(factor_portfolio)

    fund_vol = risk.annualised_volatility(df[config.TARGET_COL])
    factor_vol = risk.annualised_volatility(factor_portfolio)

    fund_mdd = risk.max_drawdown(df[config.TARGET_COL])
    factor_mdd = risk.max_drawdown(factor_portfolio)

    print("\n=== Strategy Comparison ===")
    print(f"  {'':25} {'Fund':>10} {'Factor Portfolio':>18}")
    print(f"  {'Sharpe Ratio':25} {fund_sharpe:>10.4f} {factor_sharpe:>18.4f}")
    print(f"  {'Annualised Volatility':25} {fund_vol:>10.4f} {factor_vol:>18.4f}")
    print(f"  {'Max Drawdown':25} {fund_mdd:>10.4f} {factor_mdd:>18.4f}")

    return factor_portfolio


def run_stationarity(df):
    rolling = stationarity.rolling_betas(df, window=24, factors=SELECTED_FACTORS)
    rolling.plot(figsize=(10, 5))
    plt.title("Rolling Betas")
    plt.tight_layout()
    plt.savefig("plots/rolling_betas.png")
    plt.close()
    print("\nRolling betas saved to plots/rolling_betas.png")
    value_betas = rolling["Factor - Value vs Growth"]
    credit_betas = rolling["Factor - Credit"]
    stationarity.adf_beta_test(value_betas, "Value vs Growth")
    stationarity.adf_beta_test(credit_betas, "Credit")


def main():
    df = loader.clean_data(loader.load_data())

    _, reduced_results = run_models(df)
    run_evaluation(reduced_results)
    run_strategy(df, reduced_results)
    run_stationarity(df)


if __name__ == "__main__":
    main()
