#This prog creates an algorithm visualizer
import math
import pygame
import random
pygame.init()

class DrawnInfo: #Drawing info
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    BLUE = 0,0,255
    BACKG_CLR = WHITE
    GREY = 125,125,125
    LIGHT = 160,160,160
    DARK = 200,200,200
    Greys = [GREY,LIGHT,DARK]

    FONT = pygame.font.SysFont('saline', 30)
    LARGER_FONT = pygame.font.SysFont('saline', 40)

    LR_PADDING = 120
    T_PADDING = 100
    def __init__(self, w, h, lst):
        self.w = w
        self.h = h
        self.window = pygame.display.set_mode((w,h)) # create window with width and height as a tupple
        pygame.display.set_caption("Algorithm Visualizer") 
        self.set_list(lst) 

    def set_list(self,lst): #create visualization
        self.lst = lst #internal store
        self.min_val = min(lst) #min list
        self.max_val = max(lst) #max list

        self.box_w = round((self.w - self.LR_PADDING)/ len(lst)) #ADD PADDING TO BOTH SIDES OF THE BOXES 
        self.box_h = math.floor((self.h - self.T_PADDING )/(self.max_val - self.min_val)) #ADD PADDING TO THE TOP 
        self.start_x = self.LR_PADDING//2
def make_start_list(y,min_val,max_val): #Rand. values between max and min values
    lst = []
    for i in range(y):
        val = random.randint(min_val,max_val)
        lst.append(val)
    return lst

#Bubble sort
def bubble_sort(draw_info, ascending = True):
    lst = draw_info.lst 

    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            num1 = lst[j]
            num2 = lst[j+1]
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j+1]=lst[j+1], lst[j] #swap in 1 line
                drawn_list(draw_info, {j:draw_info.BLUE, j+1:draw_info.RED},True)
                yield True # pause but stores current fxn state
    return lst

#Insertion sort
def insertion_sort(draw_info, ascending = True):
    lst = draw_info.lst 

    for i in range(1, len(lst)):
        current = lst[i]
        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i-1]
            i = i-1
            lst[i] = current
            drawn_list(draw_info, {i-1: draw_info.RED, i: draw_info.BLUE}, True)
            yield True

    return lst


def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst

    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(DrawnInfo(draw_info.w, draw_info.h, lst[:mid]), ascending)
    right = merge_sort(DrawnInfo(draw_info.w, draw_info.h, lst[mid:]), ascending)

    return merge(draw_info, left, right, ascending)

#Merge sort
def merge(draw_info, left, right, ascending):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (left[i] < right[j] and ascending) or (left[i] > right[j] and not ascending):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    draw_info.set_list(sorted_list)
    drawn_list(draw_info)
    yield True

    return sorted_list

#Quick sort
def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst
    return quick_sort_recursive(draw_info, 0, len(lst) - 1, ascending)

def quick_sort_recursive(draw_info, low, high, ascending):
    lst = draw_info.lst
    if low < high:
        pi = yield from partition(draw_info, low, high, ascending)
        yield from quick_sort_recursive(draw_info, low, pi - 1, ascending)
        yield from quick_sort_recursive(draw_info, pi + 1, high, ascending)

def partition(draw_info, low, high, ascending):
    lst = draw_info.lst
    pivot = lst[high]
    i = low - 1

    for j in range(low, high):
        if (lst[j] < pivot and ascending) or (lst[j] > pivot and not ascending):
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
            drawn_list(draw_info, {i: draw_info.BLUE, j: draw_info.RED}, True)
            yield True

    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    drawn_list(draw_info, {i + 1: draw_info.BLUE, high: draw_info.RED}, True)
    yield True

    return i + 1

#Heap sort 
def heap_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(draw_info, n, i, ascending)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        drawn_list(draw_info, {i: draw_info.BLUE, 0: draw_info.RED}, True)
        yield True
        yield from heapify(draw_info, i, 0, ascending)

def heapify(draw_info, n, i, ascending):
    lst = draw_info.lst
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and ((lst[l] > lst[largest] and ascending) or (lst[l] < lst[largest] and not ascending)):
        largest = l

    if r < n and ((lst[r] > lst[largest] and ascending) or (lst[r] < lst[largest] and not ascending)):
        largest = r

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        drawn_list(draw_info, {i: draw_info.BLUE, largest: draw_info.RED}, True)
        yield True
        yield from heapify(draw_info, n, largest, ascending)

#Selection sort 
def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if (lst[j] < lst[min_idx] and ascending) or (lst[j] > lst[min_idx] and not ascending):
                min_idx = j

        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        drawn_list(draw_info, {i: draw_info.BLUE, min_idx: draw_info.RED}, True)
        yield True



def main():
    run = True
    y = 45
    min_val = 0
    max_val = 100
    lst = make_start_list(y, min_val, max_val)
    draw_info = DrawnInfo(800, 600, lst)
    
    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting = False
    ascending = True

    sorting_algorithm_generator = None

    timer = pygame.time.Clock()  # Loop speed
    drawn(draw_info, sorting_algo_name, ascending)

    while run: 
        timer.tick(60)
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
            else:
                drawn(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():  # All events since last loop
            if event.type == pygame.QUIT:
                run = False   
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                lst = make_start_list(y, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
                drawn(draw_info, sorting_algo_name, ascending)
            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
                drawn(draw_info, sorting_algo_name, ascending)
            elif event.key == pygame.K_d and not sorting:
                ascending = False
                drawn(draw_info, sorting_algo_name, ascending)
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"
                drawn(draw_info, sorting_algo_name, ascending)
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"
                drawn(draw_info, sorting_algo_name, ascending)
            elif event.key == pygame.K_m and not sorting:
                sorting_algorithm = merge_sort
                sorting_algo_name = "Merge Sort"
                drawn(draw_info, sorting_algo_name, ascending)
            elif event.key == pygame.K_q and not sorting:
                sorting_algorithm = quick_sort
                sorting_algo_name = "Quick Sort"
                drawn(draw_info, sorting_algo_name, ascending)
            elif event.key == pygame.K_h and not sorting:
                sorting_algorithm = heap_sort
                sorting_algo_name = "Heap Sort"
                drawn(draw_info, sorting_algo_name, ascending)
            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = selection_sort
                sorting_algo_name = "Selection Sort"
                drawn(draw_info, sorting_algo_name, ascending)   
   
    pygame.quit()


def drawn(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKG_CLR)
    if ascending:
        title_color = draw_info.GREEN
    else:
        title_color = draw_info.RED

    title = draw_info.LARGER_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, title_color)
    draw_info.window.blit(title, (draw_info.w / 2 - title.get_width() / 2, 5))

    controls = draw_info.FONT.render("R - Reset   |   SPACE - Sorting Starts   |   A - Ascending   |   D - Descending", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.w / 2 - controls.get_width() / 2, 35))

    sorting_line_1 = draw_info.FONT.render("I - Insertion Sort   |   B - Bubble Sort   |   M - Merge Sort", 1, draw_info.BLACK)
    draw_info.window.blit(sorting_line_1, (draw_info.w / 2 - sorting_line_1.get_width() / 2, 55))

    sorting_line_2 = draw_info.FONT.render("Q - Quick Sort   |   H - Heap Sort   |   S - Selection Sort   ", 1, draw_info.BLACK)
    draw_info.window.blit(sorting_line_2, (draw_info.w / 2 - sorting_line_2.get_width() / 2, 75))

    drawn_list(draw_info)
    pygame.display.update()



def drawn_list(draw_info, color_position = {}, clear_bg = False):  #Draw rectangle for each element in list with the calculated position, size, and color
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.LR_PADDING//2, draw_info.T_PADDING, draw_info.w - draw_info.LR_PADDING,  draw_info.h - draw_info.T_PADDING)
        pygame.draw.rect(draw_info.window,draw_info.BACKG_CLR, clear_rect)

    for i,val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.box_w
        y = draw_info.h - (val - draw_info.min_val )* draw_info.box_h

        color = draw_info.Greys [i%3]

        if i in color_position:
            color = color_position[i]
        pygame.draw.rect(draw_info.window, color, (x,y,draw_info.box_w,draw_info.h))

    if clear_bg:
        pygame.display.update()

if __name__ == "__main__":
    main() 