def parse_version(v: str) -> tuple[int, int, int]: ...
def sqlalchemy_version(op: str, val: str) -> bool: ...
def engine_config_warning(config, version: str, deprecated_config_key: str, engine_option) -> None: ...