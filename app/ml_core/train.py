import torch
import pytorch_lightning as pl
from ml_core.registry import ModelRegistry

def train_model(model_name, num_epochs=3):
    """
    Simple training loop using pytorch lightning.
    """
    Model = ModelRegistry.get(model_name)
    
    model = Model.build(model_name)
    train_loader, _ = Model.get_dataloader()
    
    trainer = pl.Trainer(
        devices=1 if torch.cuda.is_available() else "cpu",
        max_epochs=num_epochs,
        logger=False,
        enable_progress_bar=False
    )

    trainer.fit(model, train_loader)
    trainer.save_checkpoint("model.ckpt")
    return model
