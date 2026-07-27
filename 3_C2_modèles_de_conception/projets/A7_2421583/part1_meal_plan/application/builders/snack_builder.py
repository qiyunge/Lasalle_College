from __future__ import annotations


from .meal_plan_builder import MealPlanBuilder

class SnackBuilder(MealPlanBuilder):
    def build_selected_foods(self) -> None:
        self._meal_plan.selected_foods = ["Yogurt", "Granola Bar", "Fruit"]

    def build_dietary_preferences(self) -> None:
        self._meal_plan.dietary_preferences = ["Low Sugar", "Gluten-Free"]

    def build_portion(self) -> None:
        self._meal_plan.portions = {
            "Yogurt": "150 g",
            "Granola Bar": "1 bar",
            "Fruit": "1 piece"
        }

    def build_nutritional_analysis(self) -> None:
        self._meal_plan.nutritional_analysis = {
            "Calories": 250,
            "Protein": 8,
            "Carbohydrates": 35,
            "Fat": 7
        }