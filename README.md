# astrbot_plugin_cmcc_newmsg

中国移动新消息（5G 消息）平台适配器插件 for [AstrBot](https://github.com/AstrBotDevs/AstrBot)。

通过 WebSocket 长连接接入中国移动 5G 消息平台，支持：

- 文本消息收发（自动将 Markdown 回复转换为纯文本）
- 富媒体消息收发：图片 / 音频 / 视频 / 文件（自动上传至 5G 消息服务）
- 心跳保活与断线自动重连（指数退避）
- 主动消息（`send_by_session`）与流式回复缓冲

## 安装

### 方式一：插件市场

在 AstrBot WebUI → 插件市场搜索安装（若已收录）。

### 方式二：手动安装

将本仓库克隆/下载到 AstrBot 的 `data/plugins/` 目录：

```bash
cd AstrBot/data/plugins
git clone https://github.com/jmclulu/astrbot_plugin_cmcc_newmsg
```

重启 AstrBot 后，在 WebUI → 消息平台 中新增「中国移动新消息(5G消息)」平台。

## 配置

| 字段 | 说明 | 默认值 |
| ---- | ---- | ---- |
| `api_key` | API Key，从中国移动侧管理员处获取，格式 `ak_` 或 `app_` 开头 | 必填 |
| `server_url` | WebSocket 长连接地址 | `wss://5gvas01.cmicmaap.com/gtw-ai/openclaw/ws/msg` |
| `upload_url` | 富媒体上传接口地址 | `https://5gvas01.cmicmaap.com/gtw-ai/openclaw/api` |
| `version` | 协议版本号 | `2.0` |

## 通信协议

协议移植自中国移动官方 OpenClaw 插件 `openclaw-cmcc-newmsg-channel`（安装指引：<https://5gvas01.cmicmaap.com/aifile/public/file/channel-guide.md>）：

- 连接 `wss://.../gtw-ai/openclaw/ws/msg`，握手携带 `X-API-Key` 请求头
- 连接后发送 `{"type":"auth","apiKey":...,"version":...}`，服务端先回 `connected` 再回 `auth_ok`
- 心跳：15s 一次 `ping` / `pong`，10s 超时断线重连
- 收消息：`message` / `text_message` / `media_message`（携带 `mediaType`、`mediaUrl` 等）
- 发消息：`send` 类型；富媒体先 `POST {upload_url}/upload`（multipart: `file` + `apiKey`）取得 `mediaUrl` 再发送

## 依赖

无需额外安装依赖（仅使用 `websockets` 与 `aiohttp`，均为 AstrBot 核心依赖）。

## 声明

- 本插件为社区实现，与中国移动官方无隶属关系
- 通信协议来源于中国移动官方 OpenClaw 插件的公开安装包，仅做协议兼容性移植
- API Key 请妥善保管，避免泄露

## License

MIT
