# Byte and Ink

This repository contains the Hugo source for [minglunwu.com](https://minglunwu.com).

## Local development

Preview the site locally:

```bash
hugo serve
```

Create a production build locally if needed:

```bash
hugo --minify
```

`public/` is a generated build artifact and should not be committed.

## Deployment

Production deployment is handled by GitHub Actions in [`.github/workflows/gh-pages.yml`](./.github/workflows/gh-pages.yml).

The current workflow is:

1. Push source changes to `master`.
2. GitHub Actions runs `hugo --minify`.
3. The generated site is deployed to GitHub Pages.

## Customization

Site-specific style customizations should live in `static/css/custom.css`.

The theme loads extra styles through `params.custom_css` in `config.toml`, so prefer changing files in this repository instead of editing the theme submodule directly.
