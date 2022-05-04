# Website

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

### Installation

```
$ yarn
```

### Local Development

```
$ npm run start -- --host 0.0.0.0  --port 3002
$ npm run start -- --host 0.0.0.0  --port 3002  --locale en
$ yarn run write-translations -- --locale zh-cn
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Update
有两个方案：

方案1： yarn upgrade @docusaurus/core@latest @docusaurus/preset-classic@latest
方案2：修改 package.json 文件中的版本至指定版本号，然后运行 `yarn install`，再运行 `npx docusaurus --version` 查询版本

### i18n

```
npm run write-translations -- --locale en
```

### Build

```
$ yarn build
$ npm run serve -- --host 0.0.0.0  --port 3003

```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

Using SSH:

```
$ USE_SSH=true yarn deploy
```

Not using SSH:

```
$ GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.
