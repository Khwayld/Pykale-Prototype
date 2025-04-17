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
