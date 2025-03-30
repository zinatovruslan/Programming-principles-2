import pygame
import math
import sys

def main():
    pygame.init()
    
    screen_width, screen_height = 1024, 768
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Рисовалка с фигурами")
    
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'yellow': (255, 255, 0)
    }
    background_color = (240, 240, 240)
    
    radius = 5
    current_color = colors['blue']
    shapes = []
    current_tool = 'pen'
    drawing = False
    last_pos = None
    
    clock = pygame.time.Clock()
    
    def distance(p1, p2):
        return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: current_color = colors['red']
                elif event.key == pygame.K_g: current_color = colors['green']
                elif event.key == pygame.K_b: current_color = colors['blue']
                elif event.key == pygame.K_w: current_color = colors['white']
                elif event.key == pygame.K_k: current_color = colors['black']
                elif event.key == pygame.K_y: current_color = colors['yellow']
                
                elif event.key == pygame.K_p: current_tool = 'pen'
                elif event.key == pygame.K_c: current_tool = 'circle'
                elif event.key == pygame.K_l: current_tool = 'line'
                elif event.key == pygame.K_s: current_tool = 'rectangle'
                elif event.key == pygame.K_e: current_tool = 'eraser'
                elif event.key == pygame.K_q: current_tool = 'square'
                elif event.key == pygame.K_t: current_tool = 'right_triangle'
                elif event.key == pygame.K_y: current_tool = 'equilateral_triangle'
                elif event.key == pygame.K_r: current_tool = 'rhombus'
                
                elif event.key == pygame.K_d: shapes = []
                elif event.key == pygame.K_PLUS: radius = min(50, radius + 1)
                elif event.key == pygame.K_MINUS: radius = max(1, radius - 1)
                elif event.key == pygame.K_ESCAPE: 
                    pygame.quit()
                    sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    last_pos = mouse_pos
                    if current_tool == 'pen':
                        shapes.append(('pen', [mouse_pos], current_color, radius))
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    if current_tool in ['rectangle', 'circle', 'line', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                        shapes.append((current_tool, (last_pos, mouse_pos), current_color, radius))
            
            elif event.type == pygame.MOUSEMOTION:
                if drawing and current_tool == 'pen':
                    shapes[-1][1].append(mouse_pos)
        
        screen.fill(background_color)
        
        for shape in shapes:
            tool, data, color, width = shape
            
            if tool == 'pen' and len(data) > 1:
                pygame.draw.lines(screen, color, False, data, width)
            elif tool == 'line':
                pygame.draw.line(screen, color, data[0], data[1], width)
            elif tool == 'rectangle':
                rect = pygame.Rect(
                    min(data[0][0], data[1][0]),
                    min(data[0][1], data[1][1]),
                    abs(data[1][0] - data[0][0]),
                    abs(data[1][1] - data[0][1])
                )
                pygame.draw.rect(screen, color, rect, width)
            elif tool == 'circle':
                r = int(distance(data[0], data[1]))
                pygame.draw.circle(screen, color, data[0], r, width)
            elif tool == 'square':
                size = min(abs(data[1][0] - data[0][0]), abs(data[1][1] - data[0][1]))
                pygame.draw.rect(screen, color, (data[0][0], data[0][1], size, size), width)
            elif tool == 'right_triangle':
                pygame.draw.polygon(screen, color, [data[0], (data[1][0], data[0][1]), data[1]], width)
            elif tool == 'equilateral_triangle':
                height = (math.sqrt(3) / 2) * abs(data[1][0] - data[0][0])
                p1 = data[0]
                p2 = (data[0][0] + (data[1][0] - data[0][0]) // 2, data[0][1] - int(height))
                p3 = (data[1][0], data[0][1])
                pygame.draw.polygon(screen, color, [p1, p2, p3], width)
            elif tool == 'rhombus':
                width_rhombus = abs(data[1][0] - data[0][0])
                height_rhombus = abs(data[1][1] - data[0][1])
                p1 = (data[0][0] + width_rhombus // 2, data[0][1])
                p2 = (data[1][0], data[0][1] + height_rhombus // 2)
                p3 = (data[0][0] + width_rhombus // 2, data[1][1])
                p4 = (data[0][0], data[0][1] + height_rhombus // 2)
                pygame.draw.polygon(screen, color, [p1, p2, p3, p4], width)
        
        font = pygame.font.SysFont(None, 24)
        info = [
            f"Инструмент: {current_tool}",
            f"Цвет: {[k for k,v in colors.items() if v == current_color][0]}",
            f"Размер: {radius}",
            "Управление:",
            "P-Карандаш C-Круг L-Линия S-Прямоугольник Q-Квадрат",
            "T-Прямоуг. треуг. Y-Равносторонний треуг. R-Ромб",
            "E-Ластик D-Очистить +/-Размер ESC-Выход"
        ]
        
        for i, text in enumerate(info):
            text_surface = font.render(text, True, colors['black'])
            screen.blit(text_surface, (10, 10 + i*25))
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
