class Category:
    def __init__(self, category_id, name, parent_id=None):
        if not isinstance(category_id, int) or category_id <= 0:
            raise ValueError("Category ID must be a positive integer")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Category name cannot be empty")
        self.category_id = category_id
        self.name = name.strip()
        self.parent_id = parent_id
        self.subcategories = []

    def add_subcategory(self, subcategory):
        if not isinstance(subcategory, Category):
            raise TypeError("subcategory must be a Category instance")
        if subcategory not in self.subcategories:
            self.subcategories.append(subcategory)

    def __str__(self):
        return f"Category({self.category_id}: {self.name})"


class CategoryManager:
    def __init__(self):
        self.categories = {}
        self.root_categories = []

    def create_category(self, category_id, name, parent_id=None):
        if category_id in self.categories:
            raise ValueError(f"Category ID {category_id} already exists")
        if parent_id is not None and parent_id not in self.categories:
            raise ValueError(f"Parent category {parent_id} does not exist")
        category = Category(category_id, name, parent_id)
        self.categories[category_id] = category
        if parent_id is None:
            self.root_categories.append(category)
        else:
            self.categories[parent_id].add_subcategory(category)
        return category

    def get_category_path(self, category_id):
        category = self.categories.get(category_id)
        if category is None:
            return None
        path = [category.name]
        current = category
        while current.parent_id is not None:
            current = self.categories[current.parent_id]
            path.insert(0, current.name)
        return " > ".join(path)

    def get_subcategories(self, category_id):
        category = self.categories.get(category_id)
        return list(category.subcategories) if category else []
