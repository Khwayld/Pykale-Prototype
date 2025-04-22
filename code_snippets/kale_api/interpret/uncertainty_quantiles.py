from kale.interpret.uncertainty_quantiles import fit_line_with_ci, quantile_binning_and_est_errors

# Example: Analyze correlations between errors and uncertainties.
correlations = fit_line_with_ci(errors, uncertainties, quantile_thresholds, cmaps)

# Example: Bin errors and estimate error bounds.
binned_errors, estimated_errors = quantile_binning_and_est_errors(errors, uncertainties, num_bins=10)
