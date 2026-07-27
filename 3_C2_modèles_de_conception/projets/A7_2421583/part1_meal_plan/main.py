from application.builders import (BreakfastBuilder,
                                   LunchBuilder,
                                   DinnerBuilder, 
                                   SnackBuilder, )

from application.meal_plan_director import MealPlanDirector

def print_meal_plan(meal_plan):
    print("Selected Foods:", meal_plan.selected_foods)
    print("Dietary Preferences:", meal_plan.dietary_preferences)
    print("Portions:", meal_plan.portions)
    print("Nutritional Analysis:", meal_plan.nutritional_analysis)
    print("*"*100)

def main():
    director = MealPlanDirector(BreakfastBuilder())
    breakfast = director.construct_meal_plan()
    print("Breakfast Meal Plan:")
    print_meal_plan(breakfast)

    director.set_builder(LunchBuilder())
    lunch = director.construct_meal_plan()
    print("Lunch Meal Plan:")
    print_meal_plan(lunch)

    director.set_builder(DinnerBuilder())
    dinner = director.construct_meal_plan()
    print("Dinner Meal Plan:")
    print_meal_plan(dinner)

    director.set_builder(SnackBuilder())
    snack = director.construct_meal_plan()
    print("Snack Meal Plan:")
    print_meal_plan(snack)


if __name__ == "__main__":
    main()