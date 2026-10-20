# AI Driver — ChatGPT に非公開でインストールする

この文書は、GitHub で公開された AI Driver のソースを、**利用者本人のChatGPTで非公開利用するための手順**です。これはOpenAI公式Plugin Directoryでの公開・承認・OpenAIによる推奨を意味しません。

**重要:** GitHubの「Code → Download ZIP」（リポジトリ全体のZIP）をそのままアップロードするのではなく、以下の用途別ZIPを使用してください。

## 方法A — ChatGPTの「個人用Skill」を使う（Skillsタブを利用できる場合）

1. [Skill専用ZIP](../../dist/ai-driver-chatgpt-skill-v0.1.12-poc13.zip) をダウンロードします。ZIPの中は `ai-driver/SKILL.md` と `ai-driver/references/`、`ai-driver/templates/` です。
2. ChatGPT Webの **Plugins → Skills → Create → Upload from your computer** を開きます（表示が異なる場合があります）。
3. Skill専用ZIPをアップロードし、セキュリティスキャンと必要な確認が終わってから有効にします。
4. 自分だけで使う場合は **Share/Publish を実行しません**。ワークスペース内の共有設定も確認します。
5. 新しいチャットで「AI Driverを使って、このプロジェクトの目的と完了条件から次の作業を決めて」と依頼します。

**提供条件:** OpenAIの公開ヘルプによると、ChatGPT内の個人用Skillsは主にBusiness、Enterprise、Healthcare、Edu等で提供されています。Plus等で Skills タブやアップロード機能が表示されない場合があります。利用可否はプランとワークスペース設定によります。

## 方法B — 「非公開プラグイン」としてインストールする（アップロード機能がある場合）

1. [プラグイン専用ZIP](../../dist/ai-driver-chatgpt-plugin-v0.1.12-poc13.zip) をダウンロードします。ZIP内に `.codex-plugin/plugin.json`、`plugin.json`、`skills/ai-driver/` が含まれます。
2. ChatGPTの **Plugins** ページを開きます。使用中のUIで **Add → Upload plugin** または **Upload new or existing plugin** があれば選択します。個人／ワークスペースごとに必要権限が異なります。
3. ZIPをアップロードして検証結果を確認し、プライベート利用に設定します。**公開ディレクトリへの Submit / Publish は行いません。**
4. インストールして有効化したら、新しいチャットでAI Driverの動作を確認します。

**注意:** ZIPをGitHubから取得できても、どのChatGPTアカウントにもプラグインアップロード権限があるとは限りません。個人用Plugin作成UIが使えない場合は、無理に公式公開手続きへ進まないでください。

**検証実績（2026-10-21）:** 既存プラグインに影響させないよう、公開候補とSkill本文が同じ検証専用プラグインを別名でPRIVATE作成し、13ファイル登録を確認しました。ただし、既存のPlusアカウントすべてでアップロード可能とは限らず、新規チャットでのSkill自動起動やSkill専用ZIPアップロードは未検証です。

## よくある間違い

- **GitHubリポジトリ全体のZIP ≠ Skill専用ZIP ≠ プラグイン専用ZIP**。用途ごとに異なる構造です。
- **チャットへの単純なファイル添付 ≠ Skillのインストール**。Plugins内の専用画面から導入します。
- Skill／Pluginのインストールは、以前の会話・Claudeの保存データ・個人のファイルへのアクセス権を自動的には付与しません。
- AI Driverはユーザーが許可したホスト機能でのみ動作し、チャット間の自動的な状態復元を保証しません。成果物の保存・読戻しを確認してください。
- GitHub公開はOpenAI公式Plugin Directoryへの掲載とは異なります。**非公開利用に公開者としての実名表示を伴うディレクトリ申請は不要です。**

## 利用開始用の例

> AI Driverを使って進めてください。目的は○○です。完了条件は○○です。必要な作業を判断し、可能な作業は実行し、判断が必要な点は推奨案と理由を示してください。実行結果は確認可能な証拠で検証してください。

## 確認済みと未確認

この配布物はChatGPT版ソース `0.1.12-poc13` に由来する公開候補です。原本との差分・プライバシーの静的検査は別途実施していますが、**この用途別ZIPを第三者のChatGPTアカウントにインストールできることやSkillの自動起動は、まだライブ試験で確立していません。** 各機能の提供条件とUIは変更され得ます。

公式ガイド：

- [ChatGPTのSkills](https://help.openai.com/ja-jp/articles/20001066-skills-in-chatgpt)
- [ChatGPTのPlugins](https://help.openai.com/ja-jp/articles/20001256-plugins-in-chatgpt)
- [OpenAIプラグインのパッケージ仕様](https://developers.openai.com/plugins/build/plugins)

