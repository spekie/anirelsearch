#!/usr/bin/env python3
import sys
import webbrowser
import requests

URL = 'https://graphql.anilist.co'

SEARCH_QUERY = '''
query ($search: String) {
  Page(perPage: 10) {
    media(search: $search, type: ANIME) {
      id
      title {
        romaji
        english
        native
      }
    }
  }
}
'''

def search_anime(term: str) -> list[dict]:
    resp = requests.post(URL, json={'query': SEARCH_QUERY, 'variables': {'search': term}})
    resp.raise_for_status()
    return resp.json()['data']['Page']['media']

def choose_entry(results: list[dict]) -> dict | None:
    if not results:
        print("No matches found.")
        return None
    for i, entry in enumerate(results, start=1):
        t = entry['title']
        name = t['english'] or t['romaji'] or t['native']
        print(f"[{i}] {name} (id: {entry['id']})")
    choice = input("\nPick a number (or press Enter to quit): ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(results):
        return results[int(choice) - 1]
    return None

def create_url(entry_id: int) -> str:
    # THE BEST RELEASES 
    return f"https://releases.moe/{entry_id}"

def main():
    term = ' '.join(sys.argv[1:]) or input("Type anime name (can be native, english, or romaji): ")
    results = search_anime(term)
    selected = choose_entry(results)

    if selected:
        link = create_url(selected['id'])
        print(f"Opening {link} ...")
        webbrowser.open(link)

if __name__ == '__main__':
    main()
