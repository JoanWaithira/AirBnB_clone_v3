class Test:
    def __init__(self, name):
        self.name = name


review_obj = Test('Philip')
new_dict = {'age': 25, 'id': 4}
for key, val in new_dict.items():
    if key not in ['created_at', 'updated_at', 'user_id', 'id']:
        setattr(review_obj, key, val)
print(review_obj.__dict__)
