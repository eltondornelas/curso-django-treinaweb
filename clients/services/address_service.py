from ..models import Address


def register_address(address):
    # nesse caso é interessante retornar para armazenar na relação 1-1 pelo id
    return Address.objects.create(street=address.street, number=address.number,
                                  complement=address.complement,
                                  district=address.district, city=address.city,
                                  country=address.country)


def list_address_id(id):
    address = Address.objects.get(id=id)
    return address


def edit_address(address, new_address):
    address.street = new_address.street
    address.number = new_address.number
    address.complement = new_address.complement
    address.district = new_address.district
    address.city = new_address.city
    address.country = new_address.country

    address.save(force_update=True)


def remove_address(address):
    address.delete()
