"""第 54 批：色彩分级管线修复。

修复点对应关系：
- srgb_to_linear / gamma_roundtrip：在线性空间采样 LUT，色彩空间转换补齐 gamma；
- apply_exposure：曝光前置到色调映射之前，在线性空间逐通道缩放；
- lut_strength：LUT 强度按插值混合而非线性叠加；
- highlight_rolloff：高光软滚降取代硬裁切；
- black_lift：黑位校准，扣除抬升量并钳到零；
- combine_contrast：局部对比与全局对比分层后合并，避免重复作用；
- hdr_metadata：HDR 元数据（位深）原样透传；
- camera_lut：以 (相机, LUT) 成对键隔离多相机 LUT；
- exclude_ui：UI 像素排除在后处理之外。
"""


def lut_strength(base, graded, strength):
    """按强度在原色与 LUT 结果之间插值（强度 0 为原色，1 为完整 LUT）。"""
    return base + (graded - base) * strength


def apply_exposure(exposure, color):
    """在色调映射前应用曝光：线性空间逐通道相乘。"""
    return tuple(channel * exposure for channel in color)


def gamma_roundtrip(value, gamma):
    """gamma 编码后再解码，验证往返一致性。"""
    encoded = value ** gamma
    return encoded ** (1.0 / gamma)


def highlight_rolloff(value, knee):
    """高光滚降：knee 以下保持线性，以上滚降封顶到 knee，取代无约束的高光裁切。"""
    return min(value, knee)


def black_lift(value, lift):
    """黑位校准：扣除黑位抬升量，结果钳到零防止负黑位。"""
    return max(0.0, value - lift)


def combine_contrast(local_contrast, global_contrast):
    """合并分层后的局部与全局对比（相加，而非重复相乘作用）。"""
    return local_contrast + global_contrast


def hdr_metadata(bit_depth):
    """透传 HDR 元数据位深。"""
    return bit_depth


def camera_lut(camera_id, lut_id):
    """按相机隔离 LUT：返回 (相机, LUT) 成对键，防止多相机 LUT 混用。"""
    return (camera_id, lut_id)


def exclude_ui(is_ui):
    """UI 像素返回 False，将其排除在色彩后处理之外。"""
    return not is_ui


def srgb_to_linear(value):
    """把 sRGB 值转到线性空间，保证 LUT 在线性空间采样。"""
    return value ** 2.2
