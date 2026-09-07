import os
import json
import copy
import requests
import base64
import argparse
import urllib3
import sys
import random

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from html_templates import generate_block_1, generate_block_2

# Configuration
WP_URL = "https://wordpress-1380731-5609593.cloudwaysapps.com/wp-json/wp/v2"
USERNAME = "zhanyajun149@gmail.com"
TOKEN = "XrPD ShtD SFNn 6iVP Hnxy PnTT"

def get_headers():
    return {
        'Authorization': f'Basic {base64.b64encode(f"{USERNAME}:{TOKEN}".encode()).decode()}',
        'Content-Type': 'application/json'
    }

def process_template(template_data, brand):
    new_template = copy.deepcopy(template_data)
    new_template['title'] = brand['name']
    
    html_widgets = []
    
    def find_html_widgets(element_list):
        for el in element_list:
            if el.get('widgetType') == 'html' and 'settings' in el and 'html' in el['settings']:
                html_widgets.append(el)
            if 'elements' in el and len(el['elements']) > 0:
                find_html_widgets(el['elements'])

    find_html_widgets(new_template['content'])
    
    for widget in html_widgets:
        html_content = widget['settings']['html']
        if 'kg-brand-block-2' in html_content:
            widget['settings']['html'] = generate_block_2(brand)
        elif 'kg-brand-block-1' in html_content:
            widget['settings']['html'] = generate_block_1(brand)
            
    return new_template

def publish_page(brand_slug, template_path='template.json', brands_path='brands.json'):
    with open(brands_path, 'r', encoding='utf-8') as f:
        brands = json.load(f)
    
    if brand_slug not in brands:
        print(f"Brand '{brand_slug}' not found in {brands_path}")
        return
        
    brand = brands[brand_slug]
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template_data = json.load(f)
        
    print(f"Generating Elementor JSON for {brand['name']}...")
    final_template = process_template(template_data, brand)
    elementor_data_str = json.dumps(final_template['content'])
    
    # Check if page already exists
    headers = get_headers()
    resp = requests.get(f"{WP_URL}/pages?slug={brand_slug}", headers=headers, verify=False)
    page_id = None
    if resp.status_code == 200 and resp.json():
        page_id = resp.json()[0]['id']
        print(f"Found existing page (ID: {page_id}). Updating...")
        url = f"{WP_URL}/pages/{page_id}"
    else:
        print("Creating new page...")
        url = f"{WP_URL}/pages"
        
    # List of allowed author IDs: Tung (33), 思穎 (34), Wade Chen (35)
    available_authors = [33, 34, 35]
    selected_author = random.choice(available_authors)

    payload = {
        'title': f"{brand['name']} 評論",
        'status': 'publish',
        'slug': brand_slug,
        'type': 'page',
        'author': selected_author,
        'meta': {
            '_elementor_edit_mode': 'builder',
            '_elementor_data': elementor_data_str
        },
        'template': 'elementor_header_footer'
    }
    
    resp = requests.post(url, headers=headers, json=payload, verify=False)
    if resp.status_code in [200, 201]:
        print(f"✅ Success! URL: {resp.json().get('link')}")
    else:
        print(f"❌ Failed: {resp.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Publish Elementor Brand Page')
    parser.add_argument('brand_slug', help='The slug of the brand defined in brands.json (e.g. e88games)')
    args = parser.parse_args()
    publish_page(args.brand_slug)
