def test_eco_friendly_title(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.verify_header_text('Eco Friendly')


def test_existing_sorting(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.verify_sorting('Sort By')


def test_item(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.verify_item_is_presented('Ana Running Short')
