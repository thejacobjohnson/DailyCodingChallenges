class rectangle:
    def __init__(self, start, size):
        self.top_left = start
        self.dimensions = size
        self.bottom_right = (start[0] + size[0], start[1] + size[1])

def main():
    rect1 = rectangle((1,4), (3,3))
    rect2 = rectangle((-1,3), (2,1))
    rect3 = rectangle((0,5), (4,3))

    rectangles = [rect1, rect2, rect3]
    for r in rectangles:
        for r2 in rectangles:
            if r == r2:
                continue
            if r.top_left[0] <= r2.top_left[0] and r.top_left[1] >= r2.top_left[1]:
                if r.bottom_right[0] >= r2.bottom_right[0] and r.bottom_right[1] >= r2.bottom_right[1]:
                    return True, r.top_left, r.dimensions, r2.top_left, r2.dimensions
            elif r2.top_left[0] <= r.top_left[0] and r2.top_left[1] >= r.top_left[1]:
                if r2.bottom_right[0] >= r.bottom_right[0] and r2.bottom_right[1] >= r.bottom_right[1]:
                    return True, r2.top_left, r2.dimensions, r.top_left, r.dimensions
            else:
                continue
        return False


answer = main()
if answer[0]:
    print('True')
    print(f'Rectangle at {answer[1]} with dimensions {answer[2]} overlaps rectangle at {answer[3]} with dimenions {answer[4]}')
else:
    print('False')
    print('No rectangles overlap.')
