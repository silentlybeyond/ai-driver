# AI Driver — Codexへの導入（Windows CLI）

AI Driver ChatGPT版 `v0.1.12-poc13` の**既存Skill**をCodexから明示的に利用する方法です。Codex専用の別実装はなく、自動起動も保証しません。

## ワークスペース単位のインストール

1. GitHubの [Skill専用ZIP](../dist/ai-driver-chatgpt-skill-v0.1.12-poc13.zip) をダウンロードします。**プラグイン用ZIP・リポジトリ全体のZIPは使わないでください。**
2. PowerShellで次を実行します。`$workspace` は実際のCodexプロジェクトフォルダに変更してください。既存のSkillは上書きしません。実行ポリシーの変更は不要です。

```powershell
$workspace = Join-Path $HOME 'my-codex-project'
$zip = Join-Path $HOME 'Downloads\ai-driver-chatgpt-skill-v0.1.12-poc13.zip'
$skills = Join-Path $workspace '.agents\skills'
$target = Join-Path $skills 'ai-driver'
if (-not (Test-Path -LiteralPath $workspace -PathType Container)) { throw 'Workspace not found' }
if (-not (Test-Path -LiteralPath $zip -PathType Leaf)) { throw 'Skill ZIP missing' }
if (Test-Path -LiteralPath $target) { throw 'Skill already exists: inspect without overwriting' }
New-Item -ItemType Directory -Path $skills -Force | Out-Null
Expand-Archive -LiteralPath $zip -DestinationPath $skills -ErrorAction Stop
$required = @('SKILL.md','references/requirements.md','references/conflict-rules.md','references/state-contract.md')
foreach ($name in $required) {
    if (-not (Test-Path -LiteralPath (Join-Path $target $name) -PathType Leaf)) { throw "Missing required file: $name" }
}
Write-Output 'AI_DRIVER_REQUIRED_FILES = 4/4 PRESENT'
Set-Location -LiteralPath $workspace
codex
```

3. Codexの新規セッションで以下の指示を入力します。読み取り結果を実行記録で確認してください。

```text
Use the $ai-driver Skill from .agents/skills/ai-driver. Actually read SKILL.md, references/requirements.md, references/conflict-rules.md and references/state-contract.md using available local tools. Preserve the goal, success criteria, evidence, and Human-reserved authority. Report exact read commands and results. Do not publish, contact third parties or modify protected settings without authorization.
```

## 確認済み範囲と制約

2026-10-21の**ユーザー提出Codex実行報告**に基づき、明示的Skill起動における限定SC-1〜SC-5はPASSです。SC-1：必須4資料の読取。SC-2：隔離領域での依存なしtask tracker実装。SC-3：8件の実行テスト。SC-4：ハンドオフ保存と実読戻し。SC-5：別の新規Codexセッションからの状態復元、保存証拠の照合、新しいreceiptの実読戻し。

ChatGPT CentralはWindowsの非公開実行ファイル・生ログを独立再検査していません。元のセッションIDが未記録で、2セッションのID同士の機械比較はできません。実行手順逸脱の所見も記録されています。**自動Skill起動、汎用的な第三者互換性、署名付き証明、完全な副作用監査、公式掲載や認証は未確立**です。SkillはHostの権限を拡張しません。

個人の実行パス、テストログ、ハンドオフや非公開証拠は公開リポジトリに含めていません。
