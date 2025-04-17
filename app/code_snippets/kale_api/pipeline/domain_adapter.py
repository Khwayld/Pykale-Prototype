from kale.pipeline.domain_adapter import DANNTrainer, CDANTrainer, WDGRLTrainer

# Initialize a DANN trainer
dann_trainer = DANNTrainer(feature_extractor=my_feature_extractor, task_classifier=my_task_classifier)

# Initialize a CDAN trainer
cdan_trainer = CDANTrainer(feature_extractor=my_feature_extractor, task_classifier=my_task_classifier)

# Initialize a WDGRL trainer
wdgrl_trainer = WDGRLTrainer(feature_extractor=my_feature_extractor, task_classifier=my_task_classifier)
