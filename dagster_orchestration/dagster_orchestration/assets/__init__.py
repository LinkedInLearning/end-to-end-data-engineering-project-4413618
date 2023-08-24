import os
from dagster_dbt import DbtCliClientResource
from dagster_dbt import load_assets_from_dbt_project
from dagster_airbyte import AirbyteResource
from dagster_airbyte import load_assets_from_airbyte_instance

resources = {
    "dbt": DbtCliClientResource(
        project_dir=os.getenv("DBT_PROJECT_DIR"),
        profiles_dir=os.getenv("DBT_PROFILES_DIR"),
    ),
    "airbyte_instance": AirbyteResource(
        host="localhost",
        port="8000",
        # If using basic auth, include username and password:
        username="airbyte",
        password=os.getenv("AIRBYTE_PASSWORD")
    )
}

dbt_assets = load_assets_from_dbt_project(
    project_dir=os.getenv("DBT_PROJECT_DIR"), profiles_dir=os.getenv("DBT_PROFILES_DIR"), key_prefix=["transformed_data"]
)

airbyte_assets = load_assets_from_airbyte_instance(
    resources.get("airbyte_instance"), key_prefix=["raw_data"])
