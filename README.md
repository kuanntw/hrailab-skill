# HRxAI Research Handoff Skill

這個 repository 提供 `hrxai-research-handoff` Skill，用於協助 HRxAI 實驗室成員在完成研究或專案後，產出標準化、可被 AI 讀取的研究交接文件，並檢查交接資料是否完整、可追溯、可安全使用。

## 目標

此 Skill 的主要目標是讓 lab member 在資料整理完成後，可以建立一組固定格式的 handoff package。未來成員或 AI agent 可以透過這組文件快速回答：

- 研究主題、研究問題與實驗設計是什麼？
- RAW data、cleaned data、derived data、報告與行政資料分別在哪裡？
- 問卷、量表、變項、專家評分與 AI 系統輸出如何解讀？
- 哪些檔案含個資、研究敏感資料、後台資訊或權限限制？
- 哪份報告或論文是 final / best-current version？
- 未來若要重分析、沿用問卷或查找系統資源，應該先看哪些文件？
- 交接資料還缺什麼，是否已達到可交接狀態？

## Repository 結構

```text
hrxai-research-handoff/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── templates/
│       ├── 00_README_PROJECT_OVERVIEW.md
│       ├── 01_RESEARCH_PROTOCOL.md
│       ├── 02_DATA_INVENTORY.md
│       ├── 03_RAW_DATA_GUIDE.md
│       ├── 04_VARIABLE_DICTIONARY.md
│       ├── 05_MEASUREMENT_TOOLKIT.md
│       ├── 06_TECHNICAL_RESOURCES.md
│       ├── 07_REPORTS_AND_OUTPUTS_INDEX.md
│       ├── 08_PRIVACY_AND_ACCESS_NOTES.md
│       ├── 09_NEXT_USER_GUIDE.md
│       └── 10_HANDOFF_COMPLETENESS_CHECK.md
├── references/
│   ├── ai-query-patterns.md
│   ├── completeness-checklist.md
│   ├── data-classification.md
│   ├── handoff-document-spec.md
│   └── privacy-and-ethics.md
└── scripts/
    └── validate_handoff.py
```

## Skill 使用情境

### 1. Generate mode：產生交接文件

當 lab member 完成研究資料整理後，可請 AI 使用此 Skill 依據專案資料夾產生 `00` 到 `09` 的標準文件。

建議 prompt：

```text
請使用 hrxai-research-handoff skill，根據這個研究資料夾產出 00–09 的研究交接文件。
研究名稱是：TODO
資料根目錄是：TODO
負責人是：TODO
時間範圍是：TODO
請不要修改原始資料，請標示敏感資料、不確定處與 TODO。
```

### 2. Validate mode：檢查是否可交接

當 handoff package 已產生後，可使用此 Skill 檢查必要文件、必要欄位、資料可追溯性、隱私風險與 AI search readiness，並產出 `10_HANDOFF_COMPLETENESS_CHECK.md`。

建議 prompt：

```text
請使用 hrxai-research-handoff skill，檢查這份 handoff package 是否完整。
請產出 10_HANDOFF_COMPLETENESS_CHECK.md，並依 Critical / High / Medium / Low 列出缺漏與補齊建議。
```

### 3. Repair mode：依缺漏清單補齊

當 `10_HANDOFF_COMPLETENESS_CHECK.md` 已列出缺漏後，可請 AI 協助修補文件。無法確認的內容應保留 `TODO`，不可自行推論。

建議 prompt：

```text
請根據 10_HANDOFF_COMPLETENESS_CHECK.md，協助我逐項補齊缺漏。
對無法確定的資料請保留 TODO，不要自行推論檔案用途、final 狀態、變項角色、IRB/同意範圍或信效度數值。
```

## 每個研究專案應產出的 handoff package

```text
ProjectName_Handoff/
├── 00_README_PROJECT_OVERVIEW.md
├── 01_RESEARCH_PROTOCOL.md
├── 02_DATA_INVENTORY.md
├── 03_RAW_DATA_GUIDE.md
├── 04_VARIABLE_DICTIONARY.md
├── 05_MEASUREMENT_TOOLKIT.md
├── 06_TECHNICAL_RESOURCES.md
├── 07_REPORTS_AND_OUTPUTS_INDEX.md
├── 08_PRIVACY_AND_ACCESS_NOTES.md
├── 09_NEXT_USER_GUIDE.md
└── 10_HANDOFF_COMPLETENESS_CHECK.md
```

`10_HANDOFF_COMPLETENESS_CHECK.md` 是驗收結果；第一次產生草稿時可以先建立 `00` 到 `09`，再執行驗收。

## 使用 validator script

`scripts/validate_handoff.py` 提供 deterministic first-pass validation，可檢查：

- 標準文件是否存在。
- 必要 heading 是否存在。
- 是否仍有 `TODO` 或 `needs verification` placeholder。
- 是否疑似包含 password、API key、token 等敏感 credential。
- 依檢查結果產出 `10_HANDOFF_COMPLETENESS_CHECK.md`。

執行方式：

```bash
python3 hrxai-research-handoff/scripts/validate_handoff.py /path/to/ProjectName_Handoff
```

也可以指定輸出路徑：

```bash
python3 hrxai-research-handoff/scripts/validate_handoff.py /path/to/ProjectName_Handoff --output /path/to/10_HANDOFF_COMPLETENESS_CHECK.md
```

Exit code 說明：

- `0`：沒有 Critical issue；可能仍有 warning 或 TODO。
- `2`：存在 Critical issue，代表目前不應標記為 ready for handoff。

> 注意：validator script 是第一層自動檢查。正式驗收仍應依照 `references/completeness-checklist.md` 檢查資料可追溯性、隱私風險與 AI search readiness。

## 交接驗收狀態

此 Skill 使用三種整體狀態：

| Status | 意義 |
|---|---|
| `Not ready for handoff` | 有 Critical issue，或缺核心文件 / RAW data 路徑 / privacy notes / 敏感資料標記，暫不可交接。 |
| `Ready with warnings` | 無 Critical issue，但仍有 High / Medium 缺漏，需補齊或指派 owner。 |
| `Ready for handoff` | 無 Critical / High issue，且未來 AI 可回答核心查找問題。 |

缺漏嚴重度分為：

| Severity | 意義 |
|---|---|
| `Critical` | 阻礙安全或有效交接，例如 RAW data 不明、privacy notes 缺失、credential 外洩。 |
| `High` | 明顯影響重用或理解，例如實驗組別、final report、問卷版本或主要變項缺失。 |
| `Medium` | 降低可讀性或可追溯性，例如 known issues、recommended reading order、模型版本不完整。 |
| `Low` | 格式或 optional detail 問題。 |

## 隱私與安全原則

使用此 Skill 時，請遵守以下原則：

- 不要覆寫、移動、刪除或重新命名 RAW data。
- 不要在 handoff 文件中放入受試者姓名、電話、Email、學號、簽名、禮券個資等直接識別資訊。
- 不要在 handoff 文件中放入 live password、API key、backend credential、active invite code 或 private token。
- 對於問卷回覆、影片、AI features、專家評分、同意文件、實驗名單與行政補償紀錄，預設以 sensitive 或 highly sensitive 處理。
- 若無法確認資料用途、變項角色、final 狀態、同意範圍或信效度數值，應標示 `TODO` 或 `Needs verification`，不要自行推論。

## 後續維護建議

- 若 HRxAI 資料夾結構改變，請同步更新 `SKILL.md` 的 folder map 與 search order。
- 若新增固定 handoff 文件，請同步更新 `assets/templates/`、`references/handoff-document-spec.md` 與 `references/completeness-checklist.md`。
- 若 validator script 新增檢查規則，請同步更新 README 與 completeness checklist，避免人工作業與自動檢查規則不一致。
