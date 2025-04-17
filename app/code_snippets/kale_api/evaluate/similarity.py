from kale.evaluate.similarity_metrics import jaccard_similarity, evaluate_correlations

# Calculate Jaccard Similarity between two lists
jaccard_index = jaccard_similarity(list1, list2)

# Evaluate correlations between prediction bins and uncertainty/error pairs
correlations = evaluate_correlations(bin_predictions, uncertainty_error_pairs, cmaps, num_bins, confidence_invert_tuples)
