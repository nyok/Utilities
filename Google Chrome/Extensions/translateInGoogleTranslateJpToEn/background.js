// Set up context menu at install time.
chrome.runtime.onInstalled.addListener(function() {
	var id = chrome.contextMenus.create({
		"title": "「%s」→ EN", 
		"contexts":["selection"],
		"id": "context"
	});
});

// add click event
chrome.contextMenus.onClicked.addListener(
	onClickHandler
);

// The onClicked callback function.
function onClickHandler(info, tab) {
	var sText = info.selectionText;
	var url = "https://translate.google.com/#ja/en/" + encodeURIComponent(sText);	
	window.open(url, '_blank');
};