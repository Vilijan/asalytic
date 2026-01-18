from asalytic.parsers.sale import ASASaleParser
from asalytic.indexers.indexer import AsalyticIndexerClient
from asalytic.parsers.listing.AppListingsATParser import AppListingsATParser
from asalytic.parsers.listing.ApplicationsParser import ApplicationParser
from asalytic.models.algorand import Application

asalytic_indexer = AsalyticIndexerClient(indexer_token="",
                                         indexer_address="https://mainnet-idx.4160.nodely.dev")

BLOCK = 57548065

atomic_transfers, transactions = asalytic_indexer.block_atomic_transfers_with_txns(block=BLOCK)

potential_listings = AppListingsATParser.parse_atomic_transfers(atomic_transfers=atomic_transfers)

app_id_to_app: dict[int, Application] = {}

for potential_listing in potential_listings:

    try:
        app = asalytic_indexer.retrieve_application(app_id=potential_listing.app_id)

        app_id_to_app[app.id] = app
    except:
        pass


applications: list[Application] = list(app_id_to_app.values())

parsed_app_listings = ApplicationParser.parse_applications(applications=applications)

for listing in parsed_app_listings:
    print(f'asa_id={listing.asa_id} price={listing.price / 1e6} ALGO platform={listing.platform}')