from dagster import load_assets_from_package_module, repository
from dagster import repository, with_resources
from cereal_project import assets

all_assets = [*assets]

@repository
def cereal_project_repo():
    definitions = [
        with_resources(all_assets),
    ]
    return definitions
