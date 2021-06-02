const {createProxyMiddleware} = require("http-proxy-middleware");

module.exports = function (app){
    app.use(
        "/api/**",
        createProxyMiddleware({
            target:"http://backend:5000",
            pathRewrite:{
                "^/api":"", //remove 'api' from requests
            },
        })
    )
}