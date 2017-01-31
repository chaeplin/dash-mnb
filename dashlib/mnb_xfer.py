import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from mnb_rpc import *


def broadcast_signedrawtx(mn_config, access):
    xfertxid = []
    for x in mn_config:
        alias = x.get('alias')
        signedrawtx = x.get('signedrawtx', None)
        if signedrawtx:

            print('\nverify tx for %s' % alias)
            for tx in signedrawtx:
                r = decoderawtransaction(tx, access)

                print(
                    json.dumps(
                        r.get('vout'),
                        sort_keys=True,
                        indent=4,
                        separators=(
                            ',',
                            ': ')))

                user_input = input(
                    '\nBroadcast signed raw tx ? [ Yes / (any key to no) ] + enter : ')
                if user_input == 'Yes':
                    print('\nYes, will broadcast')
                else:
                    print('\nNo.')
                    continue

                s = sendrawtransaction(tx, access)
                xfertxid.append(s)
                print('\n====> txid : %s\n' % s)

                collateral_txidtxidn = x.get('collateral_txidtxidn')

                unspent_cache_abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../cache/' + ('MAINNET' if MAINNET else 'TESTNET') + '-' + collateral_txidtxidn  + '-unspent.dat')
                open(unspent_cache_abs_path, 'w').close()


    if len(xfertxid) > 0:
        return xfertxid

    else:
        return None
