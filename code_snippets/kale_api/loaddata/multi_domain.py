from kale.loaddata.multi_domain import MultiDomainImageFolder

# Example: Initialize MultiDomainImageFolder with source and target paths
multi_domain_data = MultiDomainImageFolder(
    source_domains=["/path/to/source"],
    target_domains=["/path/to/target"]
)
train_loader = multi_domain_data.get_train()
