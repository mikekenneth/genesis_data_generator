import configparser


def get_section_credentials(ini: str, section: str, return_type: str = None):
    config = configparser.ConfigParser()
    config.read(ini)
    if section not in config.sections():
        return None
    if return_type and return_type == "config":
        return config
    return config[section]
