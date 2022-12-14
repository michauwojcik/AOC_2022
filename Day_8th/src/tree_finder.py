import numpy as np

class Forest:
    """
    Converts the raw forest plan into a form that allows to work on it.
    Also provides all operations to find all visibles trees in forest, 
    count them and calculate view score for each of them.

    """
    
    def __str__(self):
        repr = ""
        for row in self.matrix:
            repr += str(row) + "\n"
            
        return repr
            
    
    def __init__(self, raw_forest_plan: tuple):
        self.raw_forest_plan = raw_forest_plan
        self.matrix = self.parse_forest_plan()
        self.visible_trees_coors = list()
        
        self.edge_trees: int
        self.inside_visible_trees: int
        
        self.visible_trees: int
        self.view_scores = dict()
        
    
    def parse_forest_plan(self):
        """
        Creates more convenient form of forest's plan. 
        Forest plan is a generator of tuples. Each tuple represents a row of trees. 
        Each integer in row is a height of particular tree.
        
        Returns:
            (generator)
        """
        matrix = np.array([[int(char) for char in line] for line in self.raw_forest_plan])
        self.length, self.width = len(matrix), len(matrix[0])
        
        return matrix
    
    
    def get_visible_trees_coordinates(self):
        """
        Iterates over trees in *matrix* 
        and for inside trees checks whether tree is visible. 
        """
        
        for row_index in range(self.length):
            for tree_index, tree in enumerate(self.matrix[row_index]):
                is_tree_inside = (tree_index not in (0, self.width-1)) & (row_index not in (0, self.length-1))
                if is_tree_inside:
                    self.check_whether_visible(x=row_index, y=tree_index, tree_height=tree)
                
    
    
    def check_whether_visible(self, x: int, y: int, tree_height: int):
        """
        Checks whether tree is visible from west, east, north and south. 
        Works only for inside trees.

        Args:
            x (int): tree's longitude
            y (int): tree's latitude
            tree_height (int): tree's height
        """
        
        is_visible_west = (max(self.matrix[x, :y]) < tree_height) 
        is_visible_east = (max(self.matrix[x, (y+1):]) < tree_height)
        is_visible_north = (max(self.matrix[:x, y]) < tree_height)
        is_visible_south = (max(self.matrix[(x+1):, y]) < tree_height)
        
        is_visible = (is_visible_west | is_visible_east | is_visible_north | is_visible_south)
        
        if is_visible:
            self.visible_trees_coors.append((x, y))
        

    def count_trees_edges(self):
        return 2 * len(self.matrix) + 2 * (len(self.matrix[0]) - 2)
    
    
    def count_all_visible_trees(self):
        """
        Calculates number of visible trees, that is a sum of visible trees inside and trees on forest's edges.
        """
        
        self.edge_trees = self.count_trees_edges()
        
        self.get_visible_trees_coordinates()
        self.inside_visible_trees = len(self.visible_trees_coors)
        
        self.visible_trees = self.edge_trees + self.inside_visible_trees
    
    
    # TASK 2
    
    def calculate_trees_view_score(self):
        """
        Iterates over trees in *matrix* 
        and for inside trees checks whether tree is visible. 
        """
        
        for row_index in range(self.length):
            for tree_index, tree in enumerate(self.matrix[row_index]):
                view_west = self.get_tree_view(tree, self.matrix[row_index, :tree_index][::-1])
                view_east = self.get_tree_view(tree, self.matrix[row_index, (tree_index+1):])
                view_north = self.get_tree_view(tree, self.matrix[:row_index, tree_index][::-1])
                view_south = self.get_tree_view(tree, self.matrix[(row_index+1):, tree_index])

                self.view_scores[(row_index, tree_index)] = view_west * view_east * view_north * view_south


    @staticmethod
    def get_tree_view(tree_height: int, trees: np.array):
        
        if len(trees) == 0:
            return 0
        if trees[0] == tree_height:
            return 1
            
        higher_trees = list(filter(lambda _: _ >= tree_height, trees))

        if higher_trees:
            view = list(trees).index(higher_trees[0]) + 1
        else:
            view = len(trees)
        
        return view


    def get_tree_with_highest_score(self):
        key_max_view_score = max(self.view_scores, key=self.view_scores.get)
        return  key_max_view_score, self.view_scores[key_max_view_score]