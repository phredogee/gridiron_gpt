def test_missing_fields(snapshot):
    output = validate_schema({"name": "Alfredo"}, ["name", "age"], dry_run=True)
    snapshot.assert_match(output, "missing_fields_feedback")
