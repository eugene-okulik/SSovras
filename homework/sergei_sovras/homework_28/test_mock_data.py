from playwright.sync_api import Page, Route
import json

def test_mock_data(page: Page):

    def handle_and_update_rout(route: Route):
        title_update = 'updatetd_tab_title'
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = title_update
        body = json.dumps(body)
        route.fulfill(
           response=response,
            body=body
        )

    page.route('**/digital-mat?path=library/step0_iphone/digitalmat', handle_and_update_rout)
    page.goto('https://www.apple.com/shop/buy-iphone')
    iphone_item = page.get_by_role('heading', name='iPhone 16 Pro &')
    iphone_item.click()

    popup = page.locator(
        '[class="rf-digitalmat-overlay-contentsection"]'
    ).locator('#rf-digitalmat-overlay-label-0').nth(0)
    assert popup.text_content() == 'updatetd_tab_title'
