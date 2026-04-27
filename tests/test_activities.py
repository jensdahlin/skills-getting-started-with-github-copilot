from src.app import activities


def test_get_activities_returns_200(client):
    # Arrange – no extra setup needed; initial data provided by reset fixture

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_count = len(activities)

    # Act
    response = client.get("/activities")

    # Assert
    data = response.json()
    assert len(data) == expected_count


def test_get_activities_entries_have_required_fields(client):
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    data = response.json()
    for name, details in data.items():
        assert required_fields.issubset(
            details.keys()
        ), f"Activity '{name}' is missing required fields"


def test_get_activities_participants_is_list(client):
    # Arrange – nothing extra needed

    # Act
    response = client.get("/activities")

    # Assert
    data = response.json()
    for name, details in data.items():
        assert isinstance(
            details["participants"], list
        ), f"Participants for '{name}' should be a list"
