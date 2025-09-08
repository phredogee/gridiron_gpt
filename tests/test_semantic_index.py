from phred.semantic.index import patch_index, validate_index

def test_patch_and_validate():
    index = {"QB": ["Stroud"]}
    patched = patch_index(index)
    assert "QB" in patched
    assert validate_index(patched)
