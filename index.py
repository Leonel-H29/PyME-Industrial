from MySME.mySME import MySME
from Items.enums.metric_unit_enum import MetricUnitEnum


def main():
    # Create main application
    mysme = MySME()

    # Create and save an supply
    supply = mysme.add_supply(
        "Tornillos",
        100,
        MetricUnitEnum.METER,
        "Juan Pérez",
        "juan.perez@mipyme.com"
    )

    mysme.show_supplies()

    # Create and save an external service
    tps = mysme.add_third_party_service(
        "Flete",
        "Transporte S.A.",
        "Ana López",
        "ana.lopez@mipyme.com"
    )

    mysme.show_third_party_services()

    # Change supply status
    mysme.update_supply_status(supply.get_code(), 'quote')
    mysme.show_supplies()

    # Change external service status
    mysme.update_third_party_service_status(tps.get_code(), 'order')
    mysme.show_third_party_services()

    # Display from database
    mysme.load_supplies()
    mysme.show_supplies()
    mysme.load_third_party_services()
    mysme.show_third_party_services()


if __name__ == '__main__':
    main()
