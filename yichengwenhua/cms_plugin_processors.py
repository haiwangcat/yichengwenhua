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
    
    str = begin + unicode(rendered_content) + end
    dom = xml.dom.minidom.parseString(str.encode('utf-8'))

    counter = 0
    
    toRemove = []
    
    div = dom.childNodes[0]
    newSpan = dom.createElement('div')
    newSpan.setAttribute('class', 'content-text')
    div.insertBefore(newSpan, div.childNodes[0])
            
    for child in div.childNodes:
        if child.__class__.__name__ == 'Text': continue
        #print dir(child)
        if child.tagName == 'h3':
            counter = counter + 1
            
            newDiv = dom.createElement('div')
            newDiv.setAttribute('class', 'section-title')
            #newDiv.setAttribute('id', 'section-title' + unicode(counter))
            
            # Create a new div to show the left border
            innerDiv = dom.createElement('div')
            newDiv.appendChild(innerDiv)
            
            a = dom.createElement('a')
            a.setAttribute('href', 'javascript:;')
            
            a.appendChild(child.cloneNode(True))
            innerDiv.appendChild(a)
            
            div.replaceChild(newDiv, child)
                        
            newSpan = dom.createElement('div')
            newSpan.setAttribute('class', 'content-text')
            div.insertBefore(newSpan, newDiv.nextSibling)
            
        elif child.tagName != 'div':
            #if counter == 0: continue
            newSpan.appendChild(child.cloneNode(True))
            toRemove.append((div, child))
            #div.removeChild(child)
            #child.setAttribute('class', 'section-content' + unicode(counter))
            
    for (parent, child) in toRemove:
        parent.removeChild(child)
        
        
    output = dom.toxml()
    output = output.split(begin)[-1].split(end)[0]
    #print output
    return output
    
    
    
def process_heritage_video(instance, placeholder, rendered_content, original_context):
    '''
    Process the videos on culture heritage page.
    '''
    if placeholder.slot != 'heritage-text' or (instance._render_meta.text_enabled and instance.parent):
        return rendered_content
        
    
    import xml.etree.ElementTree as ET
    import xml.dom.minidom

    