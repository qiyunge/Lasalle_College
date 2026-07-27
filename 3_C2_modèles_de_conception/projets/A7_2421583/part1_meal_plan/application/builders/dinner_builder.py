from __future__ import annotations

from .meal_plan_builder import MealPlanBuilder

class DinnerBuilder(MealPlanBuilder):
    def build_selected_foods(self) -> None:
        self._meal_plan.selected_foods = ["Grilled Salmon", "Steamed Vegetables", "Quinoa"]

    def build_dietary_preferences(self) -> None:
        self._meal_plan.dietary_preferences = ["High Protein", "Low Fat"]

    def build_portion(self) -> None:
        self._meal_plan.portions = {
            "Grilled Salmon": "200 g",
            "Steamed Vegetables": "1 cup",
            "Quinoa": "1/2 cup"
        }

    def build_nutritional_analysis(self) -> None:
        self._meal_plan.nutritional_analysis = {
            "Calories": 500,
            "Protein": 40,
            "Carbohydrates": 30,
            "Fat": 20
        }