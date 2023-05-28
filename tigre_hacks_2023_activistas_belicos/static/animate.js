$('#config-display-button>i').click(()=> {
    if($('#config-display-button>i').hasClass('bars')) {
        showMenu()
        return
    }
    hideMenu()
});

$('.option-list>.cuenta').click(()=>{
    $('#cuenta').modal('show')
})

$('#changePass').click(()=>{
    $('#cuenta').modal('hide')
    $('#modal-changepass').modal({
        onHidden: ()=>{
            $('#modal-changepass').modal('hide')
            $('#cuenta').modal('show')
        }
    }).modal('show')
})

$('#cancelar-changepass').click(()=>{
    $('#modal-changepass').modal('hide')
})

$('.element.soporte').click(()=>{
    window.open('mailto:angel.duronqr@uanl.edu.mx')
})

$('.element.premium').click(()=>{
    $('#modal-planes').modal('show')
})

$('.ui.dropdown').dropdown()

function showMenu() {
    if(animando) return
    $('#config-display-button>i').removeClass('bars')
    $('#config-display-button>i').addClass('close')
    animando = true
    $('#config-display').animate({
        right: '0px'
    }, ()=> {
        animando = false
    })
}

function hideMenu() {
    if(animando) return
    $('#config-display-button>i').removeClass('close')
    $('#config-display-button>i').addClass('bars')
    animando = true
    $('#config-display').animate({
        right: '-400px'
    }, ()=> {
        animando = false
    })
}
