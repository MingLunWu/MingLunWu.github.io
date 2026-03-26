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

Article-page structure customizations should live in `layouts/_default/single.html` and local partials in `layouts/partials/`.

Current article-specific partials:

1. `layouts/partials/post-related-notes.html`
2. `layouts/partials/post-comments.html`
3. `layouts/partials/post-newsletter.html`

Article-page integrations are configured in `config.toml`:

1. `params.utterances`
2. `params.newsletter`

Sidebar structure is overridden locally in `layouts/partials/sidebar.html` and split into:

1. `layouts/partials/sidebar-profile.html`
2. `layouts/partials/sidebar-links.html`
3. `layouts/partials/sidebar-featured-tags.html`
4. `layouts/partials/sidebar-friends.html`
