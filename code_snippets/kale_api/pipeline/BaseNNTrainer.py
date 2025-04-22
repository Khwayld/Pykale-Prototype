from kale.pipeline.base_nn_trainer import BaseNNTrainer

# Initialize the trainer with desired parameters
trainer = BaseNNTrainer(optimizer=my_optimizer, max_epochs=50, init_lr=0.001)

# Example usage:
# Assume 'model' is a neural network model and 'data_loader' is a data loader
trainer.fit(model, data_loader)
