import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas

from torch.utils.data import DataLoader
from kale.loaddata.image_access import DigitDataset
from kale.prepdata.image_transform import get_transform
from kale.embed.image_cnn import SmallCNNFeature
from kale.predict.class_domain_nets import ClassNetSmallImage
from kale.pipeline.base_nn_trainer import CNNTransformerTrainer

from ml_core.models.base_model import BaseModel
from ml_core.registry import ModelRegistry


@ModelRegistry.register
class CNNTransformerModel(BaseModel):
    """"""
    name = "CNN Transformer"

    @classmethod
    def supported_datasets(cls):
        return ["MNIST_RGB", "USPS_RGB"]

    @classmethod
    def build(cls, max_epochs=3, **kwargs):
        return CNNTransformerTrainer(
            feature_extractor=SmallCNNFeature(),
            task_classifier=ClassNetSmallImage(),
            lr_gamma=0.1,
            lr_milestones=[1, max_epochs],
            max_epochs=max_epochs,
            optimizer={"type": "SGD", "optim_params": {"momentum": 0.9}},
            **kwargs,
        )

    @classmethod
    def load(cls, ckpt, max_epochs=3, **kwargs):
        model = CNNTransformerTrainer.load_from_checkpoint(
            checkpoint_path=ckpt,
            feature_extractor=SmallCNNFeature(),
            task_classifier=ClassNetSmallImage(),
            lr_gamma=0.1,
            lr_milestones=[1, max_epochs],
            optimizer=None,
            max_epochs=max_epochs,
            **kwargs,
        )
        model.eval()
        return model

    @classmethod
    def get_dataloader(cls):
        access, _ = DigitDataset.get_access(DigitDataset.MNIST_RGB, "data/digits", num_channels=3)

        train_ds = access.get_train()
        test_ds  = access.get_test()

        train_loader = DataLoader(
            train_ds,
            batch_size=32,
            shuffle=True,
            num_workers=2,
            pin_memory=True,
        )

        test_loader = DataLoader(
            test_ds,
            batch_size=32,
            shuffle=False,
            num_workers=2,
            pin_memory=True,
        )
        return train_loader, test_loader
    
    @classmethod
    def render_ui(cls, ckpt):
        col_left, col_center, col_right = st.columns([2,4,1])
        with col_center:
            st.subheader("Draw a digit (0 to 9)")

            canvas = st_canvas(
                background_color="black",  
                fill_color="white",
                stroke_color="white",
                stroke_width=15,
                height=280, width=280,
                key="digit_canvas",
            )

            if st.button("Predict"):
                img_arr = canvas.image_data

                pil = Image.fromarray(img_arr.astype("uint8"))
                tf  = get_transform("mnist32rgb", augment=False)
                x   = tf(pil).unsqueeze(0)
                net  = cls.load(ckpt)
                pred = net(x).argmax(1).item()
                
                st.image(pil.resize((112, 112)))
                st.write(f"Prediction: **{pred}**")
