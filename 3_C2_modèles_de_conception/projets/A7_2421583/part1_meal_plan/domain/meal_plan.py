from __future__ import annotations

from dataclasses import dataclass,field

@dataclass
class MealPlan:
    selected_foods:list[str] = field(default_factory=list)
    dietary_preferences: list[str] = field(default_factory=list)
    portions: dict[str, str ] = field(default_factory=dict)
    nutritional_analysis: dict[str, float] = field(default_factory=dict)
