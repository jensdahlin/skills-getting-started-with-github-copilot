from src.app import activities


def test_unregister_removes_participant(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = activities[activity_name]["participants"][0]

    # Act
    response = client.delete(f"/activities/{activity_name}/participants/{existing_email}")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Removed {existing_email} from {activity_name}"}
    assert existing_email not in activities[activity_name]["participants"]


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    unknown_activity = "Underwater Basket Weaving"
    email = "student@mergington.edu"

    # Act
    response = client.delete(f"/activities/{unknown_activity}/participants/{email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_participant_not_signed_up_returns_404(client):
    # Arrange
    activity_name = "Chess Club"
    unregistered_email = "nobody@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants/{unregistered_email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"
