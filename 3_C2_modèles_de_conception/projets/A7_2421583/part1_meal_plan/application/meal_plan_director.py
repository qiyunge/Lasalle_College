from __future__ import annotations

from application.builders import MealPlanBuilder
from domain.meal_plan import MealPlan

class MealPlanDirector:
    def __init__(self, builder: MealPlanBuilder) -> None:
        self._builder = builder

    def set_builder(self, builder: MealPlanBuilder) -> None:
        self._builder = builder

    def construct_meal_plan(self) -> MealPlan:
        self._builder.reset()
        self._builder.build_selected_foods()
        self._builder.build_dietary_preferences()
        self._builder.build_portion()
        self._builder.build_nutritional_analysis()
        
        return self._builder.get_meal_plan()
