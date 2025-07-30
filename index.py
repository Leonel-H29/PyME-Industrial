from MySME.mySME import MySME
from Items.item import Item
from Items.enums.metric_unit_enum import MetricUnitEnum
from db.DBItems import DBItems
from User.user import User

# Agregar servicio para buscar item por id (y cambiar estado)

def main():
    # Create main application
    mysme = MySME()

    # Create an Item
    # By default, its status is 'Solicitado'
    item = mysme.add_supply(
        "Tornillos", 100, MetricUnitEnum.METER, "Juan Pérez", "juan.perez@mipyme.com")

    # Insert into the database
    mysme.save_supplies()

    # Show current supplies in memory
    mysme.show_supply()

    def changeStatus(item, status_method):
        try:
            mysme.change_item_status(item, status_method)
            mysme.update_supply(item)
            print(mysme.show_supply_from_db())
        except Exception as e:
            print(f"Error al cambiar de estado: {e}")

    # ==== Solicitado -> Cotizando
    changeStatus(item=item, status_method='quote')

    # ==== Cotizando -> Ordenado
    changeStatus(item=item, status_method='order')

    # ==== Ordenado -> Transportando
    changeStatus(item=item, status_method='transport')

    # ==== Transportando -> Recibido
    changeStatus(item=item, status_method='receive')

    # ==== Recibido -> Devuelto
    changeStatus(item, status_method='refund')


if __name__ == '__main__':
    main()
