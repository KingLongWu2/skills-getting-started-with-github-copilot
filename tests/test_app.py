import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Arrange-Act-Assert: 測試取得活動列表

def test_get_activities():
    # Arrange: 無需特殊安排
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0

# Arrange-Act-Assert: 測試學生成功報名活動

def test_signup_activity_success():
    # Arrange
    email = "testuser1@mergington.edu"
    activity_name = next(iter(client.get("/activities").json().keys()))
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    # Assert
    assert response.status_code == 200
    assert f"Signed up {email}" in response.json()["message"]
    # 再查詢活動，確認 email 已在 participants
    activity = client.get("/activities").json()[activity_name]
    assert email in activity["participants"]

# Arrange-Act-Assert: 測試學生重複報名同一活動（應失敗）

def test_signup_activity_duplicate():
    # Arrange
    email = "testuser2@mergington.edu"
    activity_name = next(iter(client.get("/activities").json().keys()))
    # 先報名一次
    client.post(f"/activities/{activity_name}/signup?email={email}")
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    # Assert
    assert response.status_code == 400 or response.status_code == 409
    assert "already signed up" in response.json()["detail"].lower()

# Arrange-Act-Assert: 測試報名不存在的活動（應失敗）

def test_signup_nonexistent_activity():
    # Arrange
    email = "testuser3@mergington.edu"
    activity_name = "nonexistent-activity"
    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
