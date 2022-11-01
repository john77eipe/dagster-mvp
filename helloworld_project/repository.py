from dagster import load_assets_from_package_module, repository

from ops import hello_ops


@repository
def helloworld_project_repo():
    return hello_ops
