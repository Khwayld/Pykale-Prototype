from helpers.constants import PRIMARY_COLOR
import streamlit as st
from utils.video_utils import demo_1, demo_2, demo_3, demo_4
from navigation import go_to

def video_demo_page():    
    """
    A step-by-step tutorial demonstrating how PyKale loads and transforms video frames.
    """

    col_left, col_mid, col_right = st.columns([1, 4, 1])


    # ----------------------------------------------------------------------------
    # 1. INTRO & PAGE HEADER
    # ----------------------------------------------------------------------------
    with col_mid:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <h1>📽️ Video Loading with PyKale (Step by Step)</h1>
                <p style="font-size:16px; max-width:700px; margin:auto;">
                    Explore how PyKale efficiently loads, samples, and transforms video frames for analysis.
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )


        col_left, col_center, col_right = st.columns([3, 1.5, 3])
        with col_center:
            if st.button("🔙 Back to Hub"):
                go_to("hub")

        st.markdown("---")


    # ----------------------------------------------------------------------------
    # 2. CODE SECTIONS & EXPLANATIONS
    # ----------------------------------------------------------------------------
    
    
    # --- Demo 1: Basic Video Loading without Transforms ---
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{PRIMARY_COLOR};'>1. Basic Video Loading without Transforms</h2>",
            unsafe_allow_html=True
        )

        st.write(
            """
            This demo shows how to load a video sample using PyKale's `VideoFrameDataset` without any preprocessing.
            We set up the dataset to perform sparse sampling (e.g., 5 segments with 1 frame each). The output is a list
            of frames and a corresponding label.
            """
        )

        with st.expander("Show code"):
            st.code("""
              from kale.loaddata.videos import VideoFrameDataset

              # Create a VideoFrameDataset instance without applying any transforms
              dataset = VideoFrameDataset(
                  root_path=videos_root,                # Path to your video frames directory
                  annotationfile_path=annotation_file,   # Path to the annotations file
                  num_segments=5,                        # Divide each video into 5 segments
                  frames_per_segment=1,                  # Extract 1 frame per segment (sparse sampling)
                  imagefile_template="img_{:05d}.jpg",
                  transform=None,                        # No preprocessing transforms
                  random_shift=True,
                  test_mode=False,
              )
                    
              # Retrieve the first video sample
              sample = dataset[0]
              frames = sample[0]  # List of PIL images
              label = sample[1]   # Video label (integer)
            """)

        st.markdown("---")

    # --- Demo 2: Continuous Frame Loading without Transforms ---
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{PRIMARY_COLOR};'>2. Continuous Frame Loading without Transforms</h2>",
            unsafe_allow_html=True
        )

        st.write(
            """
            This demo demonstrates how to load a continuous block of frames from a video.
            By setting `num_segments` to 1 and increasing `frames_per_segment` (e.g. to 9),
            we retrieve a contiguous clip starting from a random index. This is useful when
            a continuous motion sequence is desired.
            """
        )

        with st.expander("Show code"):
            st.code("""
            from kale.loaddata.videos import VideoFrameDataset

            # Create a VideoFrameDataset instance for continuous frame loading
            dataset = VideoFrameDataset(
                root_path=videos_root,
                annotationfile_path=annotation_file,
                num_segments=1,         # Single segment to enforce continuity
                frames_per_segment=9,   # Load 9 consecutive frames
                imagefile_template="img_{:05d}.jpg",
                transform=None,         # No transforms applied
                random_shift=True,
                test_mode=False,
            )

            # Retrieve a sample (using a different index for variety)
            sample = dataset[1]
            frames = sample[0]  # List of 9 consecutive frames
            label = sample[1]   # Video label
            """)
        st.markdown("---")

    # --- Demo 3: Video Loading with Preprocessing Transforms ---
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{PRIMARY_COLOR};'>3. Video Loading with Preprocessing Transforms</h2>",
            unsafe_allow_html=True
        )


        col_left, col_center, col_right = st.columns([0.5, 4, 0.1])
        with col_center:
            st.write(
                """
                Preprocessing is often required before feeding video data into a deep learning model.
                In this demo, we define a transform pipeline using torchvision's transforms to:
                - Convert a list of PIL images into a tensor,
                - Resize images (scaling the smaller edge to 299 pixels),
                - Center crop them to 299x299,
                - Normalize the pixel values with ImageNet statistics.
                The result is a preprocessed video tensor ready for model input.
                """
            )

        with st.expander("Show code"):
            st.code("""
            import torchvision.transforms as transforms
            from kale.prepdata.video_transform import ImglistToTensor
            from kale.loaddata.videos import VideoFrameDataset

            # Define the preprocessing pipeline for video frames
            preprocess = transforms.Compose([
                ImglistToTensor(),          # Convert list of PIL images to tensor: (Frames x Channels x Height x Width)
                transforms.Resize(299),     # Resize so that the smaller edge is 299 pixels
                transforms.CenterCrop(299), # Center crop to 299x299 dimensions
                transforms.Normalize(       # Normalize using ImageNet mean and std
                    mean=[0.485, 0.456, 0.406],
                    std=[0.229, 0.224, 0.225]
                ),
            ])

            # Create a VideoFrameDataset instance with the preprocessing transforms
            dataset = VideoFrameDataset(
                root_path=videos_root,
                annotationfile_path=annotation_file,
                num_segments=5,             # Sparse sampling: 5 segments
                frames_per_segment=1,       # 1 frame per segment
                imagefile_template="img_{:05d}.jpg",
                transform=preprocess,       # Apply the defined preprocessing pipeline
                random_shift=True,
                test_mode=False,
            )

            # Retrieve a sample and obtain the preprocessed video tensor
            sample = dataset[1]
            frame_tensor = sample[0]  # Tensor shape: (NUM_SEGMENTS * FRAMES_PER_SEGMENT x Channels x Height x Width)
            label = sample[1]
            """)
        st.markdown("---")


    # --- Demo 4: Multi-Label Example ---
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{PRIMARY_COLOR};'>4. Multi-Label Video Loading</h2>",
            unsafe_allow_html=True
        )

        st.write(
            """
            Some video datasets assign multiple labels to a single video clip (e.g., verb, noun, action).
            This demo shows how `VideoFrameDataset` can handle such multi-label scenarios.
            Here, the annotation file contains multiple label IDs per sample, and the dataset returns a tuple of labels.
            When using a DataLoader, the labels are returned as a tuple of tensors (one per label).
            """
        )

        with st.expander("Show code"):
            st.code("""
            import torch
            from kale.loaddata.videos import VideoFrameDataset

            # Create a VideoFrameDataset instance for a multi-label dataset using the same preprocessing pipeline
            dataset = VideoFrameDataset(
                root_path=videos_root,
                annotationfile_path=annotation_file,
                num_segments=5,
                frames_per_segment=1,
                imagefile_template="img_{:05d}.jpg",
                transform=preprocess,  # You can use the same transform as before
                random_shift=True,
                test_mode=False,
            )

            # Create a DataLoader to handle batching (this example uses a batch size of 3)
            dataloader = torch.utils.data.DataLoader(
                dataset=dataset,
                batch_size=3,
                shuffle=True,
                num_workers=2,
                pin_memory=True,
            )

            # Iterate through one batch to inspect the multi-label output
            for batch in dataloader:
                video_batch, labels = batch
                    
                # 'labels' is expected to be a tuple of tensors, e.g., (labels1, labels2, labels3)
                labels1, labels2, labels3 = labels
                break
            """)
        st.markdown("---")

    # --------------------------------------------------------------------
    # 3) INTERACTIVE DEMO
    # --------------------------------------------------------------------
    with col_mid:
        st.markdown(
            f"<h2 style='text-align:center; color:{PRIMARY_COLOR};'>Interactive Demo</h2>",
            unsafe_allow_html=True
        )

        st.write(
            """
            Now that we've explained each demo, try running one below!
            Each option corresponds to the demos described above:
            """
        )

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
          demo_option = st.radio(
              "",
              ["**Basic Video Loading** (sparse sampling)", "**Continuous Frame Loading** (contiguous clip)", "**Video Loading with Transforms** (preprocessing for model input)", "**Multi-Label Loading** (handling multiple labels per clip)"],
              label_visibility="collapsed",
              index=None,
              horizontal=False
          )
        

        st.markdown("---")
        
        if demo_option == "**Basic Video Loading** (sparse sampling)":
            demo_1()
        elif demo_option == "**Continuous Frame Loading** (contiguous clip)":
            demo_2()
        elif demo_option == "**Video Loading with Transforms** (preprocessing for model input)":
            demo_3()
        elif demo_option == "**Multi-Label Loading** (handling multiple labels per clip)":
            demo_4()

    # --------------------------------------------------------------------
    # 4) Summary
    # --------------------------------------------------------------------
    with col_mid:
        st.markdown(
            f"""
            <div style="text-align: center; max-width: 700px; margin:auto;">
                <h2 style="color:{PRIMARY_COLOR};">Summary & Next Steps</h2>
                <ul style="display:inline-block; text-align:left; padding: 0; margin: 0;">
                    <li><strong>Sparse Sampling:</strong> Efficiently extracts key frames, reducing computational load while capturing essential video content.</li>
                    <li><strong>Continuous Clips:</strong> Retrieves a contiguous sequence of frames to capture motion dynamics and context.</li>
                    <li><strong>Preprocessing Pipeline:</strong> Transforms raw frames into model-ready tensors via resizing, cropping, and normalization.</li>
                    <li><strong>Multi-Label Handling:</strong> Supports video samples with multiple labels, enabling more complex annotation tasks.</li>
                </ul>
                <p style="margin-top: 10px;">
                    Experiment with these techniques to see how different sampling strategies and preprocessing steps can improve your model's performance.
                    Adjust hyperparameters and customize the transforms to suit your dataset.
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )

