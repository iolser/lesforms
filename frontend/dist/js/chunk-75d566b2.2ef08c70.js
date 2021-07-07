(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-75d566b2"],{1995:function(e,t,c){"use strict";var a=c("7a23"),o={class:"field is-grouped is-grouped-centered"},i={class:"control"},n={key:0,class:"control"},r={key:1,class:"control"},s={key:2,class:"control"};function l(e,t,c,l,d,u){var b=this,m=Object(a["resolveComponent"])("Notification");return Object(a["openBlock"])(),Object(a["createBlock"])("div",null,[c.error?(Object(a["openBlock"])(),Object(a["createBlock"])("div",{key:0,class:["flex row ca snackbar ontop",c.floatBottom?"bottom":"top"]},[Object(a["createVNode"])(m,{message:c.errorMessage,duration:c.errorDuration,bottom:c.floatBottom,class:"is-danger subtitle",onDeleted:t[1]||(t[1]=function(t){return e.$emit("dismissed")})},null,8,["message","duration","bottom"])],2)):c.successMessage?(Object(a["openBlock"])(),Object(a["createBlock"])("div",{key:1,class:["flex row ca snackbar ontop",c.floatBottom?"bottom":"top"]},[Object(a["createVNode"])(m,{message:c.successMessage,bottom:c.floatBottom,duration:c.successDuration,class:"is-success is-light",onDeleted:t[2]||(t[2]=function(t){return e.$emit("dismissed")})},null,8,["message","bottom","duration"])],2)):Object(a["createCommentVNode"])("",!0),Object(a["createVNode"])(a["Transition"],{name:"slide-fade-bottom",mode:"out-in"},{default:Object(a["withCtx"])((function(){return[c.hide?Object(a["createCommentVNode"])("",!0):(Object(a["openBlock"])(),Object(a["createBlock"])("div",{key:0,class:["flex row ca",{"snackbar bottom":c.floatBottom}]},[Object(a["createVNode"])("div",{class:{"box has-background-link-dark":c.floatBottom}},[d.confirmingCancel?(Object(a["openBlock"])(),Object(a["createBlock"])("span",{key:0,class:["level",{"has-text-light":c.floatBottom}],innerHTML:c.cancelConfirmation},null,10,["innerHTML"])):Object(a["createCommentVNode"])("",!0),d.confirmingSubmit?(Object(a["openBlock"])(),Object(a["createBlock"])("span",{key:1,class:["level",{"has-text-light":c.floatBottom}],innerHTML:c.submitConfirmation},null,10,["innerHTML"])):Object(a["createCommentVNode"])("",!0),Object(a["createVNode"])("div",o,[Object(a["createVNode"])("div",i,[Object(a["createVNode"])("button",{type:"button",class:["button",{"is-loading":!0===c.loading,"is-link is-light":!c.redGreen,"is-danger is-light":c.redGreen}],onClick:t[3]||(t[3]=function(e){return u.cancel()})},Object(a["toDisplayString"])(void 0===c.cancelText||d.confirmingCancel?"Cancelar":c.cancelText),3)]),d.confirmingCancel?(Object(a["openBlock"])(),Object(a["createBlock"])("div",n,[Object(a["createVNode"])("button",{type:"button",class:["button is-danger",{"is-loading":!0===c.loading}],onClick:t[4]||(t[4]=function(e){d.confirmingCancel=!1,b.$emit("leave")})},Object(a["toDisplayString"])(void 0!==c.cancelConfButton?c.cancelConfButton:"Confirmar"),3)])):d.confirmingSubmit?(Object(a["openBlock"])(),Object(a["createBlock"])("div",r,[Object(a["createVNode"])("button",{type:"submit",class:["button is-success",{"is-loading":!0===c.loading}]},Object(a["toDisplayString"])(void 0!==c.submitConfButton?c.submitConfButton:"Confirmar"),3)])):(Object(a["openBlock"])(),Object(a["createBlock"])("div",s,[Object(a["createVNode"])("button",{type:c.submitConfirmation?"button":"submit",class:["button",{"is-loading":!0===c.loading,"is-link":!c.redGreen,"is-success is-light":c.redGreen}],onClick:t[5]||(t[5]=function(e){return u.submit()})},Object(a["toDisplayString"])(void 0!==c.submitText?c.submitText:"Submeter"),11,["type"])]))])],2)],2))]})),_:1})])}var d=c("2b9d"),u={components:{Notification:d["a"]},name:"Submit",data:function(){return{confirmingCancel:!1,confirmingSubmit:!1}},props:["error","errorMessage","errorDuration","loading","successMessage","successDuration","submitText","cancelText","redGreen","hide","floatBottom","cancelConfirmation","submitConfirmation","cancelConfButton","submitConfButton"],methods:{cancel:function(){this.cancelConfirmation?this.confirmingCancel?this.confirmingCancel=!1:this.confirmingSubmit?this.confirmingSubmit=!1:this.confirmingCancel=!0:this.$emit("leave")},submit:function(){this.submitConfirmation&&(this.confirmingSubmit=!0)}},watch:{error:{immediate:!0,handler:function(){this.confirmingCancel=!1,this.confirmingSubmit=!1}},successMessage:{immediate:!0,handler:function(){this.confirmingCancel=!1,this.confirmingSubmit=!1}}}};u.render=l;t["a"]=u},"2b9d":function(e,t,c){"use strict";var a=c("7a23");function o(e,t,c,o,i,n){return Object(a["openBlock"])(),Object(a["createBlock"])(a["Transition"],{name:c.bottom?"slide-fade-bottom":"slide-fade",class:"box notification",mode:"out-in"},{default:Object(a["withCtx"])((function(){return[Object(a["withDirectives"])(Object(a["createVNode"])("span",null,[Object(a["createVNode"])("button",{type:"button",class:"delete",onClick:t[1]||(t[1]=function(e){return n.deactivate()})}),Object(a["createTextVNode"])(" "+Object(a["toDisplayString"])(c.message),1)],512),[[a["vShow"],i.active]])]})),_:1},8,["name"])}var i=c("1da1"),n=(c("96cf"),c("d3b7"),{name:"Notification",props:["message","duration","bottom"],emits:["deleted"],data:function(){return{active:!1}},mounted:function(){var e=this;return Object(i["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:if(e.active=!0,!e.duration){t.next=5;break}return t.next=4,new Promise((function(t){return setTimeout(t,e.duration)}));case 4:e.deactivate();case 5:case"end":return t.stop()}}),t)})))()},methods:{deactivate:function(){var e=this;return Object(i["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e.active=!1,t.next=3,new Promise((function(e){return setTimeout(e,500)}));case 3:e.$emit("deleted");case 4:case"end":return t.stop()}}),t)})))()}}});n.render=o;t["a"]=n},"64dd":function(e,t,c){"use strict";c("6e4d")},"6e4d":function(e,t,c){},"84c2":function(e,t,c){"use strict";c.r(t);var a=c("7a23"),o=c("8616"),i=c.n(o),n={class:"box"},r={class:"flex row ra"},s=Object(a["createVNode"])("span",{class:"icon"},[Object(a["createVNode"])("i",{class:"fas fa-upload"})],-1),l=Object(a["createVNode"])("span",null,"Emitir",-1),d=Object(a["createVNode"])("span",{class:"icon"},[Object(a["createVNode"])("i",{class:"fas fa-download"})],-1),u=Object(a["createVNode"])("span",null,"Cancelar emissão",-1),b=Object(a["createVNode"])("button",{class:"button is-primary",type:"button",onclick:"window.print()"},[Object(a["createVNode"])("span",{class:"icon"},[Object(a["createVNode"])("i",{class:"fas fa-print"})]),Object(a["createVNode"])("span",null,"Pré-visualizar")],-1),m={id:"printarea"},p={class:"flex my-column"},f={class:"flex row height-half"},h=Object(a["createVNode"])("div",{class:"flex my-column ca vca half-width",style:{padding:"5mm"}},[Object(a["createVNode"])("img",{src:i.a,style:{width:"80mm"}}),Object(a["createVNode"])("div",{class:"spacer"}),Object(a["createVNode"])("span",null,[Object(a["createVNode"])("b",null,"Deve ter este bilhete consigo no momento de entrada no recinto do evento.")]),Object(a["createVNode"])("div",{class:"half-spacer"}),Object(a["createVNode"])("span",null,"O bilhete pode ser impresso ou usado em formato digital. Se perder o bilhete deve proceder ao pedido da emissão de um novo bilhete na plataforma de eventos."),Object(a["createVNode"])("div",{class:"half-spacer"}),Object(a["createVNode"])("span",null,"O código QR neste bilhete serve como comprovativo de inscrição. Não deve partilhá-lo com ninguém, excepto com a organização ao fazer o registo da sua presença.")],-1),O=Object(a["createVNode"])("hr",{class:"is-hidden-print"},null,-1),j={class:"half-width"},v={id:"qrcode",class:"flex my-column ca vca"},g=Object(a["createVNode"])("h2",{class:"is-size-2"}," Código de registo de presença ",-1),V=Object(a["createVNode"])("hr",{class:"is-hidden-print"},null,-1),N={class:"flex row height-half"},y=Object(a["createStaticVNode"])('<div class="flex my-column ca vca inverted half-width" style="padding:5mm;"><h2 class="is-size-3"> Identificação </h2><div class="spacer"></div><h3 class="is-size-2"> Nome do participante </h3></div><hr class="is-hidden-print">',2),k={class:"flex my-column ca vca inverted  half-width",style:{padding:"5mm"}},C=Object(a["createVNode"])("h2",{class:"is-size-2"}," Dados do Evento ",-1),x={class:"is-size-3"},B=Object(a["createVNode"])("div",{class:"spacer"},null,-1),w={key:0},S=Object(a["createVNode"])("b",null,"Início esperado:",-1),D={key:1},T=Object(a["createVNode"])("b",null,"Fim esperado:",-1),z={key:2},I=Object(a["createVNode"])("b",null,"Localização:",-1),R=Object(a["createVNode"])("br",null,null,-1),$=Object(a["createVNode"])("br",null,null,-1),_=Object(a["createVNode"])("span",null,[Object(a["createVNode"])("b",null,"Acesso Wi-Fi")],-1),M=Object(a["createVNode"])("br",null,null,-1),P=Object(a["createVNode"])("span",null,[Object(a["createVNode"])("b",null,"SSID: "),Object(a["createTextVNode"])(" ualg-conferencias")],-1),E=Object(a["createVNode"])("span",null,[Object(a["createVNode"])("b",null,"Password: "),Object(a["createTextVNode"])(" Não sei :(")],-1),L=Object(a["createVNode"])("br",null,null,-1),F=Object(a["createVNode"])("br",null,null,-1),G={key:3},U=Object(a["createVNode"])("b",null,"Contactos de emergência",-1),A=Object(a["createVNode"])("br",null,null,-1),q={key:4},H={key:5},J=Object(a["createVNode"])("hr",{class:"is-hidden-print"},null,-1),Q={class:"flex my-column"},W={class:"flex row height-half"},X=Object(a["createVNode"])("div",{class:"flex my-column ca vca half-width",style:{padding:"5mm"}},[Object(a["createVNode"])("img",{src:i.a,style:{width:"80mm"}}),Object(a["createVNode"])("div",{class:"spacer"}),Object(a["createVNode"])("span",null,[Object(a["createVNode"])("b",null,"Deve ter este bilhete consigo no momento de entrada no recinto do evento.")]),Object(a["createVNode"])("div",{class:"half-spacer"}),Object(a["createVNode"])("span",null,"O bilhete pode ser impresso ou usado em formato digital. Se perder o bilhete deve proceder ao pedido da emissão de um novo bilhete na plataforma de eventos."),Object(a["createVNode"])("div",{class:"half-spacer"}),Object(a["createVNode"])("span",null,"O código QR neste bilhete serve como comprovativo de inscrição. Não deve partilhá-lo com ninguém, excepto com a organização ao fazer o registo da sua presença.")],-1),K=Object(a["createVNode"])("hr",{class:"is-hidden-print"},null,-1),Y={class:"half-width"},Z={id:"qrcode",class:"flex my-column ca vca"},ee=Object(a["createVNode"])("h2",{class:"is-size-2"}," Código de registo de presença ",-1),te=Object(a["createVNode"])("hr",{class:"is-hidden-print"},null,-1),ce={class:"flex row height-half"},ae=Object(a["createStaticVNode"])('<div class="flex my-column ca vca inverted half-width" style="padding:5mm;"><h2 class="is-size-3"> Identificação </h2><div class="spacer"></div><h3 class="is-size-2"> Nome do participante </h3></div><hr class="is-hidden-print">',2),oe={class:"flex my-column ca vca inverted  half-width",style:{padding:"5mm"}},ie=Object(a["createVNode"])("h2",{class:"is-size-2"}," Dados do Evento ",-1),ne={class:"is-size-3"},re=Object(a["createVNode"])("div",{class:"spacer"},null,-1),se={class:"mb-3"},le=Object(a["createVNode"])("b",null,"Início esperado:",-1),de={class:"mb-4"},ue=Object(a["createVNode"])("b",null,"Fim esperado:",-1),be=Object(a["createVNode"])("b",null,"Localização:",-1),me=Object(a["createTextVNode"])(),pe=Object(a["createStaticVNode"])("<br><br><span><b>Acesso Wi-Fi</b></span><br><span><b>SSID: </b> ualg-conferencias</span><span><b>Password: </b> Não sei :(</span><br><br><span><b>Contactos de emergência</b></span><br>",10),fe={class:"mb-2"},he=Object(a["createVNode"])("hr",{class:"is-hidden-print"},null,-1);function Oe(e,t,c,o,i,Oe){var je=this,ve=Object(a["resolveComponent"])("vue-qrcode"),ge=Object(a["resolveComponent"])("Input"),Ve=Object(a["resolveComponent"])("Submit");return Object(a["openBlock"])(),Object(a["createBlock"])("div",n,[Object(a["createVNode"])("div",r,[i.certificate.id&&!i.certificate.available?(Object(a["openBlock"])(),Object(a["createBlock"])("button",{key:0,class:["button is-link mr-3",{"is-loading":i.loading_publish}],type:"button",disabled:0!=i.changes,title:0!=i.changes?"Deve guardar o bilhete antes de o emitir":"Um bilhete emitido fica automáticamente disponível para todos os participantes com inscrição validada e participantes que futuramente tenham a sua inscrição validada.",onClick:t[1]||(t[1]=function(e){return Oe.activate()})},[s,l],10,["disabled","title"])):Object(a["createCommentVNode"])("",!0),i.certificate.id&&i.certificate.available?(Object(a["openBlock"])(),Object(a["createBlock"])("button",{key:1,class:["button is-link mr-3",{"is-loading":i.loading_publish}],type:"button",disabled:0!=i.changes,title:0!=i.changes?"Deve guardar o bilhete antes de o emitir":"Um bilhete cuja emissão é cancelada passa a estar indisponível para impressão, mas se for emitido novamente os códigos de validação mantém-se e bilhetes já emitidos podem continuar a ser usados.",onClick:t[2]||(t[2]=function(e){Oe.activate()})},[d,u],10,["disabled","title"])):Object(a["createCommentVNode"])("",!0),b]),Object(a["createVNode"])("div",m,[Object(a["createVNode"])("div",null,[Object(a["createVNode"])("div",p,[Object(a["createVNode"])("div",f,[h,O,Object(a["createVNode"])("div",j,[Object(a["createVNode"])("div",v,[g,Object(a["createVNode"])(ve,{value:"Apenas um exemplo, não pode ser usado para registo de presença",options:{width:300}})])])]),V,Object(a["createVNode"])("div",N,[y,Object(a["createVNode"])("div",k,[C,Object(a["createVNode"])("h3",x,Object(a["toDisplayString"])(i.certificate.event_name),1),B,i.certificate.start?(Object(a["openBlock"])(),Object(a["createBlock"])("span",w,[S,Object(a["createTextVNode"])(" "+Object(a["toDisplayString"])(i.certificate.start),1)])):Object(a["createCommentVNode"])("",!0),i.certificate.end?(Object(a["openBlock"])(),Object(a["createBlock"])("span",D,[T,Object(a["createTextVNode"])(" "+Object(a["toDisplayString"])(i.certificate.end),1)])):Object(a["createCommentVNode"])("",!0),i.certificate.location?(Object(a["openBlock"])(),Object(a["createBlock"])("span",z,[I,Object(a["createTextVNode"])(" "+Object(a["toDisplayString"])(i.certificate.location),1)])):Object(a["createCommentVNode"])("",!0),R,$,_,M,P,E,L,F,i.certificate.emergencyContact1||i.certificate.emergencyContact2?(Object(a["openBlock"])(),Object(a["createBlock"])("span",G,[U])):Object(a["createCommentVNode"])("",!0),A,i.certificate.emergencyContact1?(Object(a["openBlock"])(),Object(a["createBlock"])("span",q,Object(a["toDisplayString"])(i.certificate.emergencyContact1),1)):Object(a["createCommentVNode"])("",!0),i.certificate.emergencyContact2?(Object(a["openBlock"])(),Object(a["createBlock"])("span",H,Object(a["toDisplayString"])(i.certificate.emergencyContact2),1)):Object(a["createCommentVNode"])("",!0)]),J])])])]),Object(a["createVNode"])("form",{id:"editarea",ref:"form",onSubmit:t[15]||(t[15]=Object(a["withModifiers"])((function(e){return Oe.submit()}),["prevent"]))},[Object(a["createVNode"])("div",null,[Object(a["createVNode"])("div",Q,[Object(a["createVNode"])("div",W,[X,K,Object(a["createVNode"])("div",Y,[Object(a["createVNode"])("div",Z,[ee,Object(a["createVNode"])(ve,{value:"Apenas um exemplo, não pode ser usado para registo de presença",options:{width:300}})])])]),te,Object(a["createVNode"])("div",ce,[ae,Object(a["createVNode"])("div",oe,[ie,Object(a["createVNode"])("h3",ne,Object(a["toDisplayString"])(i.certificate.event_name?i.certificate.event_name:"Nome do Evento"),1),re,Object(a["createVNode"])("span",se,[le,Object(a["createVNode"])(ge,{modelValue:i.certificate.start,"onUpdate:modelValue":t[3]||(t[3]=function(e){return i.certificate.start=e}),type:"text",maxlength:"128",class:"is-small display-edit",placeholder:"Início",style:{"text-align":"center"},onInput:t[4]||(t[4]=function(e){return i.changes++})},null,8,["modelValue"])]),Object(a["createVNode"])("span",de,[ue,Object(a["createVNode"])(ge,{modelValue:i.certificate.end,"onUpdate:modelValue":t[5]||(t[5]=function(e){return i.certificate.end=e}),type:"text",maxlength:"128",class:"is-small display-edit",placeholder:"Fim",style:{"text-align":"center"},onInput:t[6]||(t[6]=function(e){return i.changes++})},null,8,["modelValue"])]),Object(a["createVNode"])("span",null,[be,me,Object(a["createVNode"])(ge,{modelValue:i.certificate.location,"onUpdate:modelValue":t[7]||(t[7]=function(e){return i.certificate.location=e}),type:"text",maxlength:"128",class:"is-small display-edit",placeholder:"Localização",style:{"text-align":"center"},required:"",onInput:t[8]||(t[8]=function(e){return i.changes++})},null,8,["modelValue"])]),pe,Object(a["createVNode"])("span",fe,[Object(a["createVNode"])(ge,{modelValue:i.certificate.emergencyContact1,"onUpdate:modelValue":t[9]||(t[9]=function(e){return i.certificate.emergencyContact1=e}),class:"display-edit is-small",type:"text",maxlength:"64",placeholder:"Contacto de Emergência",style:{"text-align":"center"},onInput:t[10]||(t[10]=function(e){return i.changes++})},null,8,["modelValue"])]),Object(a["createVNode"])("span",null,[Object(a["createVNode"])(ge,{modelValue:i.certificate.emergencyContact2,"onUpdate:modelValue":t[11]||(t[11]=function(e){return i.certificate.emergencyContact2=e}),class:"display-edit is-small",type:"text",maxlength:"64",placeholder:"Contacto de Emergência",style:{"text-align":"center"},onInput:t[12]||(t[12]=function(e){return i.changes++})},null,8,["modelValue"])])]),he])])]),Object(a["createVNode"])(Ve,{id:"submit",style:{width:"fit-content"},hide:0==i.changes,"float-bottom":"true",error:i.response&&void 0===i.response.id,"error-message":"Houve um erro na submissão do bilhete.","success-duration":"3000","success-message":i.success,loading:i.loading,"submit-text":"Guardar","red-green":"true","cancel-confirmation":"Pretende eliminar as suas alterações?","submit-confirmation":"Pretende guardar as suas alterações?","cancel-conf-button":"Eliminar","submit-conf-button":"Guardar",onLeave:t[13]||(t[13]=function(e){return Oe.cancel()}),onDismissed:t[14]||(t[14]=function(e){je.response=void 0,je.success=void 0})},null,8,["hide","error","success-message","loading"])],544)])}var je=c("1da1"),ve=(c("96cf"),c("99af"),c("1270")),ge=c("1995"),Ve=c("69d9"),Ne=c("c427"),ye=c("d56f"),ke={name:"CreateTicket",components:{VueQrcode:ye["a"],Input:ve["a"],Submit:ge["a"]},data:function(){return{certificate:{event:this.$route.params.id},response:void 0,success:void 0,changes:0,loading:void 0,invalid:!1,validity_valid:!0,loading_publish:!1}},created:function(){var e=this;document.title="Criar Bilhete de Acesso",Ne["a"].get("ticket/?event=".concat(this.$route.params.id)).then((function(t){t.data[0]&&(e.certificate=t.data[0],document.title="Editar Bilhete de Acesso")})).catch()},methods:{cancel:function(){var e=this;this.loading=!0,this.$route.params.id?Ne["a"].get("ticket/?event=".concat(this.$route.params.id)).then((function(t){e.certificate=t.data[0],e.changes=0,e.loading=void 0})):this.$router.back()},submit:function(){this.$refs.form.checkValidity()&&(this.loading=!0,setTimeout(this.postSubmission.bind(this),0))},activate:function(){var e,t,c,a=this;this.loading_publish=!0,e="patch",t="/ticket/".concat(this.certificate.id).concat("/"),c="O bilhete foi "+(this.certificate.available?"desativado":"emitido")+" com sucesso. Pode continuar a editar.";var o={method:e,url:t,headers:{"X-CSRFToken":Object(Ve["b"])("csrftoken")},data:{available:!this.certificate.available},transformResponse:[function(){var e=Object(je["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:a.loading=void 0;try{a.response=JSON.parse(t),a.certificate=a.response,a.success=c,a.loading_publish=!1}catch(o){a.response=t}return e.abrupt("return",a.response);case 3:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}()]};Object(Ne["a"])(o)},postSubmission:function(){var e,t,c,a=this;void 0===this.certificate.id?(e="post",t="/ticket/",c="O bilhete foi criado com sucesso. Pode continuar a editar."):(e="put",t="/ticket/".concat(this.certificate.id).concat("/"),c="O bilhete foi editado com sucesso. Pode continuar a editar.");var o={method:e,url:t,headers:{"X-CSRFToken":Object(Ve["b"])("csrftoken")},data:this.certificate,transformResponse:[function(){var e=Object(je["a"])(regeneratorRuntime.mark((function e(t){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:a.loading=void 0;try{a.response=JSON.parse(t),a.certificate=a.response,a.success=c,a.changes=0}catch(o){a.response=t}return e.abrupt("return",a.response);case 3:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}()]};Object(Ne["a"])(o)},valid:function(){return!this.invalid||this.$refs["input"].validity.valid},updateValidity:function(){this.validity_valid=this.$refs["input"].validity.valid}}};c("85cc"),c("64dd");ke.render=Oe;t["default"]=ke},"85cc":function(e,t,c){"use strict";c("de65")},de65:function(e,t,c){}}]);
//# sourceMappingURL=chunk-75d566b2.2ef08c70.js.map