"""第 54 批：同一张 LUT 在 HDR 和 SDR 下偏色、..."""

def lut_strength(base, graded, strength):
    """按强度插值 LUT 结果。"""
    raise NotImplementedError("TODO: lut_strength")

def apply_exposure(exposure, color):
    """在色调映射前应用曝光。"""
    raise NotImplementedError("TODO: apply_exposure")

def gamma_roundtrip(value, gamma):
    """验证 gamma 往返一致性。"""
    raise NotImplementedError("TODO: gamma_roundtrip")

def highlight_rolloff(value, knee):
    """对高光做滚降。"""
    raise NotImplementedError("TODO: highlight_rolloff")

def black_lift(value, lift):
    """校准黑位抬升。"""
    raise NotImplementedError("TODO: black_lift")

def combine_contrast(local_contrast, global_contrast):
    """合并局部与全局对比。"""
    raise NotImplementedError("TODO: combine_contrast")

def hdr_metadata(bit_depth):
    """透传 HDR 元数据位深。"""
    raise NotImplementedError("TODO: hdr_metadata")

def camera_lut(camera_id, lut_id):
    """按相机隔离 LUT。"""
    raise NotImplementedError("TODO: camera_lut")

def exclude_ui(is_ui):
    """判断是否排除 UI 后处理。"""
    raise NotImplementedError("TODO: exclude_ui")

def srgb_to_linear(value):
    """把 sRGB 值转到线性空间。"""
    raise NotImplementedError("TODO: srgb_to_linear")
