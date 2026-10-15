from app.app import app


def test_home_endpoint():
    app.config["TESTING"] = True

    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "GitOps Application Delivery"
    assert data["status"] == "running"
    assert data["version"] == "1.0.0"


def test_health_endpoint():
    app.config["TESTING"] = True

    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


def test_deployment_status_endpoint():
    app.config["TESTING"] = True

    client = app.test_client()
    response = client.get("/status")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "GitOps Application Delivery"
    assert data["deployment_status"] == "successful"
    assert data["version"] == "1.0.0"
