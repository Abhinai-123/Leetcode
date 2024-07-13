class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        stack = []
        survivors = []

        for pos, health, dir, index in robots:
            if dir == 'R':
                stack.append((pos, health, dir, index))
            else:  
                while stack and stack[-1][2] == 'R' and health > 0:
                    _, top_health, _, _ = stack[-1]
                    if top_health < health:
                        stack.pop()
                        health -= 1
                    elif top_health > health:
                        stack[-1] = (stack[-1][0], top_health - 1, stack[-1][2], stack[-1][3])
                        health = 0
                    else: 
                        stack.pop()
                        health = 0
                if health > 0:
                    survivors.append((pos, health, dir, index))

        survivors.extend(stack)
        survivors.sort(key=lambda x: x[3]) 

        return [health for _, health, _, _ in survivors]

