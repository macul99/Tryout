class NestedMap(dict):
    token_str = '.'
    
    def _is_leaf_node(self, key):
        if self.token_str in key:
            idx = key.index(self.token_str)
            return (False, key[:idx], key[idx+len(self.token_str):])
        return (True, None, None)
    
    def __getitem__(self, key):
        leaf_node_flag, current_node, child_nodes = self._is_leaf_node(key)
        if leaf_node_flag:
            return super().__getitem__(key)
        else:
            return super().__getitem__(current_node).__getitem__(child_nodes)
    
    def __setitem__(self, key, value):
        # convert value to NestedMap if it is native dict type
        if isinstance(value, dict) and isinstance(value, NestedMap)==False:
            value = NestedMap(value)
            
        # self is current node
        leaf_node_flag, current_node_key, child_and_following_nodes_key = self._is_leaf_node(key)
        if leaf_node_flag: # set value in dict directly in leaf node
            super().__setitem__(key, value)
        else:
            # let key = a.b.c
            # current_node_key = a
            # child_and_following_nodes_key = b.c
            # child_node_key = b
            _, child_node_key, _ = self._is_leaf_node(child_and_following_nodes_key)
            
            # check child_node exits or not, if not create a new NestedMap object
            child_node = self.get(current_node_key, None)
            if child_node is None or isinstance(child_node, NestedMap)==False:
                child_node = NestedMap()
                super().__setitem__(current_node_key, child_node)
            
            child_node.__setitem__(child_and_following_nodes_key, value)
    
    def __delitem__(self, key):
        leaf_node_flag, current_node_key, child_and_following_nodes_key = self._is_leaf_node(key)
        if leaf_node_flag:
            super().__delitem__(key)
        else:
            super().__getitem__(current_node_key).__delitem__(child_and_following_nodes_key)
            if len(super().__getitem__(current_node_key))==0: # if no more children, delete current node
                super().__delitem__(current_node_key)
            
    def __str__(self):
        """
        Returns a string representation of the NestedMap object.
        eg: ['b: 3', 'a.b.c.d: 1']
        """
        items = []
        for k, v in self.items():
            if isinstance(v, dict):
                temp = eval(str(v)) # convert str to a list
                items += [".".join([k, x]) for x in temp]
            else:
                items += [f"{k}: {v}"]
        return f"{items}"
