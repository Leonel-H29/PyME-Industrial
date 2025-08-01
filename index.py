from MySME.mySME import MySME
from Items.enums.metric_unit_enum import MetricUnitEnum


def main():
    # Create main application
    mysme = MySME()

    # Create and save an supply
    supply = mysme.add_supply(
        "Tornillos XL",
        100,
        MetricUnitEnum.METER,
        "Juan Pérez",
        [
            "juan.perez@mipyme.com",
            "ramiro.pereyra@mipyme.com",
            "marcos.alvarez@mipyme.com",
            "leornardo_mirra@mipyme.com",
        ]
    )

    mysme.show_supplies()

    # Change supply status
    mysme.update_supply_status(supply.get_code(), 'quote')
    mysme.show_supplies()

    mysme.update_supply_status(supply.get_code(), 'order')
    mysme.show_supplies()

    # Display from database
    mysme.load_supplies()
    mysme.show_supplies()


if __name__ == '__main__':
    main()
