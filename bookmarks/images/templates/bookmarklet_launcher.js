(function(){
    if(window.myBookmarklet!==undefined){
        myBookmarklet();
    }
    else{
        document.body.appendChild(document.createElement('script')).src='http://172.20.200.20:8111/static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
    }
})();