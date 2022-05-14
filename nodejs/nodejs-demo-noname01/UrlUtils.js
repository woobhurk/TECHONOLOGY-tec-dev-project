class UrlUtils {
    static getUrlMap(url = "") {
        let splitIndex = url.indexOf("?");
        let urlMap = {};

        if (splitIndex >= 0 && splitIndex < url.length - 1) {
            let keyValueStr = url.substr(splitIndex + 1);
            let keyValuePairs = keyValueStr.split("&");

            for (let keyValuePair of keyValuePairs) {
                let key = keyValuePair.split("=")[0];
                let value = keyValuePair.split("=")[1];

                urlMap[key] = value;
            }
        }

        return urlMap;
    }
}

module.exports = UrlUtils;
