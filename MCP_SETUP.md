# MCP サーバー連携

このリポジトリのルートにある `.mcp.json` で、Claude Code から以下の MCP サーバーを使えるようにしています。
リポジトリを開いて Claude Code を起動すると、初回に「プロジェクトの MCP サーバーを有効にするか」を確認されるので承認してください。

| サーバー | 用途 | 接続方式 | 認証 |
|---|---|---|---|
| Apify | 各種 Web / SNS スクレイピング (Apify Actors) | リモート HTTP `https://mcp.apify.com` | OAuth (初回利用時にブラウザでログイン) |
| Playwright | ブラウザ自動操作 | ローカル `npx @playwright/mcp@latest` | 不要 |
| Perplexity | リアルタイム Web 検索・リサーチ | ローカル `npx @perplexity-ai/mcp-server` | 環境変数 `PERPLEXITY_API_KEY` |
| Higgsfield | AI 画像・動画生成 | リモート HTTP `https://mcp.higgsfield.ai/mcp` | OAuth (Higgsfield アカウント) |
| Buffer | SNS 投稿の下書き・予約 | リモート HTTP `https://mcp.buffer.com/mcp` | OAuth (Buffer アカウント) |

## 認証手順

1. **Perplexity**: [Perplexity API ポータル](https://www.perplexity.ai/account/api) で API キーを発行し、環境変数に設定します。
   ```sh
   export PERPLEXITY_API_KEY="pplx-..."
   ```
   Claude Code on the web で使う場合は、環境設定の環境変数に `PERPLEXITY_API_KEY` を追加してください。
2. **Apify / Higgsfield / Buffer**: Claude Code で `/mcp` を実行し、各サーバーを選んで「Authenticate」からブラウザでログインします。
3. **Playwright**: 認証不要です。初回実行時にブラウザが必要な場合は `npx playwright install chromium` を実行してください。

## 動作確認

```sh
claude mcp list
```

API キーやトークンは `.mcp.json` に直接書かず、必ず環境変数または OAuth を使ってください。
