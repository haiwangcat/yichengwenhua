def process_heritage_text(instance, placeholder, rendered_content, original_context):
    '''
    Process the text on culture heritage page.
    '''
    if placeholder.slot != 'heritage-text' or (instance._render_meta.text_enabled and instance.parent):
        return rendered_content
        
    
    import xml.etree.ElementTree as ET
    import xml.dom.minidom
    
    begin = unicode("<foo>")
    end = unicode("</foo>")
    
    print rendered_content.__class__.__name__
    
    str = begin + unicode(rendered_content) + end
    dom = xml.dom.minidom.parseString(str.encode('utf-8'))
    
    
    counter = 0
    
    div = dom.childNodes[0]
    for child in div.childNodes:
        if child.tagName == 'h3':
            counter = counter + 1
            
            newDiv = dom.createElement('div')
            newDiv.setAttribute('class', 'section-title')
            #newDiv.setAttribute('id', 'section-title' + unicode(counter))
            
            a = dom.createElement('a')
            a.setAttribute('href', 'javascript:;')
            
            a.appendChild(child.cloneNode(True))
            newDiv.appendChild(a)
            
            div.replaceChild(newDiv, child)
        '''
        elif child.tagName == 'p':
            if counter == 0: continue
            child.setAttribute('class', 'section-content' + unicode(counter))
        '''
        
    output = dom.toxml()
    output = output.split(begin)[-1].split(end)[0]
    #print output
    return output
    