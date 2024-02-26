class Maple:
    def __init__(self, game_id, level):
        self.game_id = game_id
        self.level = level
maple1 = Maple('codetree', '10')
i, l = input().split()
maple2 = Maple(i,l)

print('user',maple1.game_id,'lv',maple1.level)
print('user',maple2.game_id,'lv',maple2.level)