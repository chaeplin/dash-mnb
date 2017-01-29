# config.py

# start of config
# network
#MAINNET = True  # mainnet
MAINNET = False  # testnet

# https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki
# purpose' / coin_type' / account' / change / address_index
# Dash  : 44'/5'/account'/0/0
# tDash : 44'/165'/account'/0/0
# bip32 path 
# 10 selected randomly
account_no = 10

#
if MAINNET:
    # HW WALLET TYPE
    TYPE_HW_WALLET = 'Trezor'          # Keepkey [ keepkey ], Trezor [ trezor ]

    # rpc
    rpcuser     = 'xxxx'
    rpcpassword = 'xxxxx'
    rpcbindip   = '127.0.0.1'
    rpcport     = 9998

    # ssh tunnel
    USE_SSH_TUNNEL   = True  # True or False
    SSH_IDENTITYFILE = '~/.ssh/xxxx.pem'
    SSH_USER         = 'xxxx'
    SSH_SERVER       = '10.10.10.10'
    SSH_LOCAL_PORT   = '29998'

    # masternode_config
    masternode_conf_file = 'mnconf/masternode.mainnet.conf'

    # default address to send coins in hw wallet if reveiving_address in masternode.conf is blank
    # this is not chaing payment address of mn
    default_receiving_address = ''

    # dash mainnet
    wif_prefix  = 204  # cc
    addr_prefix = 76   # 4c
    coin_name   = 'Dash'
    # don't change 


else:
    # HW WALLET TYPE
    TYPE_HW_WALLET = 'Keepkey'          # Keepkey [ keepkey ], Trezor [ trezor ]

    # rpc
    rpcuser     = 'xxxx'
    rpcpassword = 'xxxxx'
    rpcbindip   = '127.0.0.1'
    rpcport     = 19998

    # ssh tunnel
    USE_SSH_TUNNEL   = True  # True or False
    SSH_IDENTITYFILE = '~/.ssh/xxxx.pem'
    SSH_USER         = 'xxxx'
    SSH_SERVER       = '10.10.10.10'
    SSH_LOCAL_PORT   = '39998'

    # masternode_config
    masternode_conf_file = 'mnconf/masternode.testnet.conf'

    # default address to send coins in hw wallet if reveiving_address in masternode.conf is blank
    # this is not chaing payment address of mn
    default_receiving_address = 'yNYJy9ShtJWo2NFcT7sjRa2ucktTFFe71b' 

    # dash testnet
    wif_prefix  = 239 # ef
    addr_prefix = 140 # 8c
    coin_name   = 'tDash'
    # don't change 

#
min_fee     = 10000  # fee for tx

max_gab     = 20     # number of keys used on mn config

max_amounts = 50     # max amounts of each unspent tx 
max_unspent = 20
min_unspent = 1

#
errorsnprogress = []

# caution this config move 1K collateral to configured address with fee 0.0001
# destroy mode ><
MOVE_1K_COLLATERAL = False
# end of config.py
