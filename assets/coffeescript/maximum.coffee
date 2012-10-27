class MaximumIdol
    constructor: ->
        @stack = []
        @elements =
            body: $(document.body)

        @elements.body.addClass 'onready'
        $(window).load =>
            @elements.body.removeClass('loading').addClass('loaded') if @elements.body.hasClass('loading')

        @navigate()
        @buffer()

    preload: (url) ->
        image = new Image()
        image.src = url

    buffer: ->
        for i in [0 .. 2 - @stack.length] by 1
            $.getJSON '/fetch?' + i, (data) =>
                @stack.push({url: data.idol})
                @preload(data.idol)
                console.log('adding ' + data.idol)
                console.log(@stack)

    navigate: ->
        console.log 'navigated!'
        $('body').on 'click', 'a.gif', (e) =>
            @randomize()
            e.preventDefault()

    randomize: =>
        console.log 'randomized!'
        if @stack.length > 0
            @update(@stack[0].url)
            @stack.splice(0,1)
            @buffer()
        else
            $.getJSON('/fetch', (data) =>
                @update(data.idol)
            ).error ->
                window.location.href = '/random'
            @buffer()

    update: (newURL) ->
        oldGif = $('a.gif')
        newGif = oldGif.clone()
        newGif.addClass('new-gif').css('backgroundImage', 'url(\'' + newURL + '\')')
        oldGif.addClass('old-gif').before(newGif)
        oldGif.fadeOut 150, ->
            oldGif.detach()
            newGif.removeClass 'new-gif'
        _gauges.push(['track']);
        _gaq.push(['_trackPageview', '/']);


$(window).ready ->
    new MaximumIdol
