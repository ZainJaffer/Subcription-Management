class Subscription:
    def __init__(self,type,status,price,features):
        self.type = type
        self.status = status
        self.price = price
        self.features = features

    def cancel_subscription(self):
        pass

    def renew_subscription(self):
        pass

    def get_details(self):
        pass


class StreamingService(Subscription):
    def __init__(self, type, status, price, features, content_library_size):
        super().__init__(type, status, price, features)
        self.content_library_size = content_library_size
        
class PremiumContentService(Subscription):
    def __init__(self, type, status, price, features, exclusive_content_count):
        super().__init__(type, status, price, features)
        self.exclusive_content_count = exclusive_content_count

class CloudStorageService(Subscription):
    def __init__(self, type, status, price, features, storage_limit):
        super().__init__(type, status, price, features)
        self.storage_limit = storage_limit

class User():
    def __init__(self,name,subscriptions):
        self.name = name
        self.subscriptions = subscriptions

    def subscribe(self):
        pass

    def cancel_suscription(self):
        pass

    def renew_subscription(self):
        pass

    def list_subscriptions(self):
        pass


class SubscriptionService():
    def __init__(self, service_name, available_plans):
        self.service_name = service_name
        self.available_plans = available_plans

    def add_plan(self):
        pass

    def remove_plan(self):
        pass

    def get_plan_details(self):
        pass
