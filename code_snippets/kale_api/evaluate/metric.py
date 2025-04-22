from kale.evaluate.metrics import cross_entropy_logits, topk_accuracy, concord_index

# Calculate loss using cross-entropy
loss = cross_entropy_logits(output, target)

# Calculate top-1 and top-5 accuracies
top1, top5 = topk_accuracy(output, target, topk=(1, 5))

# Calculate the concordance index
ci = concord_index(y, y_pred)
