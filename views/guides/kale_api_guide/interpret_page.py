
import streamlit as st
from navigation import go_to


def interpret_page():
    """KALE API - Model Interpretation (kale.interpret)"""

    # --- Page Header ---
    st.markdown(
        """
        <div style="text-align:center;">
            <h2>🔍 Model Interpretation - <code>kale.interpret</code></h2>
            <p style="font-size:18px;">
                This module provides tools for interpreting machine learning models, including functions for analyzing model weights, quantifying uncertainty, and visualizing results.
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

    # --- Overview Section ---
    st.markdown(
        """
        <div style="text-align:center;">
            <h3>🔹 Overview</h3>
            <p>
                The <code>kale.interpret</code> module offers functionalities to interpret and understand machine learning models, focusing on:
                <ul>
                    <li>⚖️ Analyzing model weights</li>
                    <li>📏 Quantifying uncertainties</li>
                    <li>🖼️ Visualizing data and model outputs</li>
                </ul>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("---")


    # --- Expandable Sections ---

    col1, col2, col3 = st.columns([1, 3, 1])  
    with col2:
        with st.expander("⚖️ Model Weights Analysis"):
            st.write(
                """
                **`select_top_weight`**: Selects the top weights in magnitude from the model, setting the rest to zero.
                - **Parameters**:
                    - `weights`: Model weights, can be a vector or a higher-order tensor.
                    - `select_ratio` (optional): Ratio of top weights to be selected. Defaults to 0.05.
                - **Returns**: Array-like structure with top weights in the same shape as the input model weights.
                """
            )
            st.code(
                """
                from kale.interpret.model_weights import select_top_weight

                # Example usage:
                top_weights = select_top_weight(weights, select_ratio=0.05)
                """,
                language="python"
            )


        with st.expander("📏 Uncertainty Quantification"):
            st.write(
                """
                **`fit_line_with_ci`**: Calculates Spearman correlation between errors and uncertainties, plotting piecewise linear regression with bootstrap confidence intervals.
                - **Parameters**:
                    - `errors`: Array of errors.
                    - `uncertainties`: Array of uncertainties.
                    - `quantile_thresholds`: List of quantile thresholds.
                    - `cmaps`: List of colormap names.
                    - `to_log` (optional): Whether to apply logarithmic transformation on axes. Defaults to False.
                    - `error_scaling_factor` (optional): Scaling factor for error. Defaults to 1.0.
                    - `save_path` (optional): Path to save the plot; if None, the plot will be shown. Defaults to None.
                - **Returns**: Dictionary containing Spearman and Pearson correlation coefficients and p-values.

                **`quantile_binning_and_est_errors`**: Calculates quantile thresholds, performs isotonic regression on errors and uncertainties, and estimates error bounds.
                - **Parameters**:
                    - `errors`: List of errors.
                    - `uncertainties`: List of uncertainties.
                    - `num_bins`: Number of quantile bins.
                    - `type` (optional): Type of thresholds to calculate; "quantile" recommended. Defaults to "quantile".
                    - `acceptable_thresh` (optional): Acceptable threshold for errors. Defaults to 5.
                    - `combine_middle_bins` (optional): Whether to combine middle bins. Defaults to False.
                - **Returns**: Tuple containing a list of lists of errors per bin and a list of estimated errors per bin.
                """
            )

            st.code(
                """
                from kale.interpret.uncertainty_quantiles import fit_line_with_ci, quantile_binning_and_est_errors

                # Example usage:
                correlations = fit_line_with_ci(errors, uncertainties, quantile_thresholds, cmaps)
                binned_errors, estimated_errors = quantile_binning_and_est_errors(errors, uncertainties, num_bins=10)
                """,
                language="python"
            )


        with st.expander("🖼️ Visualization Tools"):
            st.write(
                """
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
                """
            )

            st.code(
                """
                from kale.interpret import visualize

                # Example usage of plot_weights:
                fig = visualize.plot_weights(weight_img, background_img=None, color_marker_pos='rs', color_marker_neg='gs')
                fig.show()

                # Example usage of plot_multi_images:
                fig = visualize.plot_multi_images(images, n_cols=3, marker_locs=marker_locs, marker_titles=marker_titles)
                fig.show()

                # Example usage of distplot_1d:
                fig = visualize.distplot_1d(data, labels=labels, xlabel='X-axis', ylabel='Y-axis', title='1D Distribution')
                fig.show()
                """,
                language="python"
            )


    st.write("---")