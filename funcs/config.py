import configparser
import os
from os.path import isfile


def read_config(filename: str) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(filename)
    return config


def check_config(config: configparser.ConfigParser) -> bool:
    if not config.has_section("VLC"):
        raise ValueError("No section \"VLC\" found.")

    if 'vlc_exec' not in config["VLC"]:
        raise ValueError("No key \"vlc_exec\" found.")

    if 'vlc_params' not in config["VLC"]:
        raise ValueError("No key \"vlc_params\" found.")
    
    if 'vlc_pid_filename' not in config["VLC"]:
        raise ValueError("No key \"vlc_pid_filename\" found.")

    if not os.path.exists(config["VLC"]["vlc_exec"]):
        raise FileNotFoundError("The VLC executable not found.")


def get_vlc_cmdline(config: configparser.ConfigParser) -> str:
    return " ".join([
                config["VLC"]["vlc_exec"],
                "--intf http",
                "--http-password",
                config["VLC"]["vlc_http_password"],
                "--http-host",
                config["VLC"]["vlc_host"],
                "--http-port",
                config["VLC"]["vlc_port"],
                config["VLC"]["vlc_params"]
             ])
