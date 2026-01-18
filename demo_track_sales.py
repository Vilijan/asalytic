from asalytic.parsers.sale import ASASaleParser
from asalytic.indexers.indexer import AsalyticIndexerClient

headers = {
    "User-Agent": "Python3",
    'x-algo-api-token': "97FF4C15114EB2363614587242715E18"
}
asalytic_indexer = AsalyticIndexerClient(indexer_token="",
                                         indexer_address="https://mainnet-idx.4160.nodely.io",
                                         headers=headers)


BLOCK = 57474744

atomic_transfers = asalytic_indexer.block_atomic_transfers(block=BLOCK)

block_sales, unknown_ats = ASASaleParser.parse_atomic_transfers(atomic_transfers=atomic_transfers)

for sale in block_sales:
    print(f'asa_id={sale.asa_id} price={sale.price / 1e6} ALGO')