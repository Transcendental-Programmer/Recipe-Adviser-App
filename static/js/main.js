document.addEventListener('DOMContentLoaded', function() {
    const recipeCards = document.querySelectorAll('.recipe-card');
    
    recipeCards.forEach(card => {
        card.addEventListener('click', function() {
            const recipeName = this.dataset.recipe;
            window.location.href = `/recipe_details/${encodeURIComponent(recipeName)}`;
        });
    });
});