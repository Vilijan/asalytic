from asalytic.parsers.sale import ASASaleParser
from asalytic.indexers.indexer import AsalyticIndexerClient


asalytic_indexer = AsalyticIndexerClient(indexer_token="",
                                         indexer_address="https://mainnet-idx.4160.nodely.dev")


BLOCK = 57474744

atomic_transfers = asalytic_indexer.block_atomic_transfers(block=BLOCK)

block_sales, unknown_ats = ASASaleParser.parse_atomic_transfers(atomic_transfers=atomic_transfers)

for sale in block_sales:
    print(f'asa_id={sale.asa_id} price={sale.price / 1e6} ALGO')