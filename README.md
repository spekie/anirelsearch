# Anime Releases Search
> [!NOTE]
> Not all anime are available

A very simple CLI anime releases search tool based on [AniList](https://anilist.co) API and [SeaDex](https://releases.moe) index.

## Usage

Using nix-shell

```
nix-shell --command 'python3 anime_releases_search.py'
```

## How It Works

This script will ask for anime name and then will open a browser tab window with the best possible release.

## Dependencies

- [requests](https://requests.readthedocs.io)
