from __future__ import annotations

from .meal_plan_builder import MealPlanBuilder

class LunchBuilder(MealPlanBuilder):
    def build_selected_foods(self) -> None:
        self._meal_plan.selected_foods = ["Chicken Salad", "Fruit Juice", "Bread"]

    def build_dietary_preferences(self) -> None:
        self._meal_plan.dietary_preferences = ["Low Carb", "Gluten-Free"]

    def build_portion(self) -> None:
        self._meal_plan.portions = {
            "Chicken Salad": "1 bowl",
            "Fruit Juice": "200 ml",
            "Bread": "1 slice"
        }

    def build_nutritional_analysis(self) -> None:
        self._meal_plan.nutritional_analysis = {
            "Calories": 400,
            "Protein": 30,
            "Carbohydrates": 20,
            "Fat": 15
        }