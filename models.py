from djongo import models


class Organization(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Role(models.Model):
    roller = models.CharField(max_length=50)

    def __str__(self):
        return self.roller


class OrganizasyonTutucu(models.Model):
    organizasyon = models.ForeignKey(Organization, on_delete=models.CASCADE)
    rol = models.ForeignKey(Role, on_delete=models.CASCADE)


class Customer(models.Model):
    name = models.CharField(max_length=50)
    organizations = models.ArrayModelField(
        model_container=OrganizasyonTutucu
    )
    text = models.TextField(max_length=50)

    def __str__(self):
        return self.name
