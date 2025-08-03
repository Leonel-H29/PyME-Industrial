from MySME.mySME import MySME
from Items.enums.metric_unit_enum import MetricUnitEnum


def main():
    mysme = MySME()

    # 1. Create multiple Supplies
    supply1 = mysme.add_supply(
        "Tornillos XL", 100, MetricUnitEnum.METER, "Juan Pérez",
        ["juan.perez@mipyme.com", "ramiro.pereyra@mipyme.com"]
    )
    supply2 = mysme.add_supply(
        "Tuercas L", 200, MetricUnitEnum.UNIT, "Ana Gómez",
        ["ana.gomez@mipyme.com", "marcos.alvarez@mipyme.com"]
    )

    # 2. Create multiple Third Party Services
    tps1 = mysme.add_third_party_service(
        service="Servicio de Mantenimiento",
        provider="Kousal S.A.",
        petitioner="Juan Carlos Cesar",
        user_emails=["juan.perez@mipyme.com", "leornardo_mirra@mipyme.com"]
    )
    tps2 = mysme.add_third_party_service(
        service="Transporte de Carga",
        provider="Logística S.R.L.",
        petitioner="María López",
        user_emails=["maria.lopez@mipyme.com", "ramiro.pereyra@mipyme.com"]
    )

    # 3. Display initial data
    print("\n--- Lista inicial de Supplies ---")
    mysme.show_supplies()
    print("\n--- Lista inicial de Third Party Services ---")
    mysme.show_third_party_services()

    # 4. Add an additional observer to a supply
    mysme.add_supply_observer(
        supply1.get_code(), "nuevo.observador@mipyme.com")
    print("\nSe agregó un observador adicional a Supply 1.")

    # 5. Change the status of items
    mysme.update_supply_status(supply1.get_code(), 'quote')
    mysme.update_supply_status(supply2.get_code(), 'quote')
    mysme.update_third_party_service_status(tps1.get_code(), 'quote')
    mysme.update_third_party_service_status(tps2.get_code(), 'quote')

    # 6. Display data after state changes
    print("\n--- Supplies después de cambios de estado ---")
    mysme.show_supplies()
    print("\n--- Third Party Services después de cambios de estado ---")
    mysme.show_third_party_services()

    # 7. Reload all lists from the database
    mysme.load_supplies()
    mysme.load_third_party_services()
    print("\n--- Listas recargadas desde la base de datos ---")
    mysme.show_supplies()
    mysme.show_third_party_services()

    # 8. Interacción con el usuario para cambiar estado de un Supply
    supply_id = input("\nIngrese el código del Supply que desea modificar: ")
    new_status = input("Ingrese el nuevo estado para el Supply: ")
    mysme.update_supply_status(supply_id, new_status)
    print("\nSupply actualizado:")
    mysme.show_supplies()

    # 8. User interaction to change the state of a Supply
    tps_id = input(
        "\nIngrese el código del Third Party Service que desea modificar: ")
    new_status_tps = input(
        "Ingrese el nuevo estado para el Third Party Service: ")
    mysme.update_third_party_service_status(tps_id, new_status_tps)
    print("\nThird Party Service actualizado:")
    mysme.show_third_party_services()

    # 9. User interaction to remove an observer from a Supply
    supply_id = input(
        "\nIngrese el código del Supply del cual desea eliminar un observador: ")
    observer_email = input(
        "Ingrese el email del observador que desea eliminar: ")
    mysme.remove_supply_observer(supply_id, observer_email)
    print("\nObservador eliminado del Supply.")
    mysme.show_supplies()

    # 10. User interaction to remove an observer from a third-party service
    tps_id = input(
        "\nIngrese el código del Third Party Service del cual desea eliminar un observador: ")
    observer_email_tps = input(
        "Ingrese el email del observador que desea eliminar: ")
    mysme.remove_third_party_service_observer(tps_id, observer_email_tps)
    print("\nObservador eliminado del Third Party Service.")
    mysme.show_third_party_services()

    # 11. Reload all lists from the database
    mysme.load_supplies()
    mysme.load_third_party_services()
    print("\n--- Listas recargadas desde la base de datos después de eliminar observadores ---")
    mysme.show_supplies()
    mysme.show_third_party_services()


if __name__ == '__main__':
    main()
