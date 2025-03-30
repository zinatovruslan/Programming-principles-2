import pygame
import math
import sys

def main():
    pygame.init()
    
    screen_width, screen_height = 1024, 768
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Рисовалка с умным ластиком")
    
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'yellow': (255, 255, 0)
    }
    background_color = (240, 240, 240)
    
    radius = 10
    current_color = colors['blue']
    shapes = []
    current_tool = 'pen'
    drawing = False
    last_pos = None
    
    erasing = False
    erase_radius = 15
    
    clock = pygame.time.Clock()
    
    def distance(p1, p2):
        return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
    
    def erase_at_position(pos, radius):
        nonlocal shapes
        new_shapes = []
        
        for shape in shapes:
            tool, data, color, width = shape
            
            if tool == 'pen':
                new_points = [p for p in data if distance(p, pos) > radius]
                if len(new_points) > 1:
                    new_shapes.append(('pen', new_points, color, width))
            
            elif tool in ['line', 'rectangle', 'circle']:
                keep_shape = True
                if tool == 'line':
                    points = [data[0], data[1]]
                elif tool == 'rectangle':
                    x1, y1 = data[0]
                    x2, y2 = data[1]
                    points = [(x1,y1), (x2,y1), (x2,y2), (x1,y2)]
                elif tool == 'circle':
                    center = data[0]
                    r = distance(center, data[1])
                    points = [center]
                
                for p in points:
                    if distance(p, pos) <= radius:
                        keep_shape = False
                        break
                
                if keep_shape:
                    new_shapes.append(shape)
        
        shapes = new_shapes
    
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
                
                elif event.key == pygame.K_d: shapes = []
                elif event.key == pygame.K_PLUS: radius = min(50, radius + 1)
                elif event.key == pygame.K_MINUS: radius = max(1, radius - 1)
                elif event.key == pygame.K_ESCAPE: 
                    pygame.quit()
                    sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if current_tool == 'eraser':
                        erasing = True
                        erase_at_position(mouse_pos, erase_radius)
                    else:
                        drawing = True
                        last_pos = mouse_pos
                        if current_tool == 'pen':
                            shapes.append(('pen', [mouse_pos], current_color, radius))
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    erasing = False
                    if current_tool in ['rectangle', 'circle', 'line'] and last_pos:
                        if current_tool == 'rectangle':
                            shapes.append(('rectangle', (last_pos, mouse_pos), current_color, radius))
                        elif current_tool == 'circle':
                            shapes.append(('circle', (last_pos, mouse_pos), current_color, radius))
                        elif current_tool == 'line':
                            shapes.append(('line', (last_pos, mouse_pos), current_color, radius))
            
            elif event.type == pygame.MOUSEMOTION:
                if drawing and current_tool == 'pen':
                    shapes[-1][1].append(mouse_pos)
                elif erasing and current_tool == 'eraser':
                    erase_at_position(mouse_pos, erase_radius)
        
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
        
        if drawing and current_tool in ['rectangle', 'circle', 'line']:
            if current_tool == 'rectangle':
                rect = pygame.Rect(
                    min(last_pos[0], mouse_pos[0]),
                    min(last_pos[1], mouse_pos[1]),
                    abs(mouse_pos[0] - last_pos[0]),
                    abs(mouse_pos[1] - last_pos[1])
                )
                pygame.draw.rect(screen, current_color, rect, 1)
            elif current_tool == 'circle':
                r = int(distance(last_pos, mouse_pos))
                pygame.draw.circle(screen, current_color, last_pos, r, 1)
            elif current_tool == 'line':
                pygame.draw.line(screen, current_color, last_pos, mouse_pos, 1)
        
        font = pygame.font.SysFont(None, 24)
        info = [
            f"Инструмент: {current_tool}",
            f"Цвет: {[k for k,v in colors.items() if v == current_color][0]}",
            f"Размер: {radius}",
            "Управление:",
            "P-Карандаш C-Круг L-Линия S-Прямоугольник E-Ластик",
            "D-Очистить +/-Размер ESC-Выход"
        ]
        
        for i, text in enumerate(info):
            text_surface = font.render(text, True, colors['black'])
            screen.blit(text_surface, (10, 10 + i*25))
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
