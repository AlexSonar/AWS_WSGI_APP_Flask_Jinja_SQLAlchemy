## npm init
```
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg> --save` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
name: (Simple_Site) 
Sorry, name can no longer contain capital letters.
name: (Simple_Site) simple_site
version: (1.0.0) 
description: simple site on Flask
entry point: (index.js) 
test command: testex
git repository: 
keywords: siteex
author: Alex Sonar
license: (ISC) 
About to write to /home/alex/Documents/ENV_Study/Python_Flask/Simple_Site/package.json:

{
  "name": "simple_site",
  "version": "1.0.0",
  "description": "simple site on Flask",
  "main": "index.js",
  "directories": {
    "doc": "doc"
  },
  "scripts": {
    "test": "testex"
  },
  "keywords": [
    "siteex"
  ],
  "author": "Alex Sonar",
  "license": "ISC"
}


Is this ok? (yes) y
```

## npm i --save-dev gulp gulp-sass

```
npm WARN deprecated chokidar@2.1.8: Chokidar 2 will break on node v14+. Upgrade to chokidar 3 with 15x less dependencies.
npm WARN deprecated resolve-url@0.2.1: https://github.com/lydell/resolve-url#deprecated
npm WARN deprecated urix@0.1.0: Please see https://github.com/lydell/urix#deprecated
npm WARN deprecated request@2.88.2: request has been deprecated, see https://github.com/request/request/issues/3142
npm WARN prefer global node-gyp@3.8.0 should be installed with -g

> node-sass@4.14.1 install /home/alex/Documents/ENV_Study/Python_Flask/Simple_Site/node_modules/node-sass
> node scripts/install.js

Cached binary found at /home/alex/.npm/node-sass/4.14.1/linux-x64-57_binding.node

> node-sass@4.14.1 postinstall /home/alex/Documents/ENV_Study/Python_Flask/Simple_Site/node_modules/node-sass
> node scripts/build.js

Binary found at /home/alex/Documents/ENV_Study/Python_Flask/Simple_Site/node_modules/node-sass/vendor/linux-x64-57/binding.node
```
```
Testing binary
Binary is fine
simple_site@1.0.0 /home/alex/Documents/ENV_Study/Python_Flask/Simple_Site
├─┬ gulp@4.0.2 
│ ├─┬ glob-watcher@5.0.3 
│ │ ├─┬ anymatch@2.0.0 
│ │ │ ├─┬ micromatch@3.1.10 
│ │ │ │ ├── array-unique@0.3.2 
│ │ │ │ ├─┬ define-property@2.0.2 
│ │ │ │ │ └─┬ is-descriptor@1.0.2 
│ │ │ │ │   ├── is-accessor-descriptor@1.0.0 
│ │ │ │ │   └── is-data-descriptor@1.0.0 
│ │ │ │ ├─┬ extglob@2.0.4 
│ │ │ │ │ ├─┬ define-property@1.0.0 
│ │ │ │ │ │ └─┬ is-descriptor@1.0.2 
│ │ │ │ │ │   ├── is-accessor-descriptor@1.0.0 
│ │ │ │ │ │   └── is-data-descriptor@1.0.0 
│ │ │ │ │ ├─┬ expand-brackets@2.1.4 
│ │ │ │ │ │ ├── define-property@0.2.5 
│ │ │ │ │ │ ├── extend-shallow@2.0.1 
│ │ │ │ │ │ └── posix-character-classes@0.1.1 
│ │ │ │ │ └── extend-shallow@2.0.1 
│ │ │ │ ├─┬ fragment-cache@0.2.1 
│ │ │ │ │ └── map-cache@0.2.2 
│ │ │ │ ├── kind-of@6.0.3 
│ │ │ │ ├── nanomatch@1.2.13 
│ │ │ │ ├── object.pick@1.3.0 
│ │ │ │ ├─┬ regex-not@1.0.2 
│ │ │ │ │ └─┬ safe-regex@1.1.0 
│ │ │ │ │   └── ret@0.1.15 
│ │ │ │ ├─┬ snapdragon@0.8.2 
│ │ │ │ │ ├─┬ base@0.11.2 
│ │ │ │ │ │ ├─┬ cache-base@1.0.1 
│ │ │ │ │ │ │ ├─┬ collection-visit@1.0.0 
│ │ │ │ │ │ │ │ ├── map-visit@1.0.0 
│ │ │ │ │ │ │ │ └── object-visit@1.0.1 
│ │ │ │ │ │ │ ├─┬ has-value@1.0.0 
│ │ │ │ │ │ │ │ └─┬ has-values@1.0.0 
│ │ │ │ │ │ │ │   └── kind-of@4.0.0 
│ │ │ │ │ │ │ ├─┬ set-value@2.0.1 
│ │ │ │ │ │ │ │ └── extend-shallow@2.0.1 
│ │ │ │ │ │ │ ├─┬ to-object-path@0.3.0 
│ │ │ │ │ │ │ │ └── kind-of@3.2.2 
│ │ │ │ │ │ │ ├── union-value@1.0.1 
│ │ │ │ │ │ │ └─┬ unset-value@1.0.0 
│ │ │ │ │ │ │   └─┬ has-value@0.3.1 
│ │ │ │ │ │ │     ├── has-values@0.1.4 
│ │ │ │ │ │ │     └── isobject@2.1.0 
│ │ │ │ │ │ ├─┬ class-utils@0.3.6 
│ │ │ │ │ │ │ ├── define-property@0.2.5 
│ │ │ │ │ │ │ └─┬ static-extend@0.1.2 
│ │ │ │ │ │ │   ├── define-property@0.2.5 
│ │ │ │ │ │ │   └─┬ object-copy@0.1.0 
│ │ │ │ │ │ │     ├── copy-descriptor@0.1.1 
│ │ │ │ │ │ │     ├── define-property@0.2.5 
│ │ │ │ │ │ │     └── kind-of@3.2.2 
│ │ │ │ │ │ ├── component-emitter@1.3.0 
│ │ │ │ │ │ ├─┬ define-property@1.0.0 
│ │ │ │ │ │ │ └─┬ is-descriptor@1.0.2 
│ │ │ │ │ │ │   ├── is-accessor-descriptor@1.0.0 
│ │ │ │ │ │ │   └── is-data-descriptor@1.0.0 
│ │ │ │ │ │ ├─┬ mixin-deep@1.3.2 
│ │ │ │ │ │ │ └── is-extendable@1.0.1 
│ │ │ │ │ │ └── pascalcase@0.1.1 
│ │ │ │ │ ├─┬ debug@2.6.9 
│ │ │ │ │ │ └── ms@2.0.0 
│ │ │ │ │ ├─┬ define-property@0.2.5 
│ │ │ │ │ │ └─┬ is-descriptor@0.1.6 
│ │ │ │ │ │   ├─┬ is-accessor-descriptor@0.1.6 
│ │ │ │ │ │   │ └── kind-of@3.2.2 
│ │ │ │ │ │   ├─┬ is-data-descriptor@0.1.4 
│ │ │ │ │ │   │ └── kind-of@3.2.2 
│ │ │ │ │ │   └── kind-of@5.1.0 
│ │ │ │ │ ├── extend-shallow@2.0.1 
│ │ │ │ │ ├─┬ source-map-resolve@0.5.3 
│ │ │ │ │ │ ├── atob@2.1.2 
│ │ │ │ │ │ ├── decode-uri-component@0.2.0 
│ │ │ │ │ │ ├── resolve-url@0.2.1 
│ │ │ │ │ │ ├── source-map-url@0.4.0 
│ │ │ │ │ │ └── urix@0.1.0 
│ │ │ │ │ └── use@3.1.1 
│ │ │ │ └── to-regex@3.0.2 
│ │ │ └── normalize-path@2.1.1 
│ │ ├─┬ async-done@1.3.2 
│ │ │ ├── end-of-stream@1.4.4 
│ │ │ ├─┬ once@1.4.0 
│ │ │ │ └── wrappy@1.0.2 
│ │ │ ├── process-nextick-args@2.0.1 
│ │ │ └── stream-exhaust@1.0.2 
│ │ ├─┬ chokidar@2.1.8 
│ │ │ ├── async-each@1.0.3 
│ │ │ ├─┬ braces@2.3.2 
│ │ │ │ ├─┬ extend-shallow@2.0.1 
│ │ │ │ │ └── is-extendable@0.1.1 
│ │ │ │ ├─┬ fill-range@4.0.0 
│ │ │ │ │ ├── extend-shallow@2.0.1 
│ │ │ │ │ ├─┬ is-number@3.0.0 
│ │ │ │ │ │ └── kind-of@3.2.2 
│ │ │ │ │ ├── repeat-string@1.6.1 
│ │ │ │ │ └── to-regex-range@2.1.1 
│ │ │ │ ├── repeat-element@1.1.3 
│ │ │ │ ├─┬ snapdragon-node@2.1.1 
│ │ │ │ │ ├─┬ define-property@1.0.0 
│ │ │ │ │ │ └─┬ is-descriptor@1.0.2 
│ │ │ │ │ │   ├── is-accessor-descriptor@1.0.0 
│ │ │ │ │ │   └── is-data-descriptor@1.0.0 
│ │ │ │ │ └─┬ snapdragon-util@3.0.1 
│ │ │ │ │   └── kind-of@3.2.2 
│ │ │ │ └── split-string@3.1.0 
│ │ │ ├─┬ glob-parent@3.1.0 
│ │ │ │ ├── is-glob@3.1.0 
│ │ │ │ └── path-dirname@1.0.2 
│ │ │ ├── inherits@2.0.4 
│ │ │ ├─┬ is-binary-path@1.0.1 
│ │ │ │ └── binary-extensions@1.13.1 
│ │ │ ├─┬ is-glob@4.0.1 
│ │ │ │ └── is-extglob@2.1.1 
│ │ │ ├── normalize-path@3.0.0 
│ │ │ ├── path-is-absolute@1.0.1 
│ │ │ ├── readdirp@2.2.1 
│ │ │ └── upath@1.2.0 
│ │ ├── is-negated-glob@1.0.0 
│ │ ├── just-debounce@1.0.0 
│ │ └─┬ object.defaults@1.1.0 
│ │   ├── array-each@1.0.1 
│ │   ├── array-slice@1.1.0 
│ │   └─┬ for-own@1.0.0 
│ │     └── for-in@1.0.2 
│ ├─┬ gulp-cli@2.3.0 
│ │ ├─┬ ansi-colors@1.1.0 
│ │ │ └── ansi-wrap@0.1.0 
│ │ ├── archy@1.0.0 
│ │ ├─┬ array-sort@1.0.0 
│ │ │ ├─┬ default-compare@1.0.0 
│ │ │ │ └── kind-of@5.1.0 
│ │ │ ├── get-value@2.0.6 
│ │ │ └── kind-of@5.1.0 
│ │ ├── color-support@1.1.3 
│ │ ├─┬ concat-stream@1.6.2 
│ │ │ ├── buffer-from@1.1.1 
│ │ │ └── typedarray@0.0.6 
│ │ ├─┬ copy-props@2.0.4 
│ │ │ ├── each-props@1.3.2 
│ │ │ └── is-plain-object@2.0.4 
│ │ ├─┬ fancy-log@1.3.3 
│ │ │ ├── ansi-gray@0.1.1 
│ │ │ ├── parse-node-version@1.0.1 
│ │ │ └── time-stamp@1.1.0 
│ │ ├─┬ gulplog@1.0.0 
│ │ │ └─┬ glogg@1.0.2 
│ │ │   └── sparkles@1.0.1 
│ │ ├── interpret@1.4.0 
│ │ ├── isobject@3.0.1 
│ │ ├─┬ liftoff@3.1.0 
│ │ │ ├── extend@3.0.2 
│ │ │ ├─┬ findup-sync@3.0.0 
│ │ │ │ ├── detect-file@1.0.0 
│ │ │ │ └─┬ resolve-dir@1.0.1 
│ │ │ │   └─┬ global-modules@1.0.0 
│ │ │ │     └─┬ global-prefix@1.0.2 
│ │ │ │       └── ini@1.3.5 
│ │ │ ├─┬ fined@1.2.0 
│ │ │ │ ├── expand-tilde@2.0.2 
│ │ │ │ └─┬ parse-filepath@1.0.2 
│ │ │ │   └─┬ path-root@0.1.1 
│ │ │ │     └── path-root-regex@0.1.2 
│ │ │ ├── flagged-respawn@1.0.1 
│ │ │ ├── object.map@1.0.1 
│ │ │ ├── rechoir@0.6.2 
│ │ │ └─┬ resolve@1.17.0 
│ │ │   └── path-parse@1.0.6 
│ │ ├─┬ matchdep@2.0.0 
│ │ │ ├─┬ findup-sync@2.0.0 
│ │ │ │ └── is-glob@3.1.0 
│ │ │ └── stack-trace@0.0.10 
│ │ ├── mute-stdout@1.0.1 
│ │ ├── pretty-hrtime@1.0.3 
│ │ ├─┬ replace-homedir@1.0.0 
│ │ │ ├─┬ homedir-polyfill@1.0.3 
│ │ │ │ └── parse-passwd@1.0.0 
│ │ │ ├─┬ is-absolute@1.0.0 
│ │ │ │ ├─┬ is-relative@1.0.0 
│ │ │ │ │ └─┬ is-unc-path@1.0.0 
│ │ │ │ │   └── unc-path-regex@0.1.2 
│ │ │ │ └── is-windows@1.0.2 
│ │ │ └── remove-trailing-separator@1.1.0 
│ │ ├─┬ semver-greatest-satisfied-range@1.1.0 
│ │ │ └── sver-compat@1.5.0 
│ │ ├── v8flags@3.2.0 
│ │ └─┬ yargs@7.1.1 
│ │   ├── camelcase@3.0.0 
│ │   ├─┬ cliui@3.2.0 
│ │   │ └── wrap-ansi@2.1.0 
│ │   ├── decamelize@1.2.0 
│ │   ├── get-caller-file@1.0.3 
│ │   ├─┬ os-locale@1.4.0 
│ │   │ └─┬ lcid@1.0.0 
│ │   │   └── invert-kv@1.0.0 
│ │   ├─┬ read-pkg-up@1.0.1 
│ │   │ ├─┬ find-up@1.1.2 
│ │   │ │ ├── path-exists@2.1.0 
│ │   │ │ └─┬ pinkie-promise@2.0.1 
│ │   │ │   └── pinkie@2.0.4 
│ │   │ └─┬ read-pkg@1.1.0 
│ │   │   ├─┬ load-json-file@1.1.0 
│ │   │   │ ├─┬ parse-json@2.2.0 
│ │   │   │ │ └─┬ error-ex@1.3.2 
│ │   │   │ │   └── is-arrayish@0.2.1 
│ │   │   │ ├── pify@2.3.0 
│ │   │   │ └── strip-bom@2.0.0 
│ │   │   └── path-type@1.1.0 
│ │   ├── require-directory@2.1.1 
│ │   ├── require-main-filename@1.0.1 
│ │   ├── set-blocking@2.0.0 
│ │   ├─┬ string-width@1.0.2 
│ │   │ ├── code-point-at@1.1.0 
│ │   │ └─┬ is-fullwidth-code-point@1.0.0 
│ │   │   └── number-is-nan@1.0.1 
│ │   ├── which-module@1.0.0 
│ │   ├── y18n@3.2.1 
│ │   └── yargs-parser@5.0.0-security.0 
│ ├─┬ undertaker@1.2.1 
│ │ ├── arr-flatten@1.1.0 
│ │ ├─┬ arr-map@2.0.2 
│ │ │ └── make-iterator@1.0.1 
│ │ ├─┬ bach@1.2.0 
│ │ │ ├── arr-filter@1.1.2 
│ │ │ ├─┬ array-initial@1.1.0 
│ │ │ │ └── is-number@4.0.0 
│ │ │ ├─┬ array-last@1.3.0 
│ │ │ │ └── is-number@4.0.0 
│ │ │ ├── async-settle@1.0.0 
│ │ │ └── now-and-later@2.0.1 
│ │ ├── collection-map@1.0.0 
│ │ ├─┬ es6-weak-map@2.0.3 
│ │ │ ├─┬ d@1.0.1 
│ │ │ │ └── type@1.2.0 
│ │ │ ├─┬ es5-ext@0.10.53 
│ │ │ │ └── next-tick@1.0.0 
│ │ │ ├── es6-iterator@2.0.3 
│ │ │ └─┬ es6-symbol@3.1.3 
│ │ │   └─┬ ext@1.4.0 
│ │ │     └── type@2.0.0 
│ │ ├─┬ last-run@1.1.1 
│ │ │ └── default-resolution@2.0.0 
│ │ ├── object.reduce@1.0.1 
│ │ └── undertaker-registry@1.0.1 
│ └─┬ vinyl-fs@3.0.3 
│   ├── fs-mkdirp-stream@1.0.0 
│   ├─┬ glob-stream@6.1.0 
│   │ ├── ordered-read-streams@1.0.1 
│   │ ├── to-absolute-glob@2.0.2 
│   │ └─┬ unique-stream@2.3.1 
│   │   ├── json-stable-stringify-without-jsonify@1.0.1 
│   │   └── through2-filter@3.0.0 
│   ├── graceful-fs@4.2.4 
│   ├── is-valid-glob@1.0.0 
│   ├── lazystream@1.0.0 
│   ├─┬ lead@1.0.0 
│   │ └── flush-write-stream@1.1.1 
│   ├─┬ object.assign@4.1.0 
│   │ ├── define-properties@1.1.3 
│   │ ├── function-bind@1.1.1 
│   │ ├── has-symbols@1.0.1 
│   │ └── object-keys@1.1.1 
│   ├─┬ pumpify@1.5.1 
│   │ ├─┬ duplexify@3.7.1 
│   │ │ └── stream-shift@1.0.1 
│   │ └── pump@2.0.1 
│   ├─┬ readable-stream@2.3.7 
│   │ ├── core-util-is@1.0.2 
│   │ ├── isarray@1.0.0 
│   │ ├── safe-buffer@5.1.2 
│   │ ├── string_decoder@1.1.1 
│   │ └── util-deprecate@1.0.2 
│   ├─┬ remove-bom-buffer@3.0.0 
│   │ ├── is-buffer@1.1.6 
│   │ └── is-utf8@0.2.1 
│   ├── remove-bom-stream@1.2.0 
│   ├── resolve-options@1.1.0 
│   ├── to-through@2.0.0 
│   ├── value-or-function@3.0.0 
│   ├─┬ vinyl@2.2.0 
│   │ ├── clone@2.1.2 
│   │ ├── clone-buffer@1.0.0 
│   │ ├── clone-stats@1.0.0 
│   │ └── cloneable-readable@1.1.3 
│   └─┬ vinyl-sourcemap@1.1.0 
│     ├─┬ append-buffer@1.0.2 
│     │ └── buffer-equal@1.0.0 
│     └── convert-source-map@1.7.0 
└─┬ gulp-sass@4.1.0 
  ├─┬ chalk@2.4.2 
  │ ├─┬ ansi-styles@3.2.1 
  │ │ └─┬ color-convert@1.9.3 
  │ │   └── color-name@1.1.3 
  │ ├── escape-string-regexp@1.0.5 
  │ └─┬ supports-color@5.5.0 
  │   └── has-flag@3.0.0 
  ├── lodash@4.17.15 
  ├─┬ node-sass@4.14.1 
  │ ├── async-foreach@0.1.3 
  │ ├─┬ chalk@1.1.3 
  │ │ ├── ansi-styles@2.2.1 
  │ │ ├─┬ has-ansi@2.0.0 
  │ │ │ └── ansi-regex@2.1.1 
  │ │ ├── strip-ansi@3.0.1 
  │ │ └── supports-color@2.0.0 
  │ ├─┬ cross-spawn@3.0.1 
  │ │ ├─┬ lru-cache@4.1.5 
  │ │ │ ├── pseudomap@1.0.2 
  │ │ │ └── yallist@2.1.2 
  │ │ └─┬ which@1.3.1 
  │ │   └── isexe@2.0.0 
  │ ├─┬ gaze@1.1.3 
  │ │ └── globule@1.3.2 
  │ ├── get-stdin@4.0.1 
  │ ├─┬ glob@7.1.6 
  │ │ ├── fs.realpath@1.0.0 
  │ │ ├── inflight@1.0.6 
  │ │ └─┬ minimatch@3.0.4 
  │ │   └─┬ brace-expansion@1.1.11 
  │ │     ├── balanced-match@1.0.0 
  │ │     └── concat-map@0.0.1 
  │ ├── in-publish@2.0.1 
  │ ├─┬ meow@3.7.0 
  │ │ ├─┬ camelcase-keys@2.1.0 
  │ │ │ └── camelcase@2.1.1 
  │ │ ├─┬ loud-rejection@1.6.0 
  │ │ │ ├─┬ currently-unhandled@0.4.1 
  │ │ │ │ └── array-find-index@1.0.2 
  │ │ │ └── signal-exit@3.0.3 
  │ │ ├── map-obj@1.0.1 
  │ │ ├── minimist@1.2.5 
  │ │ ├─┬ normalize-package-data@2.5.0 
  │ │ │ ├── hosted-git-info@2.8.8 
  │ │ │ ├── semver@5.7.1 
  │ │ │ └─┬ validate-npm-package-license@3.0.4 
  │ │ │   ├─┬ spdx-correct@3.1.1 
  │ │ │   │ └── spdx-license-ids@3.0.5 
  │ │ │   └─┬ spdx-expression-parse@3.0.1 
  │ │ │     └── spdx-exceptions@2.3.0 
  │ │ ├── object-assign@4.1.1 
  │ │ ├─┬ redent@1.0.0 
  │ │ │ ├─┬ indent-string@2.1.0 
  │ │ │ │ └─┬ repeating@2.0.1 
  │ │ │ │   └── is-finite@1.1.0 
  │ │ │ └── strip-indent@1.0.1 
  │ │ └── trim-newlines@1.0.0 
  │ ├── mkdirp@0.5.5 
  │ ├── nan@2.14.1 
  │ ├─┬ node-gyp@3.8.0 
  │ │ ├── fstream@1.0.12 
  │ │ ├─┬ nopt@3.0.6 
  │ │ │ └── abbrev@1.1.1 
  │ │ ├─┬ osenv@0.1.5 
  │ │ │ ├── os-homedir@1.0.2 
  │ │ │ └── os-tmpdir@1.0.2 
  │ │ ├── rimraf@2.7.1 
  │ │ ├── semver@5.3.0 
  │ │ └─┬ tar@2.2.2 
  │ │   └── block-stream@0.0.9 
  │ ├─┬ npmlog@4.1.2 
  │ │ ├─┬ are-we-there-yet@1.1.5 
  │ │ │ └── delegates@1.0.0 
  │ │ ├── console-control-strings@1.1.0 
  │ │ └─┬ gauge@2.7.4 
  │ │   ├── aproba@1.2.0 
  │ │   ├── has-unicode@2.0.1 
  │ │   └── wide-align@1.1.3 
  │ ├─┬ request@2.88.2 
  │ │ ├── aws-sign2@0.7.0 
  │ │ ├── aws4@1.10.0 
  │ │ ├── caseless@0.12.0 
  │ │ ├─┬ combined-stream@1.0.8 
  │ │ │ └── delayed-stream@1.0.0 
  │ │ ├── forever-agent@0.6.1 
  │ │ ├─┬ form-data@2.3.3 
  │ │ │ └── asynckit@0.4.0 
  │ │ ├─┬ har-validator@5.1.3 
  │ │ │ ├─┬ ajv@6.12.3 
  │ │ │ │ ├── fast-deep-equal@3.1.3 
  │ │ │ │ ├── fast-json-stable-stringify@2.1.0 
  │ │ │ │ ├── json-schema-traverse@0.4.1 
  │ │ │ │ └── uri-js@4.2.2 
  │ │ │ └── har-schema@2.0.0 
  │ │ ├─┬ http-signature@1.2.0 
  │ │ │ ├── assert-plus@1.0.0 
  │ │ │ ├─┬ jsprim@1.4.1 
  │ │ │ │ ├── extsprintf@1.3.0 
  │ │ │ │ ├── json-schema@0.2.3 
  │ │ │ │ └── verror@1.10.0 
  │ │ │ └─┬ sshpk@1.16.1 
  │ │ │   ├── asn1@0.2.4 
  │ │ │   ├── bcrypt-pbkdf@1.0.2 
  │ │ │   ├── dashdash@1.14.1 
  │ │ │   ├── ecc-jsbn@0.1.2 
  │ │ │   ├── getpass@0.1.7 
  │ │ │   ├── jsbn@0.1.1 
  │ │ │   ├── safer-buffer@2.1.2 
  │ │ │   └── tweetnacl@0.14.5 
  │ │ ├── is-typedarray@1.0.0 
  │ │ ├── isstream@0.1.2 
  │ │ ├── json-stringify-safe@5.0.1 
  │ │ ├─┬ mime-types@2.1.27 
  │ │ │ └── mime-db@1.44.0 
  │ │ ├── oauth-sign@0.9.0 
  │ │ ├── performance-now@2.1.0 
  │ │ ├── qs@6.5.2 
  │ │ ├─┬ tough-cookie@2.5.0 
  │ │ │ ├── psl@1.8.0 
  │ │ │ └── punycode@2.1.1 
  │ │ ├── tunnel-agent@0.6.0 
  │ │ └── uuid@3.4.0 
  │ ├─┬ sass-graph@2.2.5 
  │ │ ├─┬ scss-tokenizer@0.2.3 
  │ │ │ ├── js-base64@2.6.2 
  │ │ │ └─┬ source-map@0.4.4 
  │ │ │   └── amdefine@1.0.1 
  │ │ └─┬ yargs@13.3.2 
  │ │   ├─┬ cliui@5.0.0 
  │ │   │ ├─┬ strip-ansi@5.2.0 
  │ │   │ │ └── ansi-regex@4.1.0 
  │ │   │ └── wrap-ansi@5.1.0 
  │ │   ├─┬ find-up@3.0.0 
  │ │   │ └─┬ locate-path@3.0.0 
  │ │   │   ├─┬ p-locate@3.0.0 
  │ │   │   │ └─┬ p-limit@2.3.0 
  │ │   │   │   └── p-try@2.2.0 
  │ │   │   └── path-exists@3.0.0 
  │ │   ├── get-caller-file@2.0.5 
  │ │   ├── require-main-filename@2.0.0 
  │ │   ├─┬ string-width@3.1.0 
  │ │   │ ├── emoji-regex@7.0.3 
  │ │   │ └── is-fullwidth-code-point@2.0.0 
  │ │   ├── which-module@2.0.0 
  │ │   ├── y18n@4.0.0 
  │ │   └─┬ yargs-parser@13.1.2 
  │ │     └── camelcase@5.3.1 
  │ ├── stdout-stream@1.4.1 
  │ └── true-case-path@1.0.3 
  ├─┬ plugin-error@1.0.1 
  │ ├── arr-diff@4.0.0 
  │ ├── arr-union@3.1.0 
  │ └─┬ extend-shallow@3.0.2 
  │   ├── assign-symbols@1.0.0 
  │   └── is-extendable@1.0.1 
  ├── replace-ext@1.0.1 
  ├─┬ strip-ansi@4.0.0 
  │ └── ansi-regex@3.0.0 
  ├─┬ through2@2.0.5 
  │ └── xtend@4.0.2 
  └─┬ vinyl-sourcemaps-apply@0.2.1 
    └── source-map@0.5.7 

npm WARN optional Skipping failed optional dependency /chokidar/fsevents:
npm WARN notsup Not compatible with your operating system or architecture: fsevents@1.2.13
npm WARN simple_site@1.0.0 No repository field.

```
# ERRORS
node ./node_modules/gulp/bin/gulp.js
[14:21:17] No gulpfile found

# ERRORS
node ./gulp.js
module.js:549
    throw err;
    ^

Error: Cannot find module 'gulp-cli'
    at Function.Module._resolveFilename (module.js:547:15)
    at Function.Module._load (module.js:474:25)
    at Module.require (module.js:596:17)
    at require (internal/module.js:11:18)
    at Object.<anonymous> (/home/alex/Documents/ENV_Study/Python_Flask/Simple_Site/gulp.js:3:1)
    at Module._compile (module.js:652:30)
    at Object.Module._extensions..js (module.js:663:10)
    at Module.load (module.js:565:32)
    at tryModuleLoad (module.js:505:12)

## sudo npm install -g npm@latest
## sudo npm install -g gulp@latest
## sudo npm install --global gulp-cli

npm WARN deprecated resolve-url@0.2.1: https://github.com/lydell/resolve-url#deprecated
npm WARN deprecated urix@0.1.0: Please see https://github.com/lydell/urix#deprecated
npm ERR! code EEXIST
npm ERR! syscall symlink
npm ERR! path ../lib/node_modules/gulp-cli/bin/gulp.js
npm ERR! dest /usr/local/bin/gulp
npm ERR! errno -17
npm ERR! EEXIST: file already exists, symlink '../lib/node_modules/gulp-cli/bin/gulp.js' -> '/usr/local/bin/gulp'
npm ERR! File exists: /usr/local/bin/gulp
npm ERR! Remove the existing file and try again, or run npm
npm ERR! with --force to overwrite files recklessly.

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/alex/.npm/_logs/2020-07-06T11_16_22_962Z-debug.log


This error means that gulp doesn't find gulpfile.js to follow the instructions. To solve this error we need to add gulpfile.js to our directory root by running the command.

Create gulpfile.js and then add

var gulp = require('gulp');
gulp.task('default', function () { 
    console.log('Hello Gulp!') 
});


https://stackoverflow.com/questions/38937095/no-gulpfile-found/47406977

I encountered same problem in Laravel 6. I solved it by steps:
```
npm init
npm install --save-dev gulp
npx mkdirp yourProjectName
npm install --save-dev gulp
```

Create a gulpfile:Using your text editor, create a file named gulpfile.js in your project root with these contents:

```
function defaultTask(cb) {
  // place code for your default task here
  cb();
}
```
exports.default = defaultTask

Full Resource here: https://gulpjs.com/docs/en/getting-started/quick-start

Hope this helps ypu

# sudo npm install --global gulp-cli

create the gulpfile.js
```
with:
function defaultTask(cb) {
    // place code for your default task here
    cb();
  }
  
exports.default = defaultTask
```

```
var gulp = require('gulp'), 
		sass = require('gulp-sass'); 

gulp.task('sass', function() { 
	return gulp.src(['sass/**/*.sass', 'sass/**/*.scss']) 
		.pipe(sass({outputStyle: 'expanded'}).on('error', sass.logError)) 
		.pipe(gulp.dest('css')) 
	});

gulp.task('watch', function() {
	gulp.watch(['sass/**/*.sass', 'sass/**/*.scss'], gulp.parallel('sass')); 
});

gulp.task('default', gulp.parallel('watch'));

```
# node ./node_modules/gulp/bin/gulp.js
[14:41:38] Using gulpfile ~/Documents/ENV_Study/Python_Flask/Simple_Site/gulpfile.js
[14:41:38] Starting 'default'...
[14:41:38] Finished 'default' after 1.87 ms