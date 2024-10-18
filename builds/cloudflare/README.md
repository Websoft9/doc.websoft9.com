# CloudFlare

This is JS repository for CloudFlare worker

## Build

```
cp -f docs/reference/_include/dockerhub-proxy.md builds/cloudflare/src/backends.md
cd builds/cloudflare
npm install --save-dev webpack webpack-cli raw-loader
npm run build
```

## Upload to Cloudflare Worker

You should upload `dist/bundle.js` to Cloudflare Worker after npm build by Github action 