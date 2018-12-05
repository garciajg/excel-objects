from json import dumps

class Building(object):
    def __init__(self, **kwargs):
        self.date_added = kwargs["date_added"]
        self.occupancy = kwargs["occupancy"]
        self.lease_signed = kwargs["lease_signed"]
        self.building = kwargs["building"]
        self.building_class = kwargs["building_class"]
        self.city = kwargs["city"]
        self.deal_size = kwargs["deal_size"]
        self.tenant = kwargs["tenant"]
        self.new_renewal_expansion = kwargs["new_renewal_expansion"]
        self.term = kwargs["term"]
        self.base_rent = kwargs["base_rent"]
        self.rent_structure = kwargs["rent_structure"]
        self.esc = kwargs["esc"]
        self.t_i = kwargs["t_i"]
        self.rent_abatement = kwargs["rent_abatement"]
        self.tenant_broker = kwargs["tenant_broker"]
        self.ll_broker = kwargs["ll_broker"]
        self.t_o = kwargs["t_o"]
        self.comments = kwargs["comments"]

    @property
    def to_json(self):
        return self.__dict__
