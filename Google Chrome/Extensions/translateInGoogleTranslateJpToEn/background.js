chrome.runtime.onInstalled.addListener(function() {
    chrome.contextMenus.create({
		"title": "「%s」→ EN", 
		"contexts":["selection"],
		"id": "context"
    });
});
    
chrome.contextMenus.onClicked.addListener(function(info, tab) {
    chrome.tabs.create({  
        url: "https://translate.google.com/#ja/en/" + encodeURIComponent(info.selectionText)
    });
})