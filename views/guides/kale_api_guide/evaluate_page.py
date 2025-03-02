
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
                **`leave_one_group_out`**: Performs leave-one-group-out cross-validation for a given estimator.
                - **Parameters**:
                    - `x`: Input data [n_samples, n_features].
                    - `y`: Target labels [n_samples].
                    - `groups`: Group labels to be left out [n_samples].
                    - `estimator`: Machine learning estimator to be evaluated from kale or scikit-learn.
                    - `use_domain_adaptation`: Whether to use domain adaptation during training.
                - **Returns**: A dictionary containing results for each target group with keys 'Target', 'Num_samples', and 'Accuracy'.
                """
            )
            st.code(
                """
                from kale.evaluate.cross_validation import leave_one_group_out

                results = leave_one_group_out(x, y, groups, estimator)
                """,
                language="python"
            )

        with st.expander("📏 Performance Metrics"):
            st.write(
                """
                **`cross_entropy_logits`**: Computes cross-entropy with logits.
                - **Parameters**:
                    - `output`: The output of the last layer of the network, before softmax.
                    - `target`: The ground truth label.
                    - `weights` (optional): The weight of each sample.

                **`topk_accuracy`**: Computes the top-k accuracy for specified values of k.
                - **Parameters**:
                    - `output`: The output of the last layer of the network, before softmax.
                    - `target`: The ground truth label.
                    - `topk`: Tuple specifying which top-k accuracies to compute.

                **`concord_index`**: Calculates the Concordance Index (CI), measuring the proportion of concordant pairs between real and predicted values.
                - **Parameters**:
                    - `y`: Real values.
                    - `y_pred`: Predicted values.
                """
            )
            st.code(
                """
                from kale.evaluate.metrics import cross_entropy_logits, topk_accuracy, concord_index

                loss = cross_entropy_logits(output, target)
                top1, top5 = topk_accuracy(output, target, topk=(1, 5))
                ci = concord_index(y, y_pred)
                """,
                language="python"
            )

        with st.expander("🔗 Similarity and Uncertainty Measures"):
            st.write(
                """
                **`jaccard_similarity`**: Calculates the Jaccard Index between two lists.
                - **Parameters**:
                    - `list1`: List of elements in set A.
                    - `list2`: List of elements in set B.

                **`evaluate_correlations`**: Evaluates correlations between binned predictions and uncertainty/error pairs.
                - **Parameters**:
                    - `bin_predictions`: Dictionary of binned predictions.
                    - `uncertainty_error_pairs`: List of tuples specifying uncertainty and error pairs.
                    - `cmaps`: List of colormaps for visualization.
                    - `num_bins`: Number of bins for quantization.
                    - `confidence_invert_tuples`: List of tuples specifying confidence measures and whether to invert them.
                    - `num_folds` (optional): Number of folds for cross-validation. Defaults to 8.
                    - `error_scaling_factor` (optional): Scaling factor for errors. Defaults to 1.
                    - `combine_middle_bins` (optional): Whether to combine middle bins. Defaults to False.
                    - `save_path` (optional): Path to save results. Defaults to None.
                    - `to_log` (optional): Whether to log results. Defaults to False.
                """
            )
            st.code(
                """
                from kale.evaluate.similarity_metrics import jaccard_similarity, evaluate_correlations

                jaccard_index = jaccard_similarity(list1, list2)
                correlations = evaluate_correlations(bin_predictions, uncertainty_error_pairs, cmaps, num_bins, confidence_invert_tuples)
                """,
                language="python"
            )


    st.write("---")