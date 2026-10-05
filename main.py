"""中国移动新消息 (5G消息) AstrBot 插件入口。

加载本插件时会在 import 阶段注册 cmcc_newmsg 平台适配器，
之后在 WebUI / 配置文件里添加 type 为 cmcc_newmsg 的平台即可启用。
"""

from __future__ import annotations

from astrbot.api.star import Context, Star, register


@register(
    "astrbot_plugin_cmcc_newmsg",
    "中国移动新消息(5G消息)平台适配器",
    "yacheng",
    "1.0.0",
)
class CmccNewmsgPlugin(Star):
    def __init__(self, context: Context) -> None:
        # 导入即注册平台适配器（装饰器副作用）
        from .cmcc_adapter import CmccNewmsgPlatformAdapter  # noqa: F401
