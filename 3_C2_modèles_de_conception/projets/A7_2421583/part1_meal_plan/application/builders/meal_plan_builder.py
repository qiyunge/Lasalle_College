from __future__ import annotations

from abc import ABC, abstractmethod

from domain import MealPlan
class MealPlanBuilder(ABC):

    def __init__(self):
        self._meal_plan = MealPlan()
    
    @abstractmethod
    def build_selected_foods(self) -> None:
        pass


    @abstractmethod
    def build_dietary_preferences(self) -> None:
        pass

    @abstractmethod
    def build_portion(self) -> None:
        pass

    @abstractmethod
    def build_nutritional_analysis(self) -> None:
        pass

    def get_meal_plan(self) -> MealPlan:
        return self._meal_plan

    def reset(self) -> None:
        self._meal_plan = MealPlan()

    