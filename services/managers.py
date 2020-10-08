from django.db import models

class ServiceManager(models.Manager):

    def services(self):
        return self.get_queryset().filter(
            service_type=self.model.ServiceType.SERVICE)

    def microservices(self):
        return self.get_queryset().filter(
            service_type=self.model.ServiceType.MICROSERVICE)


class OrderManager(models.Manager):

    def pending(self):
        return self.get_queryset().filter(status=self.model.Status.PENDING)

    def approved(self):
        return self.get_queryset().filter(status=self.model.Status.APPROVED)

    def in_progress(self):
        return self.get_queryset().filter(status=self.model.Status.IN_PROGRESS)

    def fulfilled(self):
        return self.get_queryset().filter(status=self.model.Status.FULFILLED)
