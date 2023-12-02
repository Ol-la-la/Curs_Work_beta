from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT_PATH.joinpath("data")
OPERATIONS_PATH = DATA_PATH.joinpath("operations.xls")

ROOT_PATH_SOURCE = Path(__file__).resolve().parent.parent
USER_JSON_PATH = ROOT_PATH_SOURCE.joinpath("user_settings.json")

