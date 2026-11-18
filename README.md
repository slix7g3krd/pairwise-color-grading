# pairwise-color-grading

同一张 LUT 在 HDR 和 SDR 下偏色、夜景发灰、肤色被压成塑料：LUT 按 sRGB 采样；曝光在色调映射后；LUT 强度线性叠加；色彩空间转换漏了 gamma；高光裁切；黑位抬升；局部对比和全局对比重复；HDR 元数据没透传；多相机 LUT 混用；UI 也被后处理影响。render/color_grading.py 是核心，tests/test_color_grading.py 15个红。要修的是：线性空间采样；曝光前置；LUT 强度插值；gamma 往返；高光滚降；黑位校准；对比分层；HDR 元数据；相机 LUT 隔离；UI 后处理排除。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：图形渲染；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
