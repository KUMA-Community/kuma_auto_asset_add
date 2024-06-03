#!/usr/bin/python3

import argparse
import json
import os
from kumaPublicApiV1 import Kuma


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--asset', type=str, help='Asset info string. Format: IP|FQDN', required=True)
    parser.add_argument('--tenant', type=str, help='Tenant ID', required=True)
    args = parser.parse_args()

    asset = args.asset
    tenant = args.tenant
    asset_struct = {}

    index = asset.index('|')

    if index == 0:
        asset_struct.update(
            {
                "fqdn": asset[1:]
             }
        )
    elif index == len(asset)-1:
        asset_struct.update(
            {
                "ipAddresses": [asset[:-1]]
            }
        )
    else:
        asset_struct.update(
            {
                "fqdn": asset[index+1:],
                "ipAddresses": [asset[:index]]
            }
        )

    param_file_path = os.path.dirname(os.path.abspath(__file__)) + '/params.json'
    with open(param_file_path) as param_file:
        params = json.load(param_file)

    kuma = Kuma(params['kumaAddress'], params['kumaAPIPort'], params['kumaToken'])
    kuma.import_assets(tenant, [asset_struct])


if __name__ == "__main__":
    main()
