
import streamlit as st
from utils.helper_utils import load_file

from views.components.ui import (
    info_card,
    page_header,
    button_component,
    code_snippet_block
)

def interpret_page():
    """KALE API - Model Interpretation (kale.interpret)"""
    # Header
    page_header(
        title="🔍 Model Interpretation - <code>kale.interpret</code>",
        subtitle="""
        This module provides tools for interpreting machine learning models, including functions for analyzing model weights, quantifying uncertainty, and visualizing results.        
        """
    )
    
    button_component(
        button_text="🔙 Back to API Guide",
        slug="kale_api"
    )



    # Overview
    info_card(
        title="🔹 Overview",
        subtitle="The <code>kale.interpret</code> module helps you make sense of your model by:",
        bullets=[
            "⚖️ Analyzing model weights to see which parts are most important",
            "📏 Quantifying uncertainties to understand prediction confidence",
            "🖼️ Visualizing data and model outputs for easier interpretation"
        ]
    )

    # Guide section
    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
        code_snippet_block(
            label="⚖️ Model Weights Analysis",
            write_up="""
            **`select_top_weight`** picks out the largest (most important) weights from your model and sets the rest to zero.
            
            **Parameters:**
            - **weights:** The weights from your model (can be a simple vector or more complex tensor).
            - **select_ratio (optional):** The fraction of weights to keep (default is 0.05).
            
            **Returns:**  
            The selected top weights in the same shape as the input.
            """,
            code=load_file("code_snippets/kale_api/interpret/top_weight.py")
        )

        code_snippet_block(
            label="📏 Uncertainty Quantification",
            write_up="""
            **`fit_line_with_ci`** helps you understand how errors and uncertainties relate by:
            - Calculating correlations (using Spearman and Pearson methods).
            - Plotting a line with confidence intervals using a bootstrap method.
            
            **Parameters:**
            - **errors:** The difference between predicted and actual values.
            - **uncertainties:** The uncertainty values of predictions.
            - **quantile_thresholds:** Thresholds for splitting your data.
            - **cmaps:** Names of color maps for plotting.
            - **to_log (optional):** Apply a logarithmic scale to axes (default False).
            - **error_scaling_factor (optional):** Scale errors (default 1.0).
            - **save_path (optional):** Where to save the plot (if not provided, the plot is shown).
            
            **Returns:**  
            A dictionary with correlation coefficients and p-values.
            
            **`quantile_binning_and_est_errors`** splits your errors and uncertainties into bins,
            applies isotonic regression, and estimates error bounds.
            
            **Parameters:**
            - **errors:** List of errors.
            - **uncertainties:** List of uncertainties.
            - **num_bins:** Number of bins to create.
            - **type (optional):** Type of threshold ("quantile" is recommended).
            - **acceptable_thresh (optional):** Acceptable error threshold (default is 5).
            - **combine_middle_bins (optional):** Merge middle bins (default False).
            
            **Returns:**  
            A tuple with binned errors and estimated error bounds.
            """,
            code=load_file("code_snippets/kale_api/interpret/uncertainty_quantiles.py")
        )

        code_snippet_block(
            label="🖼️ Visualization Tools",
            write_up="""
            **`plot_weights`**: Visualizes model weights.
            
            - **Parameters**:
                - `weight_img`: Model weights or coefficients in 2D.
                - `background_img` (optional): 2D background image. Defaults to None.
                - `color_marker_pos` (optional): Color and marker for positive weights. Defaults to red "rs".
                - `color_marker_neg` (optional): Color and marker for negative weights. Defaults to blue "gs".
                - `im_kwargs` (optional): Keyword arguments for background images. Defaults to None.
                - `marker_kwargs` (optional): Keyword arguments for markers. Defaults to None.
            
            - **Returns**: Matplotlib figure object.

            **`plot_multi_images`**: Plots multiple images with markers in one figure.
            
            - **Parameters**:
                - `images`: Images to plot, shape (n_samples, dim1, dim2).
                - `n_cols` (optional): Number of columns for plotting multiple images. Defaults to 1.
                - `n_rows` (optional): Number of rows for plotting multiple images. If None, n_rows = n_samples / n_cols.
                - `marker_locs` (optional): Locations of markers, shape (n_samples, 2 * n_markers). Defaults to None.
                - `marker_titles` (optional): Names of the markers, where len(marker_names) == n_markers. Defaults to None.
                - `marker_cmap` (optional): Name of the color map used for plotting markers. Defaults to None.
                - `image_titles` (optional): List of titles for each image, where len(image_names) == n_samples. Defaults to None.
                - `figsize` (optional): Figure size. Defaults to None.
                - `im_kwargs` (optional): Keyword arguments for plotting images. Defaults to None.
                - `marker_kwargs` (optional): Keyword arguments for markers. Defaults to None.
                - `legend_kwargs` (optional): Keyword arguments for legend. Defaults to None.
                - `title_kwargs` (optional): Keyword arguments for title. Defaults to None.
            
            - **Returns**: Matplotlib figure object.

            **`distplot_1d`**: Plots distribution of 1D data.
            
            - **Parameters**:
                - `data`: Data to plot.
                - `labels` (optional): List of labels for each data. Defaults to None.
                - `xlabel` (optional): Label for the x-axis. Defaults to None.
                - `ylabel` (optional): Label for the y-axis. Defaults to None.
                - `title` (optional): Title for the plot. Defaults to None.
                - `figsize` (optional): Figure size. Defaults to None.
                - `im_kwargs` (optional): Keyword arguments for plotting images. Defaults to None.
            
            - **Returns**: Matplotlib figure object.
            """,
            code=load_file("code_snippets/kale_api/interpret/visualize.py")
        )

