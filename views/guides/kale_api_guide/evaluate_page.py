
import streamlit as st
from navigation import go_to


def evaluate_page():
    """KALE API - Model Evaluation (kale.evaluate)"""

    # --- Page Header ---
    st.markdown(
        """
        <div style="text-align:center;">
            <h2>📊 Model Evaluation - <code>kale.evaluate</code></h2>
            <p style="font-size:18px;">
                This module offers tools for assessing model performance, including metrics, cross-validation methods, and similarity measures.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_left, col_center, col_right = st.columns([3, 1, 3])
    with col_center:
        if st.button("🔙 Back to API Guide"):
            go_to("kale_api")

    st.write("---")


    # --- Expandable Sections ---

    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
        with st.expander("🔍 Cross-Validation Methods"):
            st.write(
                """
                **Leave-One-Group-Out Cross-Validation:**  
                This method tests your model by leaving out one group of data at a time.
                It is useful when your data is divided into groups (for example, by subject or location).  
                
                **Parameters:**
                - `x:` Your input features (data samples).
                - `y:` The correct labels for your data.
                - `groups:` Group identifiers so that one group is left out during each test.
                - `estimator:` The machine learning model you want to evaluate (from Kale or scikit-learn).
                - `use_domain_adaptation:` Option to apply domain adaptation during training.
                
                **Returns:**  
                A dictionary with the performance results for each group, including the number of samples and accuracy.
                """
            )
            st.code(
                """
                from kale.evaluate.cross_validation import leave_one_group_out
                
                # Example usage:
                results = leave_one_group_out(x, y, groups, estimator)
                """
            )

        with st.expander("📏 Performance Metrics"):
            st.write(
                """
                **Performance Metrics:**  
                These functions help you measure how well your model is performing.
                
                **Cross-Entropy with Logits:**  
                Measures the difference between your model's predictions (before applying softmax) and the actual labels.
                - **Parameters:**
                    - `output:` The raw output from your model.
                    - `target:` The true labels.
                    - `weights (optional):` Adjusts the importance of each sample.
                    
                **Top-k Accuracy:**  
                Checks if the correct label is within the top k predictions.
                - **Parameters:**
                    - `output:` Model outputs (before softmax).
                    - `target:` True labels.
                    - `topk:` A tuple specifying which top-k values to compute (e.g., top-1 and top-5).
                    
                **Concordance Index (CI):**  
                Evaluates how well the predicted values match the actual values, particularly useful for ranking problems.
                - **Parameters:**
                    - `y:` True values.
                    - `y_pred:` Predicted values.
                """
            )

            st.code(
                """
                from kale.evaluate.metrics import cross_entropy_logits, topk_accuracy, concord_index

                # Calculate loss using cross-entropy
                loss = cross_entropy_logits(output, target)
                
                # Calculate top-1 and top-5 accuracies
                top1, top5 = topk_accuracy(output, target, topk=(1, 5))
                
                # Calculate the concordance index
                ci = concord_index(y, y_pred)
                """,
                language="python"
            )

        with st.expander("🔗 Similarity and Uncertainty Measures"):
            st.write(
                """
                **Similarity and Uncertainty:**  
                These functions help compare predictions and understand model uncertainty.
                
                **Jaccard Similarity:**  
                Measures how similar two sets are.
                - **Parameters:**
                    - `list1:` Elements of the first set.
                    - `list2:` Elements of the second set.
                    
                **Evaluate Correlations:**  
                Compares groups of predictions and their associated uncertainty, helping you assess reliability.
                - **Parameters:**
                    - `bin_predictions:` A dictionary of predictions grouped into bins.
                    - `uncertainty_error_pairs:` A list of pairs showing uncertainty and error.
                    - `cmaps:` Color maps for visualizing results.
                    - `num_bins:` The number of bins to divide your data.
                    - `confidence_invert_tuples:` Tuples that specify if certain confidence values should be inverted.
                    - `num_folds (optional):` The number of folds for cross-validation (default is 8).
                    - `error_scaling_factor (optional):` Factor to scale the errors (default is 1).
                    - `combine_middle_bins (optional):` Whether to merge middle bins (default is False).
                    - `save_path (optional):` Where to save the results.
                    - `to_log (optional):` Whether to log the outcomes.
                """
            )
            st.code(
                """
                from kale.evaluate.similarity_metrics import jaccard_similarity, evaluate_correlations

                # Calculate Jaccard Similarity between two lists
                jaccard_index = jaccard_similarity(list1, list2)

                # Evaluate correlations between prediction bins and uncertainty/error pairs
                correlations = evaluate_correlations(bin_predictions, uncertainty_error_pairs, cmaps, num_bins, confidence_invert_tuples)
                """,
                language="python"
            )


    st.write("---")