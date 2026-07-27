from __future__ import annotations

from .meal_plan_builder import MealPlanBuilder

class BreakfastBuilder(MealPlanBuilder):
    def build_selected_foods(self) -> None:
        self._meal_plan.selected_foods = ["Egg", "Toast", "Milk"]

    def build_dietary_preferences(self) -> None:
        self._meal_plan.dietary_preferences = ["Vegetarian", "Low Sugar"]

    def build_portion(self) -> None:
        self._meal_plan.portions = {
            "Egg":"2",
            "Toast": "2 slices",
            "Milk": "250 ml"
        }

    def build_nutritional_analysis(self) -> None:
        self._meal_plan.nutritional_analysis = {
            "Calories": 350,
            "Protein": 10,
            "Carbohydrates": 60,
            "Fat": 5
        }