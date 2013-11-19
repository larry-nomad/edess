var TemplateRender = function(template, data) {
    for(var i in data) {
        if(!data.hasOwnProperty(i)) {
            continue;
        }
        var reg = new RegExp('\\$\\{' + i + '\\}', 'g');
        template = template.replace(reg, data[i]);
    }
    return template;
};

$( document ).on( "pageinit", "#page-list", function() {
    $( document ).on( "swipeleft swiperight", "#page-list", function( e ) {
        // We check if there is no open panel on the page because otherwise
        // a swipe to close the left panel would also open the right panel (and v.v.).
        // We do this by checking the data that the framework stores on the page element (panel: open).
        if ( $.mobile.activePage.jqmData( "panel" ) !== "open" ) {
            if ( e.type === "swipeleft"  ) {
                $( "#right-panel" ).panel( "open" );
            } else if ( e.type === "swiperight" ) {
                $( "#left-panel" ).panel( "open" );
            }
        }
    });
});
