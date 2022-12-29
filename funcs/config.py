import configparser
import os


def read_config(filename: str) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(filename)
    return config


def check_config(config: configparser.ConfigParser) -> bool:
    # DATABASE
    if not config.has_section("DATABASE"):
        raise ValueError("No section \"DATABASE\" found.")

    if 'exec' not in config["DATABASE"]:
        raise ValueError("No key \"connection\" found.")

    # VLC
    if not config.has_section("VLC"):
        raise ValueError("No section \"VLC\" found.")

    if 'exec' not in config["VLC"]:
        raise ValueError("No key \"exec\" found.")

    if 'params' not in config["VLC"]:
        raise ValueError("No key \"params\" found.")
    
    if 'pid_filename' not in config["VLC"]:
        raise ValueError("No key \"pid_filename\" found.")

    if not os.path.exists(config["VLC"]["exec"]):
        raise FileNotFoundError("The VLC executable not found.")


def get_vlc_cmdline(config: configparser.ConfigParser) -> str:
    return " ".join([
                config["VLC"]["exec"],
                "--intf http",
                "--http-password",
                config["VLC"]["http_password"],
                "--http-host",
                config["VLC"]["host_listen"],
                "--http-port",
                config["VLC"]["port"],
                config["VLC"]["params"],
                config["VLC"]["sout"]
             ])

def get_database_connection_string(config: configparser.ConfigParser) -> str:
    return config["DATABASE"]["connection"]