import math
from core.config import PARTICLE_TYPES, INTERACTION_VALUES

def get_interaction(type1, type2):
    try:
        i = PARTICLE_TYPES.index(type1)
        j = PARTICLE_TYPES.index(type2)
        return INTERACTION_VALUES[i][j]
    except ValueError:
        return 0  # Không tương tác
    
def resolve_collision(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    dist = math.hypot(dx, dy)
    min_dist = p1.radius + p2.radius

    if 0 < dist < min_dist:
        # Vector đơn vị va chạm
        nx = dx / dist
        ny = dy / dist

        # Vận tốc tương đối
        # Tích vô hướng
        v1n = p1.vx * nx + p1.vy * ny
        v2n = p2.vx * nx + p2.vy * ny

        # Va chạm đàn hồi 1D trên trục pháp tuyến (elastic collision)
        m1, m2 = p1.mass, p2.mass
        v1n_new = (v1n * (m1 - m2) + 2 * m2 * v2n) / (m1 + m2)
        v2n_new = (v2n * (m2 - m1) + 2 * m1 * v1n) / (m1 + m2)

        # Chuyển lại về vận tốc vector
        p1.vx += (v1n_new - v1n) * nx
        p1.vy += (v1n_new - v1n) * ny
        p2.vx += (v2n_new - v2n) * nx
        p2.vy += (v2n_new - v2n) * ny

        # Đẩy particle ra để không chồng lấn
        overlap = min_dist - dist
        correction = overlap / 2
        p1.x -= correction * nx
        p1.y -= correction * ny
        p2.x += correction * nx
        p2.y += correction * ny


# interaction_strength > 0 repulsion, otherwise attraction
def compute_force(p1, p2, interaction_strength, interaction_distance):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    
    dist = math.hypot(dx, dy)
    if 0 < dist < interaction_distance:
        # Vector đơn vị từ p1 đến p2
        nx = dx / dist
        ny = dy / dist

        # Lực đẩy giảm theo khoảng cách (kiểu F = k / r^2)
        k = interaction_strength  # hệ số lực, bạn có thể điều chỉnh
        force = k / (dist ** 2)

        # Áp dụng Newton III: lực ngược chiều trên 2 vật
        fx = force * nx
        fy = force * ny

        # Từ F = m·a => a = F / m
        p1.apply_force(-fx, -fy)
        p2.apply_force(fx, fy)
        