from project.peaks.base_peak import BasePeak



class ArcticPeak(BasePeak):

    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear():
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]
    
    def calculate_difficulty_level(self):
        if self.elevation > 3000:
            return "Extreme"
        elif 2000 <= self.elevation <= 3000:
            return "Advanced"

