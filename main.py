class Subscription:
    def __init__(self,type,status,price,features):
        self.type = type
        self.status = status
        self.status = price
        self.features = features

    def cancel_subscription(self):
        pass

    def renew_subscription(self):
        pass

    def get_details(self):
        pass


class StreamingService(Subscription):
    pass
        
class PremiumContentService(Subscription):
    pass

class CloudStorageService(Subscription):
    pass

class User():
    def __init__(self,name,subscriptions):
        self.name = name
        self.subscriptions = subscriptions

    def subscribe():
        pass

    def cancel_suscription():
        pass

    def renew_subscription():
        pass

    def list_subscriptions():
        pass


class SubscriptionService():
    def __init__(self, service_name, available_plans):
        self.service_name = service_name
        self.available_plans = available_plans

    def add_plan():
        pass

    def remove_plan():
        pass

    def get_plan_details():
        pass
    