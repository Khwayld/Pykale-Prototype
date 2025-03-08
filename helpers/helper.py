import streamlit as st
import torch

def display_frames_in_grid(frames, num_cols=3):
    """
    Helper function to display a list of frames (PIL images or arrays) in a grid layout.
    Each row has `num_cols` columns.
    """
    rows_needed = (len(frames) + num_cols - 1) // num_cols
    for row_idx in range(rows_needed):
        cols = st.columns(num_cols)
        for col_idx in range(num_cols):
            frame_index = row_idx * num_cols + col_idx
            if frame_index < len(frames):
                with cols[col_idx]:
                    st.markdown(
                        f"<h5 style='text-align: center;'>Frame {frame_index + 1}</h5>",
                        unsafe_allow_html=True
                    )
                    st.image(frames[frame_index], use_column_width=True)




def load_file(file_path: str) -> str:
    """Load a file from the given path and return as a string."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
    

# Taken directly from pykale/kale/evaluate/metrics.py
# This is because latest version on pypi does not include this function for some reason. 
def topk_accuracy(output, target, topk=(1,)):
    """Computes the top-k accuracy for the specified values of k.

    Args:
        output (Tensor): The output of the last layer of the network, before softmax. Shape: (batch_size, class_count).
        target (Tensor): The ground truth label. Shape: (batch_size)
        topk (tuple(int)): Compute accuracy at top-k for the values of k specified in this parameter.
    Returns:
        list(Tensor): A list of tensors of the same length as topk.
        Each tensor consists of boolean variables to show if this prediction ranks top k with each value of k.
        True means the prediction ranks top k and False means not.
        The shape of tensor is batch_size, i.e. the number of predictions.

    Examples:
        >>> output = torch.tensor(([0.3, 0.2, 0.1], [0.3, 0.2, 0.1]))
        >>> target = torch.tensor((0, 1))
        >>> top1, top2 = topk_accuracy(output, target, topk=(1, 2)) # get the boolean value
        >>> top1_value = top1.double().mean() # get the top 1 accuracy score
        >>> top2_value = top2.double().mean() # get the top 2 accuracy score
    """

    maxk = max(topk)

    # returns the k largest elements and their indexes of inputs along a given dimension.
    _, pred = output.topk(maxk, 1, True, True)

    pred = pred.t()
    correct = pred.eq(target.view(1, -1).expand_as(pred))

    result = []
    for k in topk:
        correct_k = torch.ge(correct[:k].float().sum(0), 1)
        result.append(correct_k)
    return result
