const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  //publicPath: "/static/",
  publicPath: process.env.PUBLIC_PATH,
  //publicPath: "http://192.168.1.64:8080",

  css: {
    sourceMap: true,
    // loaderOptions: {
    //   sass: {
    //     prependData: `
    //     $primary: #3273dc;
    //     @import '~bulma';
    //     @import '@/styles/flex-styles.scss';
    //     @import '@/styles/global-styles.scss';
    //     `
    //   }
    // }
  },

  outputDir: "dist/",

  chainWebpack: (config) => {
    config
      .plugin("BundleTracker")
      .use(BundleTracker, [{ filename: "webpack-stats.json" }])
      .tap(output => {
        output.crossOriginLoading = 'anonymous';
        return output;
      });

    config.resolve.alias.set("__STATIC__", "static");

    config.devServer
      .public("http://0.0.0.0:8080")
      .host("0.0.0.0")
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .headers({ "Access-Control-Allow-Origin": ["*"] });
  },
};
