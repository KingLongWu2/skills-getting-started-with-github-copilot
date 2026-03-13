## Plan: Add FastAPI Backend Tests (AAA Pattern)

TL;DR：建立 `tests` 目錄，使用 pytest 與 FastAPI TestClient，並以 AAA（Arrange-Act-Assert）模式撰寫後端 API 測試，涵蓋活動查詢、報名、重複報名、取消報名等情境。

**Steps**
1. 建立 `tests/` 目錄於專案根目錄
2. 新增 `tests/test_app.py`，引入 pytest 與 FastAPI TestClient
3. 撰寫以下測試案例，皆採用 AAA 結構：
   - 測試取得活動列表
   - 測試學生成功報名活動
   - 測試學生重複報名同一活動（應失敗）
   - 測試取消報名（若後端支援）
   - 測試報名不存在的活動（應失敗）
4. 確認 requirements.txt 已包含 pytest、httpx（或 requests）、fastapi
5. 在 README.md 補充測試執行方式（如 pytest 指令）

**Relevant files**
- `tests/test_app.py` — 新增測試檔案，集中管理 FastAPI 測試案例
- `requirements.txt` — 確認測試相關套件
- `README.md` — 補充測試說明

**Verification**
1. 執行 `pytest`，所有測試皆通過
2. 測試報名、重複報名、查詢等情境皆有明確斷言

**Decisions**
- 採用 pytest + FastAPI TestClient
- 測試案例皆以 AAA（Arrange-Act-Assert）模式撰寫
- 測試檔案集中於 tests 目錄

**Further Considerations**
1. 若需支援取消報名，後端需實作 DELETE API
2. 若資料庫改為 persistent，測試需考慮隔離與清理
