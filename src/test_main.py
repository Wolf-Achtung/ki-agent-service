from crew_config import crew

def test_flow():
    input_data = {
        "name": "Anna",
        "unternehmen": "GPT Solutions",
        "datum": "2025-06-16"
    }
    result = crew.run({"questionnaire": input_data})
    print(result)
