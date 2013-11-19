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