from collections import defaultdict, deque

def findAllRecipes(recipes, ingredients, supplies):
    ingredient_to_recipes = defaultdict(list)
    
    # Track the number of required ingredients for each recipe
    in_degree = {recipe: 0 for recipe in recipes}
    
    for i, recipe in enumerate(recipes):
        for ingredient in ingredients[i]:
            ingredient_to_recipes[ingredient].append(recipe)
            in_degree[recipe] += 1
            
    queue = deque(supplies)
    result = []
    
    while queue:
        ingredient = queue.popleft()
        
        for recipe in ingredient_to_recipes[ingredient]:
            in_degree[recipe] -= 1
            
            if in_degree[recipe] == 0:
                result.append(recipe)
                queue.append(recipe)
                
    return result

# Example usage
recipes = ["bread", "sandwich", "burger"]
ingredients = [["yeast", "flour"], ["bread", "cheese"], ["sandwich", "patty"]]
supplies = ["yeast", "flour", "cheese", "patty"]
print("Recipes that can be created:", findAllRecipes(recipes, ingredients, supplies))