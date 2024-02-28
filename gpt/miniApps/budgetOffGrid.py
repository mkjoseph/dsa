# Define a class for the OffGridTinyHouseCalculator to encapsulate the calculator logic
class OffGridTinyHouseCalculator:
    def __init__(self):
        # Initialize default costs; these could be adjusted based on more accurate or current data
        self.tiny_house_cost_per_sqft = 150  # Example cost per square foot
        self.land_cost = 0  # Default, assuming no land purchase initially
        self.solar_panel_cost = 10000  # Example flat cost for a basic solar setup
        self.water_system_cost = 5000  # Example cost for water system setup
        self.septic_system_cost = 8000  # Example cost for septic system
        self.additional_features_cost = 0  # Placeholder for additional costs

    def calculate_total_cost(self, sqft, include_land, land_cost, include_solar, include_water, include_septic, additional_features_cost):
        # Calculate the base cost for the tiny house
        tiny_house_base_cost = self.tiny_house_cost_per_sqft * sqft

        # Adjust costs based on user selections
        if not include_land:
            self.land_cost = 0
        else:
            self.land_cost = land_cost

        if not include_solar:
            self.solar_panel_cost = 0

        if not include_water:
            self.water_system_cost = 0

        if not include_septic:
            self.septic_system_cost = 0

        self.additional_features_cost = additional_features_cost

        # Calculate total cost
        total_cost = (tiny_house_base_cost + self.land_cost + self.solar_panel_cost +
                      self.water_system_cost + self.septic_system_cost + self.additional_features_cost)
        return total_cost

    def display_cost_breakdown(self, sqft, include_land, include_solar, include_water, include_septic, additional_features_cost):
        # Calculate total cost and get the breakdown
        total_cost = self.calculate_total_cost(sqft, include_land, self.land_cost, include_solar, include_water, include_septic, additional_features_cost)

        # Display the breakdown
        print(f"Cost Breakdown for Your Off-Grid Tiny House:")
        print(f"Tiny House Base Cost (for {sqft} sqft): ${self.tiny_house_cost_per_sqft * sqft}")
        if include_land:
            print(f"Land Cost: ${self.land_cost}")
        if include_solar:
            print(f"Solar Panel System Cost: ${self.solar_panel_cost}")
        if include_water:
            print(f"Water System Cost: ${self.water_system_cost}")
        if include_septic:
            print(f"Septic System Cost: ${self.septic_system_cost}")
        print(f"Additional Features Cost: ${self.additional_features_cost}")
        print(f"Total Cost: ${total_cost}")

# Note: Function calls and method calls are commented out to comply with the instructions for development within the PCI.
# The following lines would be used to create an instance of the calculator and test it with example inputs:
# calculator = OffGridTinyHouseCalculator()
# calculator.display_cost_breakdown(sqft=300, include_land=True, include_solar=True, include_water=True, include_septic=True, additional_features_cost=2000)
