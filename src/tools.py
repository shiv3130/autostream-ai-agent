def mock_lead_capture(name, email, platform):

    print(
        f"Lead captured successfully: {name}, {email}, {platform}"
    )

    return {
        "status": "success",
        "name": name,
        "email": email,
        "platform": platform
    }
