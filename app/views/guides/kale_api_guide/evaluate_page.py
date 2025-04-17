
import streamlit as st
from utils.helper_utils import load_file

from views.components.ui import (
    page_header,
    button_component,
    code_snippet_block
)

def evaluate_page():
    """KALE API - Model Evaluation (kale.evaluate)"""
    # Header
    page_header(
        title="📊 Model Evaluation - <code>kale.evaluate</code>",
        subtitle="""
        This module offers tools for assessing model performance, including metrics, cross-validation methods, and similarity measures.        
        """
    )
    
    button_component(
        button_text="🔙 Back to API Guide",
        slug="kale_api"
    )


    # Guide section
    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
        code_snippet_block(
            label="🔍 Cross-Validation Methods",
            write_up="""
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
            """,
            code=load_file("code_snippets/kale_api/evaluate/leave_one_group_out.py")
        )

        code_snippet_block(
            label="📏 Performance Metrics",
            write_up="""
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
            """,
            code=load_file("code_snippets/kale_api/evaluate/metric.py")
        )

        code_snippet_block(
            label="🔗 Similarity and Uncertainty Measures",
            write_up="""
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
            """,
            code=load_file("code_snippets/kale_api/evaluate/similarity.py")
        )