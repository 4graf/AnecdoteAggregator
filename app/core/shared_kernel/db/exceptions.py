class EntityExistsError(Exception):
    def __init__(self, msg='The entity already exists.'):
        super().__init__(msg)
