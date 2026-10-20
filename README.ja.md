# AI Driver — 日本語案内

**AIに目的と終了条件を伝え、複数段階の仕事を目的達成まで進めるためのSkillです。**

AI Driverは、利用者が定めた目的・成功条件・決定事項・権限を保全し、次の仕事の選定、権限内の実行・委任、成果の検証、未完了作業の再開を支援します。`silentlybeyond` による独立開発であり、**Anthropicが制作・認証・推奨した製品ではありません**。

## 対応環境と検証状況

| 環境 | 導入方法 | 検証状況 |
| --- | --- | --- |
| Claude Code（ターミナル / VS Code） | 以下のMarketplace経由 | rc.3のMarketplace・Plugin定義に対するClaude Code公式検証2/2 PASS。GitHubインストール済みrc.3のSkillと参照資料の読込も利用者報告で確認済み。更新候補rc.4は公式検証前 |
| **ClaudeのWebチャット（Freeを含む）** | **専用Skill ZIPをアップロード** | Anthropic公式がFreeのカスタムSkillに対応。**旧Web版のFreeでのアップロード・判断テストと、別名Adapterテスト版でのDoc保存・別チャット直接読込・タイトル検索は利用者報告に基づき限定PASS。今回のv0.3配布ZIPは未検証** |
| GitHub Copilot / Gemini CLI | 将来の対応候補 | 未検証 |
| ChatGPT / Codex | OpenAIのPlugin Directoryで別途配布 | このClaude版ZIPでは直接インストールしない |

## 1. Claude Codeでのインストール

Claude Codeの入力欄で次を実行します（PowerShellではありません）。

```text
/plugin marketplace add silentlybeyond/ai-driver
/plugin install ai-driver@silentlybeyond-ai-driver
```

必要と表示されたら `/reload-plugins` を実行します。明示起動は `/ai-driver:ai-driver`。自動選択は保証されません。ローカル試験では、展開したリポジトリのルートで `claude --plugin-dir ./plugins/ai-driver` を実行してください。

## 2. Claude Web・Free版へのインストール

Anthropic公式ヘルプでは、**Free / Pro / Max** で自分のカスタムSkillをアップロードできます。プラグイン用Marketplaceのインストールとは別の方法です。

1. このリポジトリの [Claude Web用Skill ZIP](dist/ai-driver-claude-web-skill-v0.1.13-rc.4.zip) を取得します。**リポジトリ全体のZIPはSkillアップロードに使用しません。**
2. [Claude](https://claude.ai/new) で **Settings（設定）→ Capabilities（機能）** の **Code execution and file creation（コード実行とファイル作成）** を有効にします。
3. **Customize（カスタマイズ）→ Skills → ＋ → Create skill → Upload a skill** を選びます（表示名が変更される場合があります）。
4. 上記のSkill専用ZIPをアップロードし、**AI Driver** を有効化します。
5. 新規チャットで下記の利用例を入力し、Skillが読み込まれたか確認します。自動選択されなければ、AI Driverを使うよう明示してください。

専用ZIPは `ai-driver/SKILL.md` と必須参照資料・テンプレートなどを含みます。ClaudeのカスタムSkillガイドにある **description最大200文字** に合わせて起動用説明のみ短縮し、動作ルール本文・参照資料はClaude Code版と同一です。**旧版のFree導入は実機確認済みですが、このrc.4 ZIP自体のアップロードと動作は未確認です。** Freeプラン固有の利用上限も適用されます。

公式資料：[ClaudeでSkillを使用する](https://support.claude.com/ja/articles/12512180-claude%E3%81%A7%E3%82%B9%E3%82%AD%E3%83%AB%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B)、[カスタムSkillの作成方法](https://support.claude.com/ja/articles/12512198-%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A0%E3%82%B9%E3%82%AD%E3%83%AB%E3%81%AE%E4%BD%9C%E6%88%90%E6%96%B9%E6%B3%95)。

## 3. 基本的な使い方

目的と終了条件を具体的に伝えます。次の文章を新しいチャットに入力できます。

```text
AI Driverを使って次の開発を進めてください。
目的：実際に利用できるWebタスク管理アプリを完成させる。
終了条件：タスクの追加、完了・未完了の切替、削除ができること。
ブラウザを閉じてもデータが残ること。実行テストと成果物があること。
利用可能なツールと認可の範囲内で必要な仕事を進めてください。
私の承認なしに公開・外部連絡・成功条件の変更を行わないでください。
次の必要作業と実際に検証できたことを報告してください。
```

AI Driverは実際に許可された操作だけを行います。指示文を作成したことと、実際に作業・送信・検証したことを区別します。Claude Webに登録しただけでPCのローカルファイル操作が可能になるわけではありません。

## 4. 新しいチャットへ移るときの引き継ぎ方

### Claude保存Adapter（配布用ガイド）

Skillには、Claudeで保存・再開するときだけ読む `references/claude-adapter.md` を追加しました。通常チャットの非公開Artifacts / Claude Docs、同じProject内のチャットで利用するために**明示的に登録したProject Knowledge**、Claude Codeの非公開ローカル状態ファイルを区別します。**Claude Freeで別名のAdapterテストSkillがClaude Docを保存・読戻しし、別チャットでDoc ID指定とArtifacts一覧のタイトル検索から全文を復元したとの実機報告があります。ただし今回のrc.4配布ZIPの動作、Project Knowledgeの更新、検索機能が全セッションで利用できるか、Docの共有設定は未検証です。** 文書の作成だけで次チャットへの引継ぎは成立しません。使える機能と保存・読戻しを実際に確認し、できない場合は下記の完全ハンドオフ手順に戻ります。



**Skillをインストールしただけでは、チャット間で個別プロジェクトの状態が必ず共有されるわけではありません。** 記憶・前チャット・ローカルファイルにアクセスできるとは限らないため、引継ぎ内容を明示的に残します。

**利用可能なClaude Docsツールがある場合は、完全な状態を非公開Docに保存して全文を読戻し、DocタイトルとIDを控える方式を優先します。新しいチャットからArtifacts一覧でタイトルを一意検索して全文を読めれば、コピー不要で再開できます。不可ならDoc ID、添付、全文コピーの順に代替します。以下は汎用的な引継ぎ指示です。**

**今のチャットを終える前**に、次を依頼します。

```text
AI Driverを使って、新しいチャットへ移るための引継ぎ状態を作成してください。
元の目的・終了条件、有効なHumanの決定と権限制約、検証済みの成果と
証拠の所在、未完了作業、NEXT_OWNER、NEXT_ACTION、
TARGET_SESSION_OR_TOOL、EXPECTED_RETURN、ACTION_STATE、
保存状態のバージョンと出典を整理してください。不明事項は不明と明記。
全文をコピー可能な形で提示し、実際に保存できた場合のみ保存済みと報告。
```

**新しいチャット**には、その全文を貼り付けるか非公開の引継ぎファイルを添付し、次を入力します。

```text
AI Driverを使って、この引継ぎ状態からプロジェクトを再開してください。
引継ぎを新しい権限付与とは扱わず、出典・バージョン・根拠を確認し、
有効なHumanの決定・権限・終了条件を保って次の必要作業を判断してください。
不明な成果や操作を推測で完了にしないでください。
```

Claude Codeでは、アクセスが実際に認可された**非公開の状態ファイル**を利用する方法もあります。Claude Webでは、上記のコピー可能な引継ぎを基本としてください。**個人情報・秘密情報・実際の引継ぎ状態を公開GitHubへコミットしないでください。** `templates/state-template.md` は空のテンプレートで、保存済みプロジェクトではありません。`chatgpt-library-adapter.md` はChatGPT固有の参照資料であり、ClaudeにChatGPT Libraryへのアクセス権を与えません。

## 5. プライバシーと公開状況

本配布物はSkill指示・参照Markdown・画像で構成され、独自の外部MCPサーバー、フック、実行バイナリ、テレメトリー収集プログラムは同梱していません。ホストの権限と利用者の指示の範囲で利用します。限定検査の合格は一般的な安全性の認証ではありません。

[プライバシーポリシー](https://silentlybeyond.github.io/ai-driver-privacy/ja.html) · [English README](README.md)

公開後の非機密のフィードバックはGitHub Issuesで受け付けます。秘密情報や個人の作業記録を投稿しないでください。

**公開名義：** `silentlybeyond`（個人の活動名） ／ **ライセンス：** MIT (`LICENSE`)。候補版 `0.1.13-rc.4`。Anthropic審査・掲載は未実施です。
