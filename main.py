import os
import sys
import argparse
import logging
import yaml
import torch
from runners.train import 


def parse_args_and_config():
    parser = argparse.ArgumentParser(description="Chem archive main script")
    parser.add_argument(
        "--config", type=str, required=True, help="Path to the config file"
    )
    parser.add_argument(
        "--seed", type=int, default=42, help="Random seed"
    )
    parser.add_argument(
        "--mode", type=str, default="train", choices=["train", "test", "sample"], help="Mode to run the script in"
    )
    parser.add_argument(
        "--gpu", type=str, default="0", help="GPU device to use"
    )
    
    args = parser.parse_args()
    
    os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu

    # parse config file
    with open(args.config, "r") as f:
        config = yaml.safe_load(f)
    new_config = dict2namespace(config)
    

    return args, new_config


def dict2namespace(config):
    namespace = argparse.Namespace()
    for key, value in config.items():
        if isinstance(value, dict):
            new_value = dict2namespace(value)
        else:
            new_value = value
        setattr(namespace, key, new_value)
    return namespace


def main():
    args, config = parse_args_and_config()


if __name__ == "__main__":
    main()