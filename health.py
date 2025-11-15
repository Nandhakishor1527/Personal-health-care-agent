class Health:
    def __init__(self):
        self.data = {}

    def add_data(self, key, value):
        self.data[key] = value

    def get_data(self):
        return self.data

    def get_recommendations(self, user):
        # Simple recommendation logic based on user data
        recommendations = []
        if 'weight' in user.get_profile() and user.get_profile()['weight'] > 70:
            recommendations.append('Consider reducing your weight')
        if 'blood_pressure' in self.data and self.data['blood_pressure'] > 120:
            recommendations.append('Consider reducing your blood pressure')
        return recommendations